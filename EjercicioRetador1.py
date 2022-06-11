poblacion_mujeres = 1532128
poblacion_hombres = 1494815
superficie_sinaloa_km2 = 57365
temperaturaMediaAnualCentigrados = 25.45
mmPrecipitacionMediaAnual = 790.1 
culiacan_porcentajeHab = 33.15
mazatlan_porcentajeHab = 16.57
clima=['Cálido','Seco','Semiseco','Subhúmedo']

poblacion_total = int(poblacion_mujeres) + int(poblacion_hombres)
porcentajeMazCul_total = float(culiacan_porcentajeHab) + float(mazatlan_porcentajeHab)

print('La poblacion entre hombres y mujeres es:', poblacion_total, 'habitantes')
print('El porcentaje de habitantes entre Mazatlán y Culiacán es:', porcentajeMazCul_total, '% habitantes')
print('La temperatura media anual es:', temperaturaMediaAnualCentigrados, '°C')
print('Tipos de clima: ', clima)