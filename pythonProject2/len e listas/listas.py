dados=list()
dados.append('gustavo')
dados.append(40)
galera=list()
galera.append(dados[:])
dados[0]='maria'
dados[1]='25'
galera.append(dados[:])
print(galera)