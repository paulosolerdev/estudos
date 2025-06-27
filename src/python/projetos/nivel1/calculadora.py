def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def calculadora():
    print("Bem-vindo à Calculadora!")

    while True:
        print("\nOperações disponíveis:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("Digite 'sair' para encerrar.")

        operacao = input("Escolha a operação (1/2/3/4 ou + - * /): ").strip()

        if operacao.lower() == 'sair':
            print("Até logo!")
            break

        if operacao not in ['1', '2', '3', '4', '+', '-', '*', '/']:
            print("Operação inválida!")
            continue

        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
        except ValueError:
            print('Entrada inválida! Por favor, insira números válidos.')
            continue

        if operacao in ['1', '+']:
            resultado = soma(num1, num2)
            simbolo = '+'
        elif operacao in ['2', '-']:
            resultado = subtracao(num1, num2)
            simbolo = '-'
        elif operacao in ['3', '*']:
            resultado = multiplicacao(num1, num2)
            simbolo = '*'
        elif operacao in ['4', '/']:
            resultado = divisao(num1, num2)
            simbolo = '/'

        print(f'Resultado: {num1} {simbolo} {num2} = {resultado}')

if __name__ == "__main__":
    calculadora()
