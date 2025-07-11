import requests
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recetas')
def recetas():
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=Mexican'
    response = requests.get(url)
    data = response.json()

    recetas = []
    for item in data['meals']:
        receta = {
            'id': item['idMeal'],
            'nombre': item['strMeal'],
            'imagen_url': item['strMealThumb']
        }
        recetas.append(receta)

    return render_template('recetas.html', recetas=recetas)


@bp.route('/recetas/<int:receta_id>')
def receta_detalle(receta_id):
    return render_template('receta_detalle.html', receta_id=receta_id)

@bp.route('/mapa')
def mapa():
    return render_template('mapa.html')

@bp.route('/eventos')
def eventos():
    return render_template('eventos.html')