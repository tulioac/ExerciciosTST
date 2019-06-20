total = int(raw_input())
teresa = int(raw_input())
carla = int(raw_input())
joaquim = total - (teresa + carla)

percent_teresa = 100.0 * teresa / total
percent_joaquim = 100.0 * joaquim / total
percent_carla = 100.0 * carla / total

print "Teresa vendeu %d (de %d) brinquedos. (%.2f%%)" % (teresa, total, percent_teresa)
print "Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)" % (joaquim, total, percent_joaquim)
print "Carla vendeu %d (de %d) brinquedos. (%.2f%%)" % (carla, total, percent_carla)


