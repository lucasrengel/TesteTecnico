import pandas as pd # type: ignore
from Vendedor import *

def processar_planilha(nome_arquivo):
    # Carrega a planilha
    excel = pd.read_excel(nome_arquivo)

    #Extrai os dados da coluna da linha atual e usa os dados para verificar se um vendedor existe, criar ou atualizar
    for i, linha in excel.iterrows():
        cpf = linha.CPF
        nome = linha.Nome
        datansc = linha.Data_Nascimento  # Converte para apenas data
        email = linha.Email
        estado = linha.Estado

        # Verifica se o vendedor ja existe na lista pelo CPF
        vendedor_existente = readVendedor(cpf)

        # Se o vendedor não existir, cria um novo vendedor
        if vendedor_existente == "CPF nao Encontrado\n":
            novo_vendedor = Vendedor(nome=nome, cpf=cpf, datansc=datansc, email=email, estado=estado)
            createVendedor(novo_vendedor)
        else:
            # Se o vendedor existir, atualiza suas informacoes
            updateVendedor(vendedor_existente, nome=nome, cpf=cpf, datansc=datansc, email=email, estado=estado)