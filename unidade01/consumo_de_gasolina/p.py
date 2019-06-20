pos_inicial     = float(raw_input())
litros_inicial  = float(raw_input())
pos_final       = float(raw_input())
litros_final    = float(raw_input())

dist = pos_final - pos_inicial
delta_consumo = litros_inicial - litros_final

print '%.1f' % (dist / delta_consumo)