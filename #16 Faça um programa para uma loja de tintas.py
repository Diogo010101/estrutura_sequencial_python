#16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metro_quadrado = float(input("Digite o tamanho do local de pintura em metros quadrados: "))
latas = metro_quadrado / (18 * 3)
valor_lata = latas * 80.00

print("Você precisa de {:.2f} latas de tinta para pintar um local com {:.2f}m²\nO valor gasto será de {:.2f}".format(latas, metro_quadrado, valor_lata))


