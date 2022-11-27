# intern-test-raul-munoz

## Muestreo de estadisticas 

En este desorrollo se busca cumplir con varios puntos mencionados en 
[intern-test](https://github.com/Tartomas/intern-test) 
de [AgroSpace](https://agrospace.cl/).

En particular se hace un grafico de una zona especifica con sus divisiones particulares junto un grafico con estadisticas generales. 
En este caso se utiliza el archivo raster `agrospace_piloto_2019-10-21.tif` y el archivo shape
`agrospace_piloto.geojson` obteniendo la siguiente figura:

![](/img/grafico.png)

A su vez tambien se genera una lista general en detalle con los datos mostrados en el grafico y se anexa informacion de los potreros con mejor rendimiento en base al raster cargado:

![](/img/estadisticas generales y top.png)

Este codigo puede obtener estadisticas de cualquier raster disponible en el directorio `rasterv2` el cual debe ser indicado en el codigo fuente.

### Herramientas utilizadas
 - Lenguaje: Python 3.6 
 - Paquetes utilizados: 
    - [rasterio](https://rasterio.readthedocs.io/en/latest/) 
    - [rasterstas](https://pythonhosted.org/rasterstats/) 
    - [pandas](https://pandas.pydata.org/) 
    - [matplotlib](https://matplotlib.org/) 



