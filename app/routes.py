import requests
from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recetas')
def recetas():
    query = request.args.get('q')
    recetas = []

    if query:
        url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={query}'
    else:
        url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=Mexican'  # Recetas aleatorias por defecto

    response = requests.get(url)
    data = response.json()

    if data['meals']:
        for item in data['meals']:
            receta = {
                'id': item['idMeal'],
                'nombre': item['strMeal'],
                'imagen_url': item['strMealThumb']
            }
            recetas.append(receta)

    return render_template('recetas.html', recetas=recetas)



@bp.route('/recetas/<int:receta_id>')
@bp.route('/recetas/<int:id>')
def ver_receta(id):
    url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}'
    response = requests.get(url)
    data = response.json()

    if not data['meals']:
        return render_template('404.html'), 404

    meal = data['meals'][0]

    # Extraer ingredientes y medidas
    ingredientes = []
    for i in range(1, 21):
        ingrediente = meal.get(f'strIngredient{i}')
        medida = meal.get(f'strMeasure{i}')
        if ingrediente and ingrediente.strip():
            ingredientes.append(f"{medida.strip()} {ingrediente.strip()}")

    receta = {
        'nombre': meal['strMeal'],
        'imagen_url': meal['strMealThumb'],
        'ingredientes': ingredientes,
        'instrucciones': meal['strInstructions'],
        'fuente': meal.get('strSource') or f"https://www.themealdb.com/meal/{id}"
    }

    return render_template('receta_detalle.html', receta=receta)

@bp.route('/mapa')
def mapa():
    # Ejemplo de lugares (puedes sacar esto de una base de datos o archivo JSON más adelante)
    lugares = [
        {
            'nombre': 'Cocina Tradicional Doña Mary',
            'lat': 16.9037,
            'lng': -92.0945,
            'descripcion': 'Especialidades como tamales de chipilín y caldo de res.'
        },
        {
            'nombre': 'Mercado Municipal de Ocosingo',
            'lat': 16.9055,
            'lng': -92.0930,
            'descripcion': 'Puestos con antojitos típicos chiapanecos y productos locales.'
        },
        {
            'nombre': 'Restaurante El Buen Sazón',
            'lat': 16.9043,
            'lng': -92.0962,
            'descripcion': 'Comida casera chiapaneca, tortillas hechas a mano y bebidas tradicionales.'
        },
        {
            'nombre': 'Festival del Maíz Ocosingo',
            'lat': 16.9021,
            'lng': -92.0950,
            'descripcion': 'Evento anual con exposición de platillos a base de maíz y música regional.'
        }
    ]
    return render_template('mapa.html', lugares=lugares)

@bp.route('/eventos')
def eventos():
    return render_template('eventos.html')