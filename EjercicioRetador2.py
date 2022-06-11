municipios = []
lista_habitantes = []
cantidad = 0
n=3

while cantidad < n:
  municipio = input('Ingresa municipio: ')
  municipios.append(municipio)
  habitantes = input('Ingresa cantidad de habitantes: ')
  lista_habitantes.append(habitantes)
  
  cantidad+=1
sumatoriaHabitantes = (int(lista_habitantes[0]) + int(lista_habitantes[1]) + int(lista_habitantes[2]))
promedioHabitantes = sumatoriaHabitantes/n

print('El municipio de',municipios[0], ' tiene',lista_habitantes[0],' habitantes')
print('El municipio de',municipios[1], ' tiene',lista_habitantes[1],' habitantes')
print('El municipio de',municipios[2], ' tiene',lista_habitantes[2],' habitantes')
print('Cantidad de total de habitantes es:',sumatoriaHabitantes)
print('Promedio de habitantes por municipio es:','{:.2f}'.format(promedioHabitantes))