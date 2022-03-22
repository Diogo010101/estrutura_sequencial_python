#4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("---------------------------\nEscola de Artes Mãos Leves\n---------------------------")


nota_bimestre_01 = float(input("Digite a nota do primeiro bimestre: "))
nota_bimestre_02 = float(input("Digite a nota do segundo bimestre: "))
nota_bimestre_03 = float(input("Digite a nota do terceiro bimestre: "))
nota_bimestre_04 = float(input("Digite a nota do quarto bimestre: "))

media = (nota_bimestre_01 + nota_bimestre_02 + nota_bimestre_03 + nota_bimestre_04) / 4

print("A média anual é: {:.2f}".format(media))