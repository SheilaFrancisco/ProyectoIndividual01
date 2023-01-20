# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<hr>  
<br/>
Este repositorio forma parte de los requerimientos solicitados durante la cursada del bootcamp de Data Science de Henry.
<br/>
<br/>
<hr>
<br/>
Para la aprobación del primer proyecto individual se dio la siguiente consigna:

<br/>

<p align="center">
<br/>
        "Como parte del equipo de data de una empresa, el área de análisis de datos le solicita al área de Data Engineering (usted) ciertos requerimientos para el óptimo desarrollo de sus actividades. Usted deberá elaborar las transformaciones requeridas y disponibilizar los datos mediante la elaboración y ejecución de una API".
</p>
<br/>
Se proporcionaron 4 archivos CSV con datos sobre 4 plataformas de streaming: Amazon, Disney, Hulu y Netflix. El código utilizado para realizar las transformaciones solicitadas en la consigna se puede observar en el archivo Transformaciones.ipynb
<br/>
<br/>
Una vez realizadas las transformaciones se procedió a elaborar una API utilizando el framework FastAPI y, finalmente, para el deployment de la API se utilizó [Deta](https://www.deta.sh/?ref=fastapi) 
<br/>
<br/>
Para el funcionamiento de la API se solicitó definir cinco funciones para consulta de los datos. A continuación se muestran las consultas solicitadas acompañadas de la forma para accedera ellas en el navegador:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
        + https://yvpv8c.deta.dev//get_word_count/{plataforma}/{keyword}

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating

<br/>

<br/>

## **Fuente de datos**

+ Los archivos proporcionados con los datos de las plataformas de streaming se encuentran en la carpeta Datasets, en este mismo repositorio.
+ En el archivo main.py se encuentra cada una de las funciones desarrolladas para las consultas a la API.
+ En requirements.txt se ubican las librerías necesarias para el correcto funcionamiento de la API en Deta.
