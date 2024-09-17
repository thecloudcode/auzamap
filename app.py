from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Full list of 20 Indian places with coordinates
all_coordinates = [
    [28.7041, 77.1025, "Delhi"],
    [19.0760, 72.8777, "Mumbai"],
    [13.0827, 80.2707, "Chennai"],
    [12.9716, 77.5946, "Bangalore"],
    [22.5726, 88.3639, "Kolkata"],
    [17.3850, 78.4867, "Hyderabad"],
    [26.8467, 80.9462, "Lucknow"],
    [21.1702, 72.8311, "Surat"],
    [23.0225, 72.5714, "Ahmedabad"],
    [9.9312, 76.2673, "Kochi"],
    [11.0168, 76.9558, "Coimbatore"],
    [15.2993, 74.1240, "Goa"],
    [18.5204, 73.8567, "Pune"],
    [24.5854, 73.7125, "Udaipur"],
    [25.3176, 82.9739, "Varanasi"],
    [30.7333, 76.7794, "Chandigarh"],
    [25.5941, 85.1376, "Patna"],
    [31.6340, 74.8723, "Amritsar"],
    [27.0238, 74.2179, "Ajmer"],
    [32.7266, 74.8570, "Jammu"]
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_coordinates')
def get_coordinates():
    # Randomly select 5 places from the list of 20 places
    selected_coordinates = random.sample(all_coordinates, 10)
    return jsonify(selected_coordinates)

if __name__ == '__main__':
    app.run(debug=True)
