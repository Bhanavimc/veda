from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/store_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define database models
class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

# Define a route for the homepage
@app.route('/')
def homepage():
    return jsonify({"message": "Welcome to the Microlearning Platform API!"})

# Define API endpoints
@app.route('/api/add', methods=['POST'])
def add_entry():
    try:
        data = request.json
        name = data.get('name')

        if not name:
            return jsonify({"error": "Name field is required"}), 400

        new_entry = ExampleModel(name=name)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"message": "Entry added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/list', methods=['GET'])
def list_entries():
    try:
        entries = ExampleModel.query.all()
        result = [{"id": entry.id, "name": entry.name} for entry in entries]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main block
if __name__ == "__main__":
    # Create tables within the application context
    with app.app_context():
        db.create_all()

    # Start the Flask app
    app.run(debug=True)
