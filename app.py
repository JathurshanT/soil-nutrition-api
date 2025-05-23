from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = load('soil_nutrition_model.joblib')

# Define the recommendations for each level
recommendations = {
    1: "Add N, P, K (all nutrients are low)",
    2: "Add N (P and K are sufficient)",
    3: "Add P (N and K are sufficient)",
    4: "Add K (N and P are sufficient)",
    5: "Add N and P (K is sufficient)",
    6: "Add P and K (N is sufficient)",
    7: "Add N and K (P is sufficient)",
    8: "Perfect condition (no fertilizer needed)"
}

# Home route
@app.route('/')
def home():
    return """
    <h1>Soil Nutrition Control System API</h1>
    <p>Send a POST request to /predict with JSON data containing N, P, K, and pH values.</p>
    <p>Example: {"n": 70, "p": 80, "k": 70, "ph": 6}</p>
    """

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Extract soil values
        n = float(data['n'])
        p = float(data['p'])
        k = float(data['k'])
        ph = float(data['ph'])
        
        # Validate the input values
        if not (0 <= n <= 100):
            return jsonify({"success": False, "error": "N value must be between 0 and 100"})
        if not (0 <= p <= 120):
            return jsonify({"success": False, "error": "P value must be between 0 and 120"})
        if not (0 <= k <= 110):
            return jsonify({"success": False, "error": "K value must be between 0 and 110"})
        if not (0 <= ph <= 14):
            return jsonify({"success": False, "error": "pH value must be between 0 and 14"})
        
        # Create DataFrame for prediction
        df = pd.DataFrame({'N': [n], 'P': [p], 'K': [k], 'pH': [ph]})
        
        # Make prediction
        prediction = int(model.predict(df)[0])
        
        # Return result
        return jsonify({
            'success': True,
            'prediction': prediction,
            'recommendation': recommendations[prediction]
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

# Add a simple test route
@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'success': True,
        'message': 'API is working correctly!'
    })

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)