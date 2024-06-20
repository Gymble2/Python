import pandas as pd

#importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')



#visualização da base de dados
pd.set_option('display.max_columns',None)

#faturamento por loja
faturamentos =  tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamentos)

#quntidade de produtos por loja
qntd = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(qntd)

#ticket medio
medio = (faturamentos['Valor Final']/qntd['Quantidade']).to_frame()
print(medio)

#enviar email
import win32com.client as win32
outlook = win32.Dispatch('Outlook(PWA).application')
mail = outlook.CreateItem(0)
mail.To = 'gymble23@gmail.com'
mail.Subject = 'Relatório'
mail.HTMLBody = '''
Prezados,

Segue o Relatório de Vendas por cada loja.
Faturamento:
{}


Quantidade Vendida:
{}

Qualquer Dúvida estou a disposição;
{}

Amém e beijos
'''

mail.send()