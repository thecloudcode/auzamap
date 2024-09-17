from flask import Flask, render_template, jsonify
import random
import time
import json

app = Flask(__name__)
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

all_coordinates = load_data('data.json')

@app.route('/')
def index():
    return render_template('index.html')

selected_coordinates = random.sample(all_coordinates, 10)
@app.route('/get_coordinates')
def get_coordinates():
    new_coordinates = random.sample(all_coordinates, 2)
    selected_coordinates.pop(0)
    selected_coordinates.pop(0)
    selected_coordinates.extend(new_coordinates)
    return jsonify(selected_coordinates)

if __name__ == '__main__':
    app.run(debug=True)
