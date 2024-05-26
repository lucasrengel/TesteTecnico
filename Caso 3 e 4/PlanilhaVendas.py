import pandas as pd # type: ignore

#Carrega os dados da planilha Excel
excel = pd.read_excel("Caso 3 e 4/Vendas.xlsx")

#Funcao para converter os valores em reais para float
def converter_valor(valor):
    if isinstance(valor, str):
        valor = float(valor.replace('R$', '').replace('.', '').replace(',', '.'))
    return valor

#Aplica a funcao converter valor na planilha na coluna Valor da Venda
excel['Valor da Venda'] = excel['Valor da Venda'].apply(converter_valor)

#Funcao para calcular a comissao de cada venda
def calcular_comissao(row):
    valor_venda = row['Valor da Venda']
    canal_venda = row['Canal de Venda']

    comissao = valor_venda * 0.1

    if canal_venda == 'Online':
        comissao_vendedor = comissao * 0.8
        comissao_marketing = comissao * 0.2
    else:
        comissao_vendedor = comissao
        comissao_marketing = 0

    if comissao_vendedor >= 1000:
        comissao_vendedor = comissao * 0.9
        comissao_gerente = comissao * 0.1
    else:
        comissao_gerente = 0

    return comissao_vendedor, comissao_marketing, comissao_gerente

#Aplica a funcao calcular_comissao para calcular a comissao de cada venda
excel[['Comissao Vendedor', 'Comissao Marketing', 'Comissao Gerente']] = excel.apply(calcular_comissao, axis=1, result_type='expand')

print("Planilha de vendas:")
print(excel)

excel['Total Venda por Profissional'] = excel.groupby(['Nome do Vendedor', 'Canal de Venda'])['Valor da Venda'].transform('sum')
excel['Total Venda por Canal'] = excel.groupby('Canal de Venda')['Valor da Venda'].transform('sum')

#Remove as duplicatas pra evitar aparecer varios nomes
excel = excel.drop_duplicates(subset=['Nome do Vendedor', 'Canal de Venda'])

#Ordena a coluna Total Venda por Canal em decrescente
excel = excel.sort_values(by=['Total Venda por Canal'], ascending=False)

#Exibe a planilha atualizada
print("Planilha de vendas com total de vendas por profissional e por canal:")
print(excel)