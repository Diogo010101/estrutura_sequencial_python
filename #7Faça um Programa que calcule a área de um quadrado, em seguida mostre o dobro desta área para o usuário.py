#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite tamanho de um dos lados do quadrado:  "))
dobro_area = (lado * lado) * 2

print("O dobro da área do quadrado é: {:.2f}".format(dobro_area))