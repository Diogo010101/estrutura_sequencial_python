#13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a - Para homens: (72.7*h) - 58
# b - Para mulheres: (62.1*h) - 44.7

print("Peso Ideal")
altura = float(input("Digite a altura: "))
peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7

print("Peso ideal para um Homem com a altura de {:.2f}m é de {:.2f} Kg".format(altura, peso_ideal_homem))
print("Peso ideal para uma Mulher com a altura de {:.2f}m é de {:.2f} Kg".format(altura, peso_ideal_mulher))
