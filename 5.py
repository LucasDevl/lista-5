def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Erro: Divisão por zero.")
        return None

def menu():
    print("Calculadora Simples")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '5':
            print("Saindo...")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = somar(num1, num2)
            print("Resultado da soma:", resultado)
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            print("Resultado da subtração:", resultado)
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            print("Resultado da multiplicação:", resultado)
        elif escolha == '4':
            resultado = dividir(num1, num2)
            if resultado is not None:
                print("Resultado da divisão:", resultado)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
