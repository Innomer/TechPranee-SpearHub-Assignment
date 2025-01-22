from flask import Flask, request, jsonify
import os
import joblib
from model import train_model, predict_defect
from utils import save_file

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
MODEL_FOLDER = './models'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MODEL_FOLDER'] = MODEL_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MODEL_FOLDER, exist_ok=True)

# Upload endpoint
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    if file:
        file_path = save_file(file, app.config['UPLOAD_FOLDER'])
        return jsonify({"message": f"File uploaded to {file_path}"}), 200

# Train endpoint
@app.route('/train', methods=['POST'])
def train():
    try:
        model_type = request.args.get('model_type', 'DecisionTree')  # Default: DecisionTree
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sample.csv')
        metrics = train_model(file_path, model_type)
        
        model_path = os.path.join(app.config['MODEL_FOLDER'], f'{model_type}_model.pkl')
        joblib.dump(metrics['model'], model_path)

        return jsonify({"accuracy": metrics['accuracy'], "f1_score": metrics['f1_score']}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        model_type = request.args.get('model_type', 'DecisionTree')  # Default: DecisionTree
        input_data = request.get_json()

        model_path = os.path.join(app.config['MODEL_FOLDER'], f'{model_type}_model.pkl')
        if not os.path.exists(model_path):
            return jsonify({"error": "Model not trained. Train the model first."}), 400

        model = joblib.load(model_path)
        prediction = predict_defect(model, input_data)
        return jsonify(prediction), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)