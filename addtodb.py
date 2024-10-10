from app import app
from models import db, Pizza

pizzas = [
    {
        "name": "Margarita",
        "image": "/static/images/margarita.png",
        "price": 12.50,
        "description": "Margarita pizza is a pizza originating from the Italian city of Naples, Italy. It is a thick, rectangular pizza with a crispy crust and a soft, chewy interior. The pizza is topped with tomato sauce, onions, olives, and cheese, and is traditionally baked in a wood-fired oven.",
    },
    {
        "name": "Sicilian",
        "image": "/static/images/sicilian.png",
        "price": 15.50,
        "description": "Sicilian pizza is a pizza originating from the Italian city of Naples, Italy. It is a thick, rectangular pizza with a crispy crust and a soft, chewy interior. The pizza is topped with tomato sauce, onions, olives, and cheese, and is traditionally baked in a wood-fired oven.",
    },
    {
        "name": "Diablo",
        "image": "/static/images/diablo.png",
        "price": 14.50,
        "description": "Diablo pizza is a pizza originating from the Spanish city of Seville, Spain. It is a thick, rectangular pizza with a crispy crust and a soft, chewy interior. The pizza is topped with tomato sauce, onions, olives, and cheese, and is traditionally baked in a wood-fired oven.",
    },
    {
        "name": "Four cheese",
        "image": "/static/images/four-cheese.png",
        "price": 16.50,
        "description": "Four cheese pizza is a pizza originating from the Italian city of Naples, Italy. It is a thick, rectangular pizza with a crispy crust and a soft, chewy interior. The pizza is topped with tomato sauce, onions, olives, and cheese, and is traditionally baked in a wood-fired oven.",
    },
    {
        "name": "Capricciosa",
        "image": "/static/images/capricciosa.png",
        "price": 15.50,
        "description": "Capricciosa pizza is a pizza originating from the Italian city of Naples, Italy. It is a thick, rectangular pizza with a crispy crust and a soft, chewy interior. The pizza is topped with tomato sauce, onions, olives, and cheese, and is traditionally baked in a wood-fired oven.",
    },
    {
        "name": "Hawaiian",
        "image": "/static/images/hawaiian.png",
        "price": 13.50,
        "description": "Hawaiian pizza is a pizza originating from the Hawaiian Islands. It is a thick, rectangular pizza with a crispy crust and a soft, chewy interior. The pizza is topped with tomato sauce, onions, olives, and cheese, and is traditionally baked in a wood-fired oven.",
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for pizza_data in pizzas:
        pizza = Pizza(
            name=pizza_data["name"],
            image=pizza_data["image"],
            price=pizza_data["price"],
            description=pizza_data["description"],
        )
        db.session.add(pizza)
    db.session.commit()
