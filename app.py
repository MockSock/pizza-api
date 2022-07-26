from flask import Flask, jsonify, redirect, request, url_for
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
def get_pizza_orders():
    entries = PizzaOrder.query.all()
    result = PizzaOrderSChema.dump(entries)
    return jsonify(result)

@app.route('/orders', methods='POST')
def post_pizza_order():
    req = request.get_json()
    orderId = req['orderId']
    size = req['size']
    crust = req['crust']
    topping = req['topping']
    new_entry = PizzaOrder(orderId=orderId, size=size, crust=crust, topping=topping)

    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('/orders'))

if __name__ == "__main__":
    db.create_all()
    app.run()