from flask import Flask, render_template

app = Flask(__name__)

pizzas = [
    {
        'name': 'Margarita',
        'image': '/static/images/margarita.png',
        'price': 12
    },
    {
        'name': 'Sicilian',
        'image': '/static/images/sicilian.png',
        'price': 15
    },
    {
        'name': 'Diablo',
        'image': '/static/images/diablo.png',
        'price': 14
    },
    {
        'name': 'Four cheese',
        'image': '/static/images/four-cheese.png',
        'price': 16
    },
    {
        'name': 'Capricciosa',
        'image': '/static/images/capricciosa.png',
        'price': 15
    },
    {
        'name': 'Hawaiian',
        'image': '/static/images/hawaiian.png',
        'price': 15
    }
]

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html', pizzas=pizzas)

@app.route('/margarita')
def margarita():
    return render_template('pizzas/margarita.html')

@app.route('/sicilian')
def sicilian():
    return render_template('pizzas/sicilian.html')

@app.route('/diablo')
def diablo():
    return render_template('pizzas/diablo.html')

@app.route('/four-cheese')
def four_cheese():
    return render_template('pizzas/four-cheese.html')

@app.route('/capricciosa')
def capricciosa():
    return render_template('pizzas/capricciosa.html')

@app.route('/hawaiian')
def hawaiian():
    return render_template('pizzas/hawaiian.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()