from Vendedor import *
from PlanilhaVendedor import processar_planilha

#Arquivo aonde os testes sao feitos

if __name__ == "__main__":
    #vendedor1 = Vendedor(nome="Lucas",cpf="123",datansc="2005-04-12",email="123@hotmail.com",estado="SC")

    """Inserindo o Vendedor criado"""
    #LISTA_VENDEDORES.append(vendedor1)

    """Lendo um Vendedor pelo seu cpf"""
    #print(readVendedor("123"))

    """Tentando atualizar um Vendedor sem o cpf cadastrado"""
    #updateVendedor(vendedor1, nome="Joao", cpf="070", datansc="2004-12-12", email="jao@hotmail.com", estado="SC")

    """Atualizando um Vendedor com o cpf cadastrado"""
    #updateVendedor(vendedor1, nome="Claudio", cpf="123", datansc="2005-12-12", email="claudio@hotmail.com", estado="SC")

    """Lendo o Vendedor atualizado"""
    #print(readVendedor("123"))

    """Deletando um Vendedor pelo cpf"""
    #deleteVendedor("123")

    """Verificando se o Vendedor foi deletado"""
    #print(readVendedor("123"))

    processar_planilha('Caso 1 e 2/DadosVendedores.xlsx')

    print(getVendedor())