# Criar uma lista de alunos
lista_de_alunos = ['Paulo', 'Maria', 'João', 'Ana', 'Carlos']

# 1. Adicionar novos alunos que estão fazendo essa aula.
lista_de_alunos.append('Lucas')
lista_de_alunos.append('Sofia')

# 2. Um dos alunos desistiu da aula, agora você precisa remover ele da lista.
lista_de_alunos.remove('Carlos')

# 3. Imprimir a lista de alunos atualizada.
print(lista_de_alunos)

# 4. Por fim, use o conceito de dicionário para que você possa pesquisar
# um aluno em específico nessa lista

# Criar um dicionário para armazenar os alunos
dicionario_de_alunos = {
    'Paulo': {'idade': 20, 'curso': 'Engenharia'},
    'Maria': {'idade': 22, 'curso': 'Medicina'},
    'João': {'idade': 19, 'curso': 'Direito'},
    'Ana': {'idade': 21, 'curso': 'Arquitetura'},
    'Lucas': {'idade': 23, 'curso': 'Computação'},
    'Sofia': {'idade': 20, 'curso': 'Design'}
}

# Função para pesquisar um aluno no dicionário
def pesquisar_aluno(nome):
    if nome in dicionario_de_alunos:
        return dicionario_de_alunos[nome]
    else:
        return "Aluno não encontrado."
    
# Exemplo de pesquisa
aluno_pesquisado = 'Maria'
resultado = pesquisar_aluno(aluno_pesquisado)
print(f"Informações do aluno {aluno_pesquisado}: {resultado}")
