#coding: utf-8

custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissoes = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())

venda = custo * (despesas + lucro + 100) / (100 - impostos - comissoes - descontos - encargos)

print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (venda, int(venda), venda - int(venda))
