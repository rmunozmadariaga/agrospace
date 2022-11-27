import geopandas as gpd
import rasterio
from rasterio.plot import show
import rasterstats
import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce

# Carga de elemento shape geojson
potreros_shape = gpd.read_file('shape/agrospace_piloto.geojson')

# Carga de raster especifico agrospace_piloto_2019-10-21
potreros_raster = rasterio.open('rasterv2/agrospace_piloto_2019-10-21.tif', mode='r')

#Funcion general de calculo de stats
def get_stats(shape, raster, affine, stat):
    stats = []
    i = 0
    # Calculo de estadisticas zonales
    zonal_stats = rasterstats.zonal_stats(shape,
                                          raster,
                                          affine=affine,
                                          stats=[stat],
                                          geojson_out=True)

    # Extraccion de data de zonal_stats para manejo de propiedades
    while i < len(zonal_stats):
        stats.append(zonal_stats[i]['properties'])
        i = i + 1

    return stats

# Grafico de potreros_raster y potreros_shape juntos y se delimita espacio para estadisticas
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (8,8))

show(potreros_raster, ax=ax1, title='Divisiones Predio')
potreros_shape.plot(ax=ax1, facecolor='None', edgecolor='red')

# Se asigna los valores de potreros_raster a un array
ndvi_array = potreros_raster.read(1)

#Se define affine
affine = potreros_raster.transform

#Se calculan stats con la funcion get_stats previamente construido
avg_ndvi = get_stats(potreros_shape, ndvi_array, affine, 'mean')
max_ndvi = get_stats(potreros_shape, ndvi_array, affine, 'max')
min_ndvi = get_stats(potreros_shape, ndvi_array, affine, 'min')
median_ndvi = get_stats(potreros_shape, ndvi_array, affine, 'median')

# Se transfiere informacion a pandas DataFrames
avg_potreros = pd.DataFrame(avg_ndvi)
max_potreros = pd.DataFrame(max_ndvi)
min_potreros = pd.DataFrame(min_ndvi)
median_potreros = pd.DataFrame(median_ndvi)

#Se grafican Dataframes generados
avg_potreros.plot(ax=ax2, x='Name', y='mean', kind='line', color='blue', title='Estadisticas por Potrero')
median_potreros.plot(ax=ax2, x='Name', y='median', kind='line', color='black')
max_potreros.plot(ax=ax2, x='Name', y='max', kind='bar', color='green')
min_potreros.plot(ax=ax2, x='Name', y='min', kind='bar', color='red')
plt.show()

#Se reducen Dataframes para obtencion de estadisticas Generales
dataframes_stats = [avg_potreros, max_potreros, median_potreros, min_potreros]
dataframe_final = reduce(lambda left, right: pd.merge(left, right, on='Name'), dataframes_stats)

print('Estadisticas por Potrero')
print(dataframe_final[['Name', 'mean', 'median', "max", "min"]])

print('Top 10 Potreros mas productivos')
print(max_potreros.sort_values('max')['Name'].head(10))












