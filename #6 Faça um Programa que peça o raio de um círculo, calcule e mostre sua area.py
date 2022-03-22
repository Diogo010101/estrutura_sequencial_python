#6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print("Esse programa calcula a área de um circulo")

raio = float(input("Digite o raio do circulo: "))
area = (raio ** 2) * 3.14

print("Um circulo com o raio de {:.2f} tem a seguinte área: {:.2f}".format(raio, area))