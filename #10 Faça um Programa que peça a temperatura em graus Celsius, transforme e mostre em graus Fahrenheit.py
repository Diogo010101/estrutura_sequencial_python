#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
print("------------------------\nConversor de Temperatura ºF para \n------------------------")
celsius = float(input("Digite a temperatura em Celsius: "))
fahre = (celsius * 1.8) + 32
print("A temperatura em Fahrenheit é: {:.2f}ºC".format(fahre))
