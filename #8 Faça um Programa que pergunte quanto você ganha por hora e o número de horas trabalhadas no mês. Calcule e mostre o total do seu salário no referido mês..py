#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalha por mês? "))
salario_mes = horas_mes * salario_hora
print("Seu sálario depois de um mês de trabalho será: {:.2f}".format(salario_mes))