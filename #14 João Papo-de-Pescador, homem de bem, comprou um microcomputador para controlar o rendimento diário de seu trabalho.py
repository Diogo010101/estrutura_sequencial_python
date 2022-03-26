# 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print("-------------------------------\n        Peso de Peixes\n-------------------------------\n")
peso = float(input("Digita o total de kg dos peixes: "))
excesso = peso - 50.0
multa = 4.00 * excesso

print("\n O peso total de peixes foi de: {:.2f} Kg\n".format(peso))
print("O excesso de peso foi de {:.2f} Kg\n".format(excesso))
print("O valor total da multa ficou em R$ {:.2f}".format(multa))
