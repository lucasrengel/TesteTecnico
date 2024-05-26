import pandas as pd #type: ignore

dados = [
    ['Lucas', 0, '2005-12-04', 'lucaslangel@hotmail.com', 'SC'],
    ['Sarah', 11077728943, '2004-10-08', 'sarah@gmail.com', 'SC'],
    ['João Silva', 12345678901, '1980-12-12', 'joaosilva@email.com', 'SP'],
    ['Maria Souza', 98765432109, '1980-12-12', 'mariasouza@email.com', 'RJ'],
    ['Pedro Oliveira', 12312451242, '2000-03-30', 'pedrooliveira@email.com', 'MG'],
    ['Lucas Rengel', 7037982944, '2005-12-04', 'lucaslangel@hotmail.com', 'SC']
]

criar_planilha = pd.DataFrame(dados, columns=['Nome', 'CPF', 'Data_Nascimento', 'Email', 'Estado'])
criar_planilha.to_excel('Caso 1 e 2/DadosVendedores.xlsx', index=False)
print("Planilha criada com sucesso!")