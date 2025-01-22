import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.metrics import accuracy_score, f1_score

def train_model(file_path, model_type="DecisionTree"):
    data = pd.read_csv(file_path)
    
    # Drop last column (Assuming last column is target and rest are numerical values for training datapoints)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    # Standardize data
    X = (X - X.mean()) / X.std()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Select model
    if model_type == "DecisionTree":
        model = DecisionTreeClassifier()
    elif model_type == "LogisticRegression":
        model = LogisticRegression()
    elif model_type == "RandomForest":
        model = RandomForestClassifier()
    elif model_type == "Stacking":
        base_models = [
            ("decision_tree", DecisionTreeClassifier()),
            ("logistic_regression", LogisticRegression()),
            ("random_forest", RandomForestClassifier())
        ]
        model = StackingClassifier(
            estimators=base_models,
            final_estimator=LogisticRegression(),
            cv=5  # 5-fold cross-validation
        )
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return {"model": model, "accuracy": accuracy, "f1_score": f1}

def predict_defect(model, input_data):
    features = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(features)
    confidence = model.predict_proba(features).max()

    return {"Defect": "Yes" if prediction[0] else "No", "Confidence": confidence}