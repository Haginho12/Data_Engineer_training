from flask import Flask, request
from person_service import db_get_persons, db_get_person_by_id, db_create_person, db_update_person, db_delete_person 
from attribute_service import get_attributes, get_attribute_by_id, post_attributes, update_attributes, delete_attribute
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

@app.route('/person', methods=['GET'])
def get_all_person():
    try:  
        return db_get_persons()
    except:
        return {"error": "no data"}

@app.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    try:
        return db_get_person_by_id(id)
    except:
        return {"error": "no person with id %s" % id}

@app.route("/person", methods=['POST'])
def create_person():
    try: 
        data = request.get_json()
        username = data['name']
        age = data['age']
        student = data['student']
        db_create_person(username, age, student)
        return {"success": "created person: %s" % username}
    except:
        return {"error": "error creating person"}

@app.route("/person/<int:id>", methods=['PUT'])
def update_person(id):
    try:
        data = request.get_json()
        username = data['name']
        age = data['age']
        student = data['student']
        db_update_person(id, username, age, student)
        return {"success": "updated person"}
    except:
        return {"error": "error updating person"}

@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        return db_delete_person(id)
    except:
        return {"error": "no such person"}
    
@app.route('/attributes', methods=['GET'])
def get_all_attributes():
    try:  
        return get_attributes()
    except:
        return {"error": "no data"} 
    
@app.route('/attributes/<int:id>', methods=['GET'])
def get_attr_by_id(id):
    try:  
        return get_attribute_by_id(id)
    except:
        return {"error": "no person with id" % id} 

@app.route("/attributes", methods=['POST'])
def create_attribute():
    try:
        data = request.get_json()
        attribute_name = data['attribute_name']
        attribute_description = data['attribute_description']
        attribute_value = data['attribute_value']
        post_attributes(attribute_name, attribute_description, attribute_value)
        return {"success": "created attribute: %s" % attribute_name}
    except:
        return {"error": "error creating attribute"}

@app.route("/attributes/<int:id>", methods=['PUT'])
def update_attr(id):
    try:
        data = request.get_json()
        person_id = data['person_id']
        attribute_name = data['attribute_name']
        attribute_description = data['attribute_description']
        attribute_value = data['attribute_value']
        update_attributes(id, attribute_name, attribute_description, attribute_value, person_id)
        return {"success": " attribute: %s updated successfully" % attribute_name}
    except:
        return {"error": "error updating attribute"}

@app.route('/attributes/<int:id>', methods=['DELETE'])
def deleteattribute(id):
    try:
        return delete_attribute(id)
    except:
        return {"error": "no such attribute"}



if __name__ == "__main__":
    app.run()

