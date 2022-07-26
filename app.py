from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/orders')
def getPizzaOrders():
    return 'I will get pizza orders one day'

if __name__ == "__main__":
    app.run()