import cupy as cp
from multiprocessing import Pool, cpu_count
import logging
import numpy as np
import os
import time

os.add_dll_directory('C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.5/bin')

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definição das propriedades dos elementos
elementos = {
    "Hidrogênio": {"densidade_inicial": 1e18, "temperatura_inicial": 1e6, "temp_max_eficiencia": 2e6, "frequencia_ressonancia": 1e9, "percentual_ideal": 0.5},
    "Hélio": {"densidade_inicial": 5e18, "temperatura_inicial": 2e6, "temp_max_eficiencia": 3e6, "frequencia_ressonancia": 5e9, "percentual_ideal": 0.3},
    "Lítio": {"densidade_inicial": 1e19, "temperatura_inicial": 3e6, "temp_max_eficiencia": 4e6, "frequencia_ressonancia": 1e10, "percentual_ideal": 0.2},
    "Trítio": {"densidade_inicial": 1e17, "temperatura_inicial": 3.5e6, "temp_max_eficiencia": 4.5e6, "frequencia_ressonancia": 1.2e10, "percentual_ideal": 0.01}
}

# Funções de cálculo
def calcular_frequencia_plasma(densidade_eletrons):
    e = 1.60217662e-19
    me = 9.10938356e-31
    epsilon_0 = 8.85418782e-12
    
    # Garantir que a densidade de elétrons seja positiva
    densidade_eletrons = cp.maximum(densidade_eletrons, 0)
    return cp.sqrt(densidade_eletrons * e**2 / (me * epsilon_0))

def eficiencia_temperatura(temperatura_atual, temp_max_eficiencia):
    sigma = temp_max_eficiencia / 5
    return cp.exp(-((temperatura_atual - temp_max_eficiencia)**2) / (2 * sigma**2))

def eficiencia_ressonancia(frequencia_plasma, frequencia_ressonancia):
    sigma = frequencia_ressonancia / 5
    return cp.exp(-((frequencia_plasma - frequencia_ressonancia)**2) / (2 * sigma**2))

def energia_liberada(densidade_eletrons, temperatura):
    return densidade_eletrons * temperatura * 1e-20

def energia_gasta_ajuste_frequencia(frequencia_plasma, frequencia_ressonancia):
    return cp.abs(frequencia_plasma - frequencia_ressonancia) * 1e-5

# Função objetivo
def objective_function(args):
    densidade_eletrons, temperatura_atual, temp_max_eficiencia, frequencia_ressonancia = args
    frequencia_plasma = calcular_frequencia_plasma(densidade_eletrons)
    eta_temp = eficiencia_temperatura(temperatura_atual, temp_max_eficiencia)
    eta_res = eficiencia_ressonancia(frequencia_plasma, frequencia_ressonancia)
    energia = energia_liberada(densidade_eletrons, temperatura_atual)
    custo = energia_gasta_ajuste_frequencia(frequencia_plasma, frequencia_ressonancia)
    return (eta_temp * eta_res * energia - custo).get()

# Algoritmo FuFiO
def initialize_population(size, lower_bound, upper_bound, densidade_inicial):
    return cp.array(densidade_inicial + np.random.uniform(lower_bound, upper_bound, size))

def fusion(solutions):
    return cp.mean(solutions)

def fission(solution, num_sub_solutions, perturbation):
    return solution + cp.random.uniform(-perturbation, perturbation, num_sub_solutions)

def select_best_solutions(solutions, args_list, num_best):
    logging.info("Calculando fitness das soluções.")
    with Pool(cpu_count()) as pool:
        fitness = pool.map(objective_function, args_list)
    fitness = cp.array(fitness)
    best_indices = cp.argsort(fitness)[-num_best:]
    return solutions[best_indices]

def fufio_multipop(objective_function, pop_size, num_generations, lower_bound, upper_bound, num_best, perturbation, elementos):
    populacoes = {elem: initialize_population(pop_size, lower_bound, upper_bound, props['densidade_inicial']) for elem, props in elementos.items()}
    tempo_total = 0

    inicio_total = time.time()

    for generation in range(num_generations):
        inicio_geracao = time.time()

        for elem, props in elementos.items():
            temperatura_atual = props['temperatura_inicial']
            temp_max_eficiencia = props['temp_max_eficiencia']
            frequencia_ressonancia = props['frequencia_ressonancia']
            populacao = populacoes[elem]

            args_list = [(sol, temperatura_atual, temp_max_eficiencia, frequencia_ressonancia) for sol in cp.asnumpy(populacao)]
            populacoes[elem] = select_best_solutions(populacao, args_list, num_best)

            fused_solution = fusion(populacoes[elem])
            populacoes[elem] = fission(fused_solution, pop_size, perturbation)

        fim_geracao = time.time()
        tempo_geracao = fim_geracao - inicio_geracao
        tempo_total += tempo_geracao

        logging.info(f"Geração {generation + 1}: Tempo estimado {tempo_geracao:.2f} segundos")

    fim_total = time.time()
    tempo_total_total = fim_total - inicio_total
    logging.info(f"Tempo total do processo: {tempo_total_total:.2f} segundos")

    melhores_solucoes = {elem: cp.mean(populacao).get() for elem, populacao in populacoes.items()}
    return melhores_solucoes

# Função para calcular a porcentagem ideal de cada população
def calcular_percentuais_ideais(melhores_solucoes, elementos):
    total_densidade = sum(melhores_solucoes[elem] for elem in elementos)
    percentuais_ideais = {elem: (melhores_solucoes[elem] / total_densidade) * 100 for elem in elementos}
    return percentuais_ideais

# Função para calcular e imprimir a quantidade de prótons injetados
def calcular_protons_necessarios(melhores_solucoes, elementos):
    densidade_litio_inicial = elementos["Lítio"]["densidade_inicial"]
    densidade_helios_produzidos = melhores_solucoes["Hélio"]
    densidade_litio = densidade_litio_inicial + densidade_helios_produzidos

    densidade_tritio_desejada = densidade_litio
    densidade_protons_necessaria = densidade_tritio_desejada - elementos["Trítio"]["densidade_inicial"]
    densidade_protons_necessaria = max(densidade_protons_necessaria, 0)

    logging.info(f"Densidade total de lítio disponível: {densidade_litio:.2e}")
    logging.info(f"Densidade de trítio desejada: {densidade_tritio_desejada:.2e}")
    logging.info(f"Densidade de prótons necessários: {densidade_protons_necessaria:.2e}")

# Função para calcular a quantidade de nêutrons liberados
def calcular_neutrons_liberados(densidade_litio, densidade_tritio):
    return densidade_litio - densidade_tritio

# Função para imprimir os nêutrons liberados
def imprimir_neutrons_liberados(melhores_solucoes):
    densidade_litio = melhores_solucoes["Lítio"]
    densidade_tritio = melhores_solucoes["Trítio"]
    neutrons_liberados = calcular_neutrons_liberados(densidade_litio, densidade_tritio)
    logging.info(f"Nêutrons liberados: {neutrons_liberados:.2e}")

# Função para calcular a quantidade de nêutrons necessários para a fissão de 100% do lítio
def calcular_neutrons_necessarios_fissao(densidade_litio_inicial):
    return densidade_litio_inicial

# Função para imprimir os resultados das melhores soluções
def imprimir_resultados(melhores_solucoes, elementos):
    for elem, sol in melhores_solucoes.items():
        props = elementos[elem]
        logging.info(f"Melhor solução para {elem}:")
        logging.info(f"Densidade de elétrons: {sol}")
        logging.info(f"Temperatura inicial: {props['temperatura_inicial']}")
        logging.info(f"Temperatura máxima de eficiência: {props['temp_max_eficiencia']}")
        logging.info(f"Frequência de ressonância: {props['frequencia_ressonancia']}")

# Parâmetros do algoritmo
pop_size = 100
num_generations = 50
lower_bound = -0.1e19
upper_bound = 0.1e19
num_best = 10
perturbation = 0.01e19

# Execução do algoritmo
melhores_solucoes = fufio_multipop(objective_function, pop_size, num_generations, lower_bound, upper_bound, num_best, perturbation, elementos)

# Impressão dos resultados
imprimir_resultados(melhores_solucoes, elementos)

# Cálculo e impressão dos percentuais ideais
percentuais_ideais = calcular_percentuais_ideais(melhores_solucoes, elementos)
logging.info("Percentuais ideais das populações:")
for elem, percentual in percentuais_ideais.items():
    logging.info(f"{elem}: {percentual:.2f}%")

# Cálculo e impressão dos prótons necessários
calcular_protons_necessarios(melhores_solucoes, elementos)

# Cálculo e impressão dos nêutrons liberados
imprimir_neutrons_liberados(melhores_solucoes)

# Cálculo e impressão dos nêutrons necessários para a fissão de 100% do lítio
neutrons_necessarios_fissao = calcular_neutrons_necessarios_fissao(elementos["Lítio"]["densidade_inicial"])
logging.info(f"Nêutrons necessários para fissão de 100% do lítio: {neutrons_necessarios_fissao:.2e}")

