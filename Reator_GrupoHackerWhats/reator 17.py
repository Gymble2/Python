import numpy as np

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
    densidade_eletrons = np.maximum(densidade_eletrons, 0)
    return np.sqrt(densidade_eletrons * e**2 / (me * epsilon_0))

def eficiencia_temperatura(temperatura_atual, temp_max_eficiencia):
    sigma = temp_max_eficiencia / 5
    return np.exp(-((temperatura_atual - temp_max_eficiencia)**2) / (2 * sigma**2))

def eficiencia_ressonancia(frequencia_plasma, frequencia_ressonancia):
    sigma = frequencia_ressonancia / 5
    return np.exp(-((frequencia_plasma - frequencia_ressonancia)**2) / (2 * sigma**2))

def energia_liberada(densidade_eletrons, temperatura):
    return densidade_eletrons * temperatura * 1e-20

def energia_gasta_ajuste_frequencia(frequencia_plasma, frequencia_ressonancia):
    return np.abs(frequencia_plasma - frequencia_ressonancia) * 1e-5

# Função objetivo
def objective_function(densidade_eletrons, temperatura_atual, temp_max_eficiencia, frequencia_ressonancia):
    frequencia_plasma = calcular_frequencia_plasma(densidade_eletrons)
    eta_temp = eficiencia_temperatura(temperatura_atual, temp_max_eficiencia)
    eta_res = eficiencia_ressonancia(frequencia_plasma, frequencia_ressonancia)
    energia = energia_liberada(densidade_eletrons, temperatura_atual)
    custo = energia_gasta_ajuste_frequencia(frequencia_plasma, frequencia_ressonancia)
    return eta_temp * eta_res * energia - custo

# Algoritmo FuFiO
def initialize_population(size, lower_bound, upper_bound, densidade_inicial):
    return densidade_inicial + np.random.uniform(lower_bound, upper_bound, size)

def fusion(solutions):
    return np.mean(solutions)

def fission(solution, num_sub_solutions, perturbation):
    return solution + np.random.uniform(-perturbation, perturbation, num_sub_solutions)

def select_best_solutions(solutions, objective_function, num_best, temperatura_atual, temp_max_eficiencia, frequencia_ressonancia):
    fitness = np.array([objective_function(sol, temperatura_atual, temp_max_eficiencia, frequencia_ressonancia) for sol in solutions])
    best_indices = np.argsort(fitness)[-num_best:]
    return solutions[best_indices]

def fufio_multipop(objective_function, pop_size, num_generations, lower_bound, upper_bound, num_best, perturbation, elementos):
    populacoes = {elem: initialize_population(pop_size, lower_bound, upper_bound, props['densidade_inicial']) for elem, props in elementos.items()}
    
    for generation in range(num_generations):
        for elem, props in elementos.items():
            temperatura_atual = props['temperatura_inicial']
            temp_max_eficiencia = props['temp_max_eficiencia']
            frequencia_ressonancia = props['frequencia_ressonancia']
            populacao = populacoes[elem]
            
            populacoes[elem] = select_best_solutions(populacao, objective_function, num_best, temperatura_atual, temp_max_eficiencia, frequencia_ressonancia)
            
            fused_solution = fusion(populacoes[elem])
            populacoes[elem] = fission(fused_solution, pop_size, perturbation)
    
    melhores_solucoes = {elem: np.mean(populacao) for elem, populacao in populacoes.items()}
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
    
    # Para máxima conversão em trítio, o lítio deve ser convertido em trítio
    densidade_tritio_desejada = densidade_litio
    densidade_protons_necessaria = densidade_tritio_desejada - elementos["Trítio"]["densidade_inicial"]
    densidade_protons_necessaria = max(densidade_protons_necessaria, 0)  # Garantir que não seja negativo
    
    print(f"Densidade total de lítio disponível: {densidade_litio:.2e}")
    print(f"Densidade de trítio desejada: {densidade_tritio_desejada:.2e}")
    print(f"Densidade de prótons necessários: {densidade_protons_necessaria:.2e}")

# Função para calcular a quantidade de nêutrons liberados
def calcular_neutrons_liberados(densidade_litio, densidade_tritio):
    # Assumindo que a conversão de lítio para trítio libera nêutrons
    # Aqui simplificamos a suposição de que cada átomo de lítio convertido em trítio libera um nêutron
    return densidade_litio - densidade_tritio

# Função para imprimir os nêutrons liberados
def imprimir_neutrons_liberados(melhores_solucoes):
    densidade_litio = melhores_solucoes["Lítio"]
    densidade_tritio = melhores_solucoes["Trítio"]
    neutrons_liberados = calcular_neutrons_liberados(densidade_litio, densidade_tritio)
    print(f"Nêutrons liberados: {neutrons_liberados:.2e}")

# Função para calcular e imprimir a quantidade de nêutrons necessários para a fissão de 100% do lítio
def calcular_neutrons_necessarios_fissao(densidade_litio_inicial):
    # Assumindo que cada átomo de lítio precisa de um nêutron para se converter em trítio
    return densidade_litio_inicial

# Função para imprimir os resultados das melhores soluções
def imprimir_resultados(melhores_solucoes, elementos):
    for elem, sol in melhores_solucoes.items():
        props = elementos[elem]
        print(f"Melhor solução para {elem}:")
        print(f"Densidade de elétrons: {sol}")
        print(f"Temperatura inicial: {props['temperatura_inicial']}")
        print(f"Temperatura de máxima eficiência: {props['temp_max_eficiencia']}")
        print(f"Frequência de ressonância: {props['frequencia_ressonancia']}")
        print("")

# Parâmetros do algoritmo FuFiO
pop_size = 100
num_generations = 50
lower_bound = -1e16
upper_bound = 1e16
num_best = 10
perturbation = 1e16

# Executar o algoritmo FuFiO
melhores_solucoes = fufio_multipop(objective_function, pop_size, num_generations, lower_bound, upper_bound, num_best, perturbation, elementos)

# Calcular e imprimir os percentuais ideais
percentuais_ideais = calcular_percentuais_ideais(melhores_solucoes, elementos)
for elem, percentual in percentuais_ideais.items():
    print(f"Percentual ideal de {elem}: {percentual:.2f}%")

# Calcular e imprimir os prótons necessários
calcular_protons_necessarios(melhores_solucoes, elementos)

# Calcular e imprimir os nêutrons liberados
imprimir_neutrons_liberados(melhores_solucoes)

# Calcular e imprimir a quantidade de nêutrons necessários para a fissão de 100% do lítio
densidade_litio_inicial = elementos["Lítio"]["densidade_inicial"]
neutrons_necessarios = calcular_neutrons_necessarios_fissao(densidade_litio_inicial)
print(f"Nêutrons necessários para fissão de 100% do lítio: {neutrons_necessarios:.2e}")

# Imprimir os resultados das melhores soluções
imprimir_resultados(melhores_solucoes, elementos)

