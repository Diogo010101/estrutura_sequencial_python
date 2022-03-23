#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

print("------------------------\nConversor de Temperatura ºF para ºC\n------------------------")
fahre = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahre-32) / 9)
print("A temperatura em Celsius é: {:.2f}ºC".format(celsius))
