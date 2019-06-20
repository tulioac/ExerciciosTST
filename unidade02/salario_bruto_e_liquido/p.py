#coding: utf-8

nome = raw_input()
horas_extras = float(raw_input())
salario_min = float(raw_input())
preco_extra = float(raw_input())

salario_extra = horas_extras * preco_extra
salario_bruto = 4 * salario_min + salario_extra

desconto_inss = salario_bruto * 0.12
desconto_renda = salario_bruto * 0.2

salario_liquido = salario_bruto - (desconto_inss + desconto_renda)

print "O Salário Bruto de Antonio é de R$ %.2f" % salario_bruto
print "O Salário Líquido de Antonio é de R$ %.2f" % salario_liquido

