import random

def sorteio(inicio, fim):
    numero_sorteado = random.randint(inicio, fim)
    return numero_sorteado

# Exemplo de uso da função sorteio
inicio_intervalo = 1
fim_intervalo = 100
numero_sorteado = sorteio(inicio_intervalo, fim_intervalo)
print("O número sorteado é:", numero_sorteado)
