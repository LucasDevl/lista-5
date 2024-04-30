def tabuada(numero):
    print("Tabuada do", numero)
    for i in range(1, 11):
        resultado = numero * i
        print("{} x {} = {}".format(numero, i, resultado))

tabuada(7)
