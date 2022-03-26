#17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1 - comprar apenas latas de 18 litros;
# 2 - comprar apenas galões de 3,6 litros;
# 3 - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

#Entrada de Dados
metros_quadrados = float(input("Digite o tamanho "))

lata_litro = 18
valor_lata = 80.00
galao_litro = 3.6
valor_galao = 25.00
rendimento_litro = 6
folga = 1.1




#lógica apenas latas de 18 litros
lata = 6 * 18
lata_rendimento = metros_quadrados / lata
preco_lata = (math.ceil(lata_rendimento)) * 80.00

print("\nSerão necessárias {:.0f} latas de tinta".format(
    math.ceil(lata_rendimento)))
print("Preço das latas {:.2f}".format(preco_lata))


#lógica apenas galões de 3,6 litros
galao = 6 * 3.6
galao_rendimento = metros_quadrados / galao
preco_galao = (math.ceil(galao_rendimento)) * 25.00

print("\nSerão necessários {:.0f} galões de tinta".format(
    math.ceil(galao_rendimento)))
print("Preço dos galões {:.2f}".format(preco_galao))



#lógica de menor disperdício de tinta

total_tinta = metros_quadrados / rendimento_litro
print(total_tinta)


