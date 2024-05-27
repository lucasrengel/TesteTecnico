from dataclasses import dataclass

LISTA_VENDEDORES = []

#Criando a classe Vendedor usando o @dataclass
@dataclass
class Vendedor:
    nome: str
    cpf: str
    datansc: str
    email: str
    estado: str

    def __str__(self):
        return (f"Nome: {self.nome}, "
            f"CPF: {self.cpf}, "
            f"Data de Nascimento: {self.datansc}, "
            f"Email: {self.email}, "
            f"Estado: {self.estado}, \n")

#Cria um vendedor
def createVendedor(vendedor: Vendedor):
    LISTA_VENDEDORES.append(vendedor)
    print("Vendedor adicionado com sucesso\n")

#Imprime um Vendedor ao percorrer a lista e verificar o cpf passado no parametro
def readVendedor(cpf):
    for vendedor in LISTA_VENDEDORES:
        if vendedor.cpf == cpf:
            return vendedor        
    return "CPF nao Encontrado\n"
        
#Atualiza um vendedor percorrendo a lista e verificando o cpf passado no parametro
def updateVendedor(vendedor, nome, cpf, datansc, email, estado):
    for vendedor in LISTA_VENDEDORES:
        if vendedor.cpf == cpf:
            vendedor.nome = nome
            vendedor.datansc = datansc
            vendedor.email = email
            vendedor.estado = estado
            print("Vendedor alterado com sucesso\n")
            return
    print("CPF nao encontrado\n")

#Deleta um vendedor percorrendo a lista e verificando se o cpf passado pelo parametro existe
def deleteVendedor(cpf):
    for i, vendedor in enumerate(LISTA_VENDEDORES):
        if vendedor.cpf == cpf:
            del LISTA_VENDEDORES[i]
            print("Vendedor deletado com sucesso\n")
            return
    print("CPF nao encontrado\n")
        
#Imprime todos os vendedores na lista_vendedores
def getVendedor():
    if LISTA_VENDEDORES:
        for vendedor in LISTA_VENDEDORES:
            print(vendedor)
    else:
        print("Lista vazia\n")