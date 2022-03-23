#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
print("Peso Ideal")
altura = float(input("Digite a altura: "))
peso_ideal = (72.7 * altura) - 58

print("Para a altura de {:.2f} o peso ideal é: {:.2f} Kg".format(altura, peso_ideal))