productos = [['Maiz Grano', 285.55],['Pepino', 334.72],['Tomate Verde', 129.00]]

cantidadProductos=len(productos)
idProducto = int(input('Ingrese Id del producto: '))

while idProducto > cantidadProductos or idProducto < 1:
  print('No existe ese producto')
  idProducto = int(input('Ingrese Id del producto: '))
  
#print(productos[idProducto-1][0])
cantidadCajas = int(input('Ingrese cantidad de cajas a comprar: '))

if idProducto == 1:
  idproducto = 1
elif idProducto == 2:
  idProducto = 2
elif idProducto == 3:
 idProducto = 3
   
producto = productos[idProducto-1][0]
costoCaja = productos[idProducto-1][1]
costoTotal = float(costoCaja) * cantidadCajas
print('\nEl producto es:', producto)
print('El precio por caja es:', costoCaja, 'pesos')
print('El total a pagar es:', '{:.2f}'.format(costoTotal),'pesos')