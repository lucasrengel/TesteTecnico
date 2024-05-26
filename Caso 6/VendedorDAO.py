import mysql.connector  # type: ignore
from Vendedor import Vendedor

#Arquivo onde instancia o Banco de Dados e opera os metodos

#Configuracao da conexao do MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db_vendas"
)

#Criando um cursor para se comunicar com o banco de dados
cursor = conexao.cursor()


#CREATE - Cria um vendedor e usa uma tupla para verificar se o cpf ja existe
def insertVendedorDB(vendedor):
    verifica = 'SELECT * FROM tb_vendedores WHERE cpf = %s'
    valor_verifica = (vendedor.cpf,)
    cursor.execute(verifica, valor_verifica)
    if cursor.fetchone():
        print("CPF ja cadastrado!")
        print()  #quebra de linha
    else:
        comando = 'INSERT INTO tb_vendedores(nome, cpf, data_nascimento, email, estado) VALUES(%s, %s, %s, %s, %s)'
        valores = (vendedor.nome, vendedor.cpf, vendedor.datansc, vendedor.email, vendedor.estado)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Vendedor cadastrado com sucesso")
        print()  #quebra de linha


# READ - Imprime um vendedor pelo seu CPF
def selectVendedorDB(cpf):
    comando = 'SELECT * FROM tb_vendedores WHERE CPF = %s'
    cursor.execute(comando, (cpf,))
    resultado = cursor.fetchone()

    if resultado:
        return Vendedor(
            nome=resultado[0],
            cpf=resultado[1],
            datansc=resultado[2],
            email=resultado[3],
            estado=resultado[4]
        )
        #A quebra de linha ao mostrar um vendedor fica no metodo __str__() na classe Vendedor
    else:
        return "CPF nao encontrado \n"


#UPDATE - Atualiza um vendedor pelo cpf e usa uma tupla para verificar se o cpf existe
def updateVendedorDB(vendedor, nome, cpf, datansc, email, estado):
    verifica = 'SELECT * FROM tb_vendedores WHERE cpf = %s'
    cursor.execute(verifica, (cpf,))

    if cursor.fetchone():
        comando = 'UPDATE tb_vendedores SET nome = %s, data_nascimento = %s, email = %s, estado = %s WHERE cpf = %s'
        valores = (nome, datansc, email, estado, cpf)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Vendedor atualizado com sucesso")
        vendedor.nome = nome
        vendedor.datansc = datansc
        vendedor.email = email
        vendedor.estado = estado
        print()  #quebra de linha
    else:
        print("CPF nao encontrado")
        print()  #quebra de linha


#DELETE - Deleta um vendedor pelo cpf e usa uma tupla para verificar se o cpf existe
def deleteVendedorDB(cpf):
    comando = 'DELETE FROM tb_vendedores WHERE cpf = %s'
    cursor.execute(comando, (cpf,))
    conexao.commit()
    if cursor.rowcount > 0:
        print("Vendedor deletado com sucesso")
        print()
    else:
        print("CPF não encontrado")
        print()
