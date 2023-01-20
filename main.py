from fastapi import FastAPI
import pandas as pd
from pandasql import sqldf

df_plataformas = pd.read_csv('Plataformas_Unificado.csv')

app=FastAPI()

@app.get('/')
def root():
    return "PI01 Sheila Francisco"

@app.get('/get_word_count/{plataforma}/{keyword}')
def get_word_count(plataforma:str, keyword:str):
    '''
    Esta función recibe como parámetros la plataforma requerida y la palabra a buscar. 
    Devuelve como resultado la cantidad de veces que se repite esa palabra en los títulos 
    de las películas y series que están disponibles en esa plataforma.
    '''
    if plataforma == "amazon":
        inicial = "a%"
    elif plataforma == 'netflix':
        inicial = 'n%'
    elif plataforma == "hulu":
        inicial = "h%"
    elif plataforma == 'disney':
        inicial = 'd%'
    else:
        return 'plataforma inválida'
    
    querie = f'select count(*) as cantidad from df_plataformas where id like "{inicial}" and title like "%{keyword}%"'

    return (plataforma, sqldf(querie).to_string(index=False, header=False))

@app.get('/get_score_count/{plataforma}/{puntaje}/{anio}')
def get_score_count(plataforma, puntaje, anio):
    '''
    Esta función recibe como parámetros la plataforma requerida, el puntaje y el año a buscar.
    Devuelve como resultado la cantidad de PELICULAS con puntaje mayor al indicado, que están disponibles en esa plataforma
    y se estrenaron en el año indicado.
    '''
    if plataforma == "amazon":
        inicial = "a%"
    elif plataforma == 'netflix':
        inicial = 'n%'
    elif plataforma == "hulu":
        inicial = "h%"
    elif plataforma == 'disney':
        inicial = 'd%'
    else:
        return 'plataforma inválida'

    querie = f'select count(*) from df_plataformas where id like "{inicial}" and type == "movie" and score > {puntaje} and release_year == {anio}'

    return plataforma, sqldf (querie).to_string(index=False, header=False)

@app.get('/get_second_score/{plataforma}')
def get_second_score(plataforma):
    '''
    Esta función recibe como parámetro la plataforma requerida.
    Devuelve como resultado la segunda PELICULA con mayor puntaje, disponible en la plataforma indicada. En caso de haber dos 
    películas con el mismo puntaje hace la discriminación por orden alfabético para retornar un solo resultado.
    '''
    if plataforma == "amazon":
        inicial = "a%"
    elif plataforma == 'netflix':
        inicial = 'n%'
    elif plataforma == "hulu":
        inicial = "h%"
    elif plataforma == 'disney':
        inicial = 'd%'
    else:
        return 'plataforma inválida'

    querie = f'select title, score from df_plataformas where id like "{inicial}" and type == "movie" order by score desc, title limit 1 offset 1'
    
    return sqldf (querie).to_string(index=False, header=False)

@app.get('/get_longest/{plataforma}/{tipo}/{anio}')
def get_longest(plataforma, tipo, anio):
    '''
    Esta función recibe como parámetros la plataforma requerida, el tipo de duración y el año de lanzamiento.
    Devuelve como resultado la PELICULA con mayor duración en el año indicado, disponible en esa plataforma.
    '''
    if plataforma == "amazon":
        inicial = "a%"
    elif plataforma == 'netflix':
        inicial = 'n%'
    elif plataforma == "hulu":
        inicial = "h%"
    elif plataforma == 'disney':
        inicial = 'd%'
    else:
        return 'plataforma inválida'

    querie = f'select title, duration from df_plataformas where id like "{inicial}" and type == "movie" and release_year == {anio} order by duration_int desc limit 1'
    
    return sqldf (querie).to_string(index=False, header=False)

@app.get('/get_rating_count/{rating}')
def get_rating_count(rating):
    '''
    Esta función recibe como parámetro el rating.
    Devuelve como resultado la cantidad de series y películas que están clasificadas con ése rating en toda la base de datos,
    es decir, no discrimina por plataforma.
    '''
    querie = f'select rating, count(*) as cantidad from df_plataformas where rating == "{rating}"'
    
    return sqldf (querie).to_string(index=False, header=False)