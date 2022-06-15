"""Flask app for Cupcakes"""

from crypt import methods
from webbrowser import get
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from forms import AddCupCake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/')
def homepage():
    form = AddCupCake()
    return render_template('home.html',form=form)
   


@app.route('/api/cupcakes', methods=['GET', 'POST'])
def list_all_cupcakes():
    if request.method == 'GET':
        cupcakes = Cupcake.query.all()
        json = [cupcake.serialize() for cupcake in cupcakes]
        return jsonify(cupcakes=json)
    
    if request.method == 'POST':
        new_cupcake = Cupcake(flavor=request.json['flavor'],
                              size=request.json['size'], rating=request.json['rating'], 
                              image=request.json['image'])
        db.session.add(new_cupcake)
        db.session.commit()
        return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:cupcake_id>')
def list_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH', 'DELETE'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    if request.method == 'PATCH':
        cupcake.flavor = request.json.get('flavor', cupcake.flavor)
        cupcake.size = request.json.get('size', cupcake.size)
        cupcake.rating = request.json.get('rating', cupcake.rating)
        cupcake.image = request.json.get('image', cupcake.image)

        db.session.commit()
        return jsonify(cupcake=cupcake.serialize())

    if request.method == 'DELETE':
        db.session.delete(cupcake)
        db.session.commit()
        return jsonify(cupcake={'deleted': cupcake_id}) 


