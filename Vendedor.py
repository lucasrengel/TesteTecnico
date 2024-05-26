from dataclasses import dataclass


#Arquivo onde crio o construtor de Vendedor usando @dataclasses para usar no VendedorDAO como parametros

@dataclass
class Vendedor:
    nome: str
    cpf: str
    datansc: str
    email: str
    estado: str

    #Retorno para mostrar as informacoes do Vendedor
    def __str__(self):
        return (f"Nome: {self.nome}, "
                f"CPF: {self.cpf}, "
                f"Data de Nascimento: {self.datansc}, "
                f"Email: {self.email}, "
                f"Estado: {self.estado}, \n")
