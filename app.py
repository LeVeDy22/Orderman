from flask import Flask, render_template, request, jsonify
from config import Config
from models import db, Pizza

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/menu", methods=["GET"])
def menu_page():
    pizzas = Pizza.query.all()
    result = [
        {
            "id": pizza.id,
            "name": pizza.name,
            "image": pizza.image,
            "price": pizza.price,
            "description": pizza.description,
        }
        for pizza in pizzas
    ]
    return render_template("menu.html", pizzas=pizzas)


@app.route("/margarita")
def margarita():
    return render_template("pizzas/margarita.html")


@app.route("/sicilian")
def sicilian():
    return render_template("pizzas/sicilian.html")


@app.route("/diablo")
def diablo():
    return render_template("pizzas/diablo.html")


@app.route("/four-cheese")
def four_cheese():
    return render_template("pizzas/four-cheese.html")


@app.route("/capricciosa")
def capricciosa():
    return render_template("pizzas/capricciosa.html")


@app.route("/hawaiian")
def hawaiian():
    return render_template("pizzas/hawaiian.html")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
