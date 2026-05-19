# # Função

# def pure_increments(elements, index):
#     new_elements = elements.copy()
#     new_elements[index] += 1
#     return new_elements

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(pure_increments(lista, 0))
# print(pure_increments(lista, 1))
# print(pure_increments(lista, 2))
# print(pure_increments(lista, 3))
# print(pure_increments(lista, 4))
# print(pure_increments(lista, 5))


# # Explicação: A função pure_increments recebe uma lista de elementos
# # e um índice. Ela cria uma cópia da lista original, incrementa o valor
# # no índice especificado e retorna a nova lista. Isso permite que a 
# # função seja pura, pois não modifica a lista original e sempre retorna
# # o mesmo resultado para os mesmos argumentos.


#==============================================================#


# def dividir(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Erro: Divisão por zero não é permitida."
#     finally:
#         print("Função executada.")

# print(dividir(4, 2))
# # print(dividir(4, 0))


#==============================================================#


"""
1. Crie um trecho de código usando try, except e finally
2. Dentro da instrução try, coloque um trecho de código que efetue uma
operação matemática de divisão entre duas variáveis.
3. Defina a mensagem de erro e de sucesso que você deseja exibir e 
insira ela nos respectivos comandos de cada uma, conforme você aprendeu
nessa aula.
4. Agora teste ir trocando os valores das variáveis até provocar algum
erro. Um exemplo, você pode provocar uma divisão zero, que nem como
fizemos nessa aula.
"""

def dividir(a, b):
    try:
        resultado = a / b
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    finally:
        print("Função de divisão executada.")

# Testando a função com diferentes valores
dividir(10, 2)  # Deve imprimir o resultado da divisão

print("$=======================================================$")

dividir(10, 0)  # Deve imprimir a mensagem de erro
