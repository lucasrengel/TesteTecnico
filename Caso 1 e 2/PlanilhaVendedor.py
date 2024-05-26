import pandas as pd # type: ignore
from Vendedor import *

def processar_planilha(nome_arquivo):
    # Carrega a planilha
    excel = pd.read_excel(nome_arquivo)

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