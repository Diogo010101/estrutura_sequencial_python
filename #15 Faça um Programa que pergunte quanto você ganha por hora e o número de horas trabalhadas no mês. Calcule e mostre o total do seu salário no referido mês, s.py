#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


salario_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalha por mês? "))
salario_bruto = horas_mes * salario_hora
imposto_de_renda = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
descontos = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - descontos
print("\nSeu sálario Bruto é: {:.2f}".format(salario_bruto))
print("\nDesconto de 11% do Imposto de Renda: {:.2f}".format(imposto_de_renda))
print("\nDesconto de 8% INSS: {:.2f}".format(inss))
print("\nDesconto de 5% Sindicato: {:.2f}".format(sindicato))
print("\nSalário liquido: {:.2f}".format(salario_liquido))