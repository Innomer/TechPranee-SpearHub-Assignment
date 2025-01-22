# Predictive Analysis for Manufacturing Operations

This project implements a RESTful API using Flask to predict machine downtime or product defects in a manufacturing environment. It supports multiple machine learning models, including a **Stacking Classifier**, **Logistic Regression**, **Decision Tree Classifier** and **Random Forest Classifier**. The API provides endpoints to upload data, train a predictive model, and make predictions.

---

## **Features**
- **Upload Endpoint**: Accepts CSV files containing manufacturing data.
- **Train Endpoint**: Trains a predictive model (Decision Tree, Logistic Regression, Random Forest, or Stacking Classifier) on the uploaded dataset and returns performance metrics.
- **Predict Endpoint**: Accepts JSON input to predict downtime or defects and returns predictions with confidence scores.

---

## **Setup Instructions**

### 1. **Prerequisites**
- Python 3.8+
- pip (Python package manager)

### 2. **Clone the Repository**
```bash
git clone <repository-link>
cd predictive_analysis
```

### 3. **Install Dependencies**
- Install required Python libraries
```bash
pip install -r requirements.txt
```

### 4. **Run the Application**
- Start the Flask server
```bash
python app.py
```
- By default, the server will run at http://127.0.0.1:5000.

---

## **API Endpoints**

### 1. **Upload Data**
- Endpoint: POST /upload
- Description: Upload a CSV file containing manufacturing data.
- Example Request (sample is provided in test_dataset):
```bash
curl -X POST -F "file=@test_dataset/manufacturing_defect_dataset.csv" http://127.0.0.1:5000/upload
```
- Example Response:
```bash
{
  "message": "File uploaded to ./uploads/sample.csv"
}
```

### 2. **Train the Model**
- Endpoint: POST /train?model_type=<model_type>
- Description: Trains the specified machine learning model on the uploaded dataset.
- Supported Models: DecisionTree (default), LogisticRegression, RandomForest, Stacking
- Example Request:
```bash
curl -X POST http://127.0.0.1:5000/train?model_type=Stacking
```
- Example Response:
```bash
{
  "accuracy": 0.95,
  "f1_score": 0.92
}
```

### 3. **Make Predictions**
- Endpoint: POST /predict?model_type=<model_type>
- Description: Accepts JSON input and returns predictions with confidence scores.
- Supported Models: DecisionTree (default), LogisticRegression, RandomForest, Stacking
- Example Request: Save the following input as input.json (sample is provided in test_dataset):
```bash
{
  "ProductionVolume": 500,
  "ProductionCost": 1500,
  "SupplierQuality": 0.85,
  "DeliveryDelay": 3,
  "DefectRate": 0.02,
  "QualityScore": 95,
  "MaintenanceHours": 10,
  "DowntimePercentage": 5,
  "InventoryTurnover": 7,
  "StockoutRate": 0.01,
  "WorkerProductivity": 80,
  "SafetyIncidents": 1,
  "EnergyConsumption": 1200,
  "EnergyEfficiency": 0.92,
  "AdditiveProcessTime": 4,
  "AdditiveMaterialCost": 50
}
```
- Run the following command:
```bash
curl -X POST -H "Content-Type: application/json" -d @test_dataset/sample_test.json http://127.0.0.1:5000/predict?model_type=Stacking
```
- Example Response:
```bash
{
  "Defect": "Yes",
  "Confidence": 0.88
}
```

---

## Project Structure:
predictive_analysis/
│
├── app.py                # Main Flask app
├── model.py              # ML model logic
├── utils.py              # Helper functions
├── uploads/              # Folder for uploaded datasets
│   └── sample.csv        # Example dataset
├── test_dataset/         # Folder for dataset used for creation of this project
│   └── manufacturing_defect_dataset.csv        # Example dataset
│   └── sample_test.json        # Example json for predict API
├── models/               # Folder for saved models
│   └── Stacking_model.pkl # Example saved stacking model
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

---

## Dataset Information:
Link: https://www.kaggle.com/datasets/rabieelkharoua/predicting-manufacturing-defects-dataset
DOI: 10.34740/kaggle/dsv/8715500
Citation: Rabie El Kharoua. (2024). 🏭 Predicting Manufacturing Defects Dataset [Data set]. Kaggle. https://doi.org/10.34740/KAGGLE/DSV/8715500