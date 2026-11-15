"""
Exercício Controle de Empréstimos em uma Biblioteca

Objetivo: Desenvolver um programa que auxilie Maria, uma bibliotecária,
a controlar o número de livros emprestados por um usuário durante o
mês. Para cada dia que o usuário exceder o limite estabelecido de livros
pegos, uma multa será aplicada.

Instruções:

1. O sistema de biblioteca possui um limite estabelecido de 5 livros
que cada usuário pode pegar por vez.

2. Para cada livro excedente, o usuário deve pagar uma multa de R$ 2,00.

3. O programa deve começar solicitando ao usuário o número de dias
em que ele pegou livros emprestados.

4. Em seguida, para cada um desses dias, o programa deve pedir que o
usuário informe quantos livros ele pegou emprestados.

5. O sistema deve calcular e exibir o excesso de livros e o valor da
multa para cada dia.

6. Ao final, o programa deve mostrar o total de livros excedentes e o
total da multa acumulada durante o período informado.

7. Se, ao final do mês, o usuário não tiver excedido o limite em nenhum
dia, o programa deve mostrar uma mensagem de parabenização por seguir
as regras.

Observação: O programa deve considerar que o usuário informará dados
válidos, ou seja, valores inteiros não negativos para o número de dias
e o número de livros emprestados.

"""


# Função principal do programa
def main():
    # Solicita ao usuário o número de dias em que ele pegou livros emprestados
    num_dias = int(
        input("Digite o número de dias em que você pegou livros emprestados: ")
    )

    # Inicializa variáveis para acumular o total de livros excedentes e a multa total
    total_excedente = 0
    multa_total = 0

    # Loop para cada dia informado pelo usuário
    for dia in range(1, num_dias + 1):
        # Solicita ao usuário o número de livros emprestados no dia atual
        livros_emprestados = int(
            input(f"Digite o número de livros emprestados no dia {dia}: ")
        )

        # Calcula o excesso de livros e a multa para o dia atual
        if livros_emprestados > 5:
            excedente = livros_emprestados - 5
            multa = excedente * 2.00
            print(
                f"No dia {dia}, você excedeu em {excedente} livro(s). Multa: R$ {multa:.2f}"
            )
            total_excedente += excedente
            multa_total += multa
        else:
            print(f"No dia {dia}, você não excedeu o limite de livros.")

    # Exibe o total de livros excedentes e a multa acumulada ao final do período informado
    if total_excedente > 0:
        print(f"\nTotal de livros excedentes durante o período: {total_excedente}")
        print(f"Total da multa acumulada: R$ {multa_total:.2f}")
    else:
        print("\nParabéns! Você não excedeu o limite de livros em nenhum dia.")


if __name__ == "__main__":
    main()
