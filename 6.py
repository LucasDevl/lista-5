import random

def abrir_caixa():
    probabilidade = random.random() * 100
    if probabilidade <= 80:
        return "comum"
    elif probabilidade <= 99:
        return "raro"
    else:
        return "lendário"

def consultar_itens(inventario):
    print("Itens coletados:")
    print("Itens comuns:", inventario["comum"])
    print("Itens raros:", inventario["raro"])
    print("Itens lendários:", inventario["lendário"])

def main():
    inventario = {"comum": 0, "raro": 0, "lendário": 0}

    while True:
        print("1 – Abrir uma caixa")
        print("2 – Consultar itens")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao == '1':
            item_obtido = abrir_caixa()
            print("Você coletou 1 item", item_obtido + "!")
            inventario[item_obtido] += 1
        elif opcao == '2':
            consultar_itens(inventario)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
