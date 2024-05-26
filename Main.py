import mysql.connector  # type: ignore
from VendedorDAO import *

#Arquivo aonde os testes sao feitos

if __name__ == "__main__":
    novo_vendedor = Vendedor(
        nome="Testee",
        cpf="123",
        datansc="2005-04-12",
        email="123@hotmail.com",
        estado="SC"
    )

    #Inserindo o Vendedor criado
    insertVendedorDB(novo_vendedor)

    #Lendo um Vendedor pelo seu cpf
    print(selectVendedorDB(123))

    #Tentando atualizar um Vendedor sem o cpf cadastrado
    updateVendedorDB(nome="Joao", cpf="070", datansc="2004-12-12", email="jao@hotmail.com", estado="SC")

    #Atualizando um Vendedor com o cpf cadastrado
    updateVendedorDB(nome="Lucas", cpf="123", datansc="2005-04-12", email="lucaslangel@hotmail.com", estado="SC")

    #Lendo o Vendedor atualizado
    print(selectVendedorDB(123))

    #Deletando um Vendedor pelo cpf
    deleteVendedorDB(123)
    #Verificando se o Vendedor foi deletado
    print(selectVendedorDB(123))
