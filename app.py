from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import cross_origin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONs'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class PizzaOrder(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(500))
    crust = db.Column(db.String(500))
    topping = db.Column(db.String(500))

class PizzaOrderSChema(ma.Schema):
    class Meta:
        fields = ('orderId', 'size', 'crust', 'topping')


@app.route('/')
def hello_world():
    return 'Hello World!'

@cross_origin()
@app.route('/orders')
def getPizzaOrders():
    return 'I will get pizza orders one day'

if __name__ == "__main__":
    db.create_all()
    app.run()