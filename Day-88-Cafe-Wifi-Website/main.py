from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record


@app.route("/random", methods=['GET'])
def get_random_cafe():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafes = results.scalars()
    cafe = choice(all_cafes.all())
    return jsonify({
                'cafe' : {
                    'id': cafe.id,
                    'name': cafe.name,
                    'can_take_calls': cafe.can_take_calls,
                    'map_url': cafe.map_url,
                    'img_url': cafe.img_url,
                    'location': cafe.location,
                    'seats': cafe.seats,
                    'has_toilet': cafe.has_toilet,
                    'has_wifi': cafe.has_wifi,
                    'has_sockets': cafe.has_sockets,
                    'coffee_price': cafe.coffee_price
                        }
                    }
                )
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    # return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=['GET'])
def random_cafe():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.id))
    all_cafes = results.scalars().all()
    data = {
        'all_cafe_list': [cafe.to_dict() for cafe in all_cafes]
    }
    return jsonify(data)


@app.route("/search", methods=['GET'])
def search_cafe():
    query_location = request.args.get("loc")
    results = db.session.execute(db.select(Cafe).where(Cafe.location==query_location))
    result_cafes = results.scalars().all()
    if len(result_cafes) == 0:
        return jsonify({"error":{
             "Not Found": f"Sorry, we don't have a cafe at that {query_location}."
                                }
                        }
        )
    else:
        data = {
        'all_cafe_list': [cafe.to_dict() for cafe in result_cafes]
                }
        return jsonify(data)
    

## HTTP POST - Create Record


@app.route("/add", methods=['POST'])
def add_cafe():
    add_one_cafe = Cafe(
        # name=request.form.get("name"),
        # can_take_calls=bool(request.form.get("can_take_calls")),
        # map_url=request.form.get("map_url"),
        # img_url=request.form.get("img_url"),
        # location=request.form.get("location"),
        # seats=request.form.get("seats"),
        # has_toilet=bool(request.form.get("has_toilet")),
        # has_wifi=bool(request.form.get("has_wifi")),
        # has_sockets=bool(request.form.get("has_sockets")),
        # coffee_price=request.form.get("coffee_price"),
        name=request.json["name"],
        can_take_calls=bool(request.json["can_take_calls"]),
        map_url=request.json["map_url"],
        img_url=request.json["img_url"],
        location=request.json["location"],
        seats=request.json["seats"],
        has_toilet=bool(request.json["has_toilet"]),
        has_wifi=bool(request.json["has_wifi"]),
        has_sockets=bool(request.json["has_sockets"]),
        coffee_price=request.json["coffee_price"]

    )
    db.session.add(add_one_cafe)
    db.session.commit()
    result = db.session.execute(db.select(Cafe).where(Cafe.name==request.json["name"]))
    result_cafe = result.scalar()
    data = {'result':"data added failed."}
    if result_cafe:
        data['result'] = "data added successfully."
    return data


## HTTP PUT/PATCH - Update Record


@app.route("/update_price/<cafe_id>", methods=['PATCH'])
def update_price_cafe(cafe_id):
    cafe_to_update_price = db.session.execute(db.select(Cafe).where(Cafe.id == int(cafe_id))).scalar()
    if cafe_to_update_price:
        cafe_to_update_price.coffee_price = request.json["new_price"]
        db.session.commit()
        return jsonify(response={"success": f"Successfully added the new price in {cafe_id}."})
    else:
        return jsonify({"error":{
             "Not Found": f"Sorry, we don't have a cafe in that {cafe_id}."
                                }
                        }
        )
 

## HTTP DELETE - Delete Record   


@app.route("/delete", methods=['DELETE'])
def remove_cafe():
    cafe_id = request.json['id']
    cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == int(cafe_id))).scalar()
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": f"Successfully deleted the new price in {cafe_id}."})
    else:
        return jsonify({"error":{
             "Not Found": f"Sorry, we don't have a cafe in that {cafe_id}."
                                }
                        }
        )


if __name__ == '__main__':
    app.run(debug=True)
