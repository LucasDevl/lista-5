def mediaUnisinos(nota_a, nota_b):
    grau_final = nota_a * 0.33 + nota_b * 0.67
    return grau_final

nota_a = 7.5
nota_b = 8.0
resultado_final = mediaUnisinos(nota_a, nota_b)
print("O resultado do grau final é:", resultado_final)
