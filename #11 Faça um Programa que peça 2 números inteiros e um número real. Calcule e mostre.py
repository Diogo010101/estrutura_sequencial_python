#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1: o produto do dobro do primeiro com metade do segundo .
# 2: a soma do triplo do primeiro com o terceiro.
# 3: o terceiro elevado ao cubo.


numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

primeiro = (numero_1 * 2) * (numero_2 / 2)
segundo = (3 * numero_1) + (real)
terceiro = real ** 3

print("\nO produto do dobro do primeiro com metade do segundo é: {:.2f}\n".format(primeiro))
print("soma do triplo do primeiro com o terceiro é: {:.2f}\n".format(segundo))
print("O terceiro elevado ao cubo é: {:.2f}\n".format(terceiro))


