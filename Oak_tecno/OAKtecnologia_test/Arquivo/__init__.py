from OAKtecnologia_test.Interface import *


#verifica se existe arquivo
def existeArquivo(nome):

    try:
        a = open(nome, 'rt+')#rt+ Abre Arquivos
        a.close()#Fecha arquivo
    except FileNotFoundError:
        return False
    else:
        return True

#Cria o arquivo caso n exista
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')#wt+ Cria Arquivos
        a.close()
    except:
        print("Erro ao criar arquivo.txt")
    else:
        print(f"Arquivo {nome} Criado com sucesso!")

#organiza o arquivo txt
def organizaCrescente(arq):
    try:
        # le arquivos
        a = open(arq, 'r')
        newFile = []
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace('\n', '')
            newFile.append(dado)

        #Organiza a lista em forma crescente
        newFile.sort(key=lambda x: float(x[1]), reverse=False)
        return newFile
    #Verifica erro
    except IndexError:
        txt("ARQUIVO VAZIO",cor=1)

#Reescreve arquivo formatado
def reescreveArquivo(arq,newFile):
    #Reescreve separado por ';'
    try:
        a = open(arq,'r+',encoding='utf8')
        a.truncate(0)
        a.seek(0)
        for position in newFile:
            a.writelines(f'{position[0]};{position[1]}\n')
    # Verifica erro
    except TypeError:
        txt("ARQUIVO VAZIO",cor=1)

def lerArquivo(nome_Arquivo):
    try:
        """rt le arquivos"""
        a = open(nome_Arquivo, 'rt')
    except:
        print("Erro Desconhecido")
    else:
        txt("PRODUTOS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
         a.close()

#Cadastra os produtos e os valores
def cadastrar(arq, nome_produto="Nulo", valor=0):
    try:
        a= open(arq, 'at')#escreve
        b= open(arq, 'rt')#le
    except:
        print('Houve um Erro na abertura do arquivo')
    else:
        try:
                a.write(f'{nome_produto};{valor}\n')
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de produto: {nome_produto} cadastrado.\n")
            lerArquivo(arq)
            print(f'{nome_produto:<30}{valor:>3}')
            a.close()