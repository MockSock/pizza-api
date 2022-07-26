from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONs'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/orders')
def getPizzaOrders():
    return 'I will get pizza orders one day'

if __name__ == "__main__":
    app.run()