# Pizza-Restaurant

This is a program  for managing restaurants and the pizzas they offer, built it uses  Flask, SQLAlchemy, and Flask-Migrate.


##  Things this program can do 

- View all restaurants
- View a single restaurant and the pizzas it serves
- View all available pizzas
- Add a pizza to a restaurant
- Delete a restaurant

## language and library used

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite

## Project Structure

pizza-api-challenge/
├── server/
│ ├── app.py # Flask app factory
│ ├── config.py # Config class
│ ├── models/
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
│ └── init.py
├── migrations/ # Flask-Migrate folder
├── seed.py # DB seed script
├── README.md
└── requirements.txt


## 📦 Installation

```bash
# 1. Clone the repo
git clone https://github.com/maxwellkiplagat/pizza-api-challenge.git
cd pizza-api-challenge

# 2. Create virtual environment
pipenv install
pipenv shell


# 3. Run migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 4. Seed the database (optional)
python seed.py

# 5. Start the server
flask run
Server will be running at http://127.0.0.1:5555

# API Endpoints
Method	Endpoint  |	Description
_________________________________
GET	/restaurants ------->        List all restaurants
GET	/restaurants/<id> ------->	    Get restaurant by ID
DELETE	/restaurants/<id> ------>	Delete a restaurant
GET	/pizzas	-------->List all pizzas
POST	/restaurant_pizzas	-------->Add pizza to a restaurant

## Example Request (POST)
Add a pizza to a restaurant:

http
Copy
Edit
POST /restaurant_pizzas
Content-Type: application/json

{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}
