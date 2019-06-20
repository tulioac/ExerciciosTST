# coding: utf-8
unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade? '))

proxima_unidade = unidade + 1

msg = '\nO aluno vai para a unidade %d com média %.1f.' % (proxima_unidade, media)

print msg
