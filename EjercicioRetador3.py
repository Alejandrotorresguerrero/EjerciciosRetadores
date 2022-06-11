pesoCementoKg= 40
pesoYesoKg = 30
pesoMaximo = 3254
pesoMinimo = float(pesoMaximo) * .50

costalCemento = input('Número de costales de cemento(kg): ')
costalYeso = input('Número de costales de yeso(kg): ')

KgCemento = int(costalCemento) * int(pesoCementoKg)
KgYeso = int(costalYeso) * int(pesoYesoKg)
KgTotal = KgCemento + KgYeso
decision = KgTotal<=pesoMaximo and KgTotal>pesoMinimo
print('El peso total del envio es:', KgTotal, 'kg')
print('¿Puede enviarse el pedido?:', decision)