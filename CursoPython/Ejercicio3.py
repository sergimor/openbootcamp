peso = input('Escribe tu peso en Kg: ')
altura = input('Escribe tu altura en metros: ')
mc = int(peso) / int(altura) ** 2
print('Tu índice de masa corporal es ', round(mc, 2))