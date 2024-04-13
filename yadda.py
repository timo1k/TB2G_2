import random
import json

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def train_model(data):
    # Split data into features (X) and target variable (y)
    X = data.drop(columns=['bathroom_id', 'rating'])
    y = data['rating']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Evaluate model performance
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    return clf

def predict_best_bathroom(model, bathroom_data):
    # Preprocess bathroom data
    # You may need to encode categorical variables, scale numerical features, etc.

    # Make prediction using the trained model
    predicted_rating = model.predict(bathroom_data)

    # Return the bathroom with the highest predicted rating
    best_bathroom_index = predicted_rating.argmax()
    best_bathroom = bathroom_data.iloc[best_bathroom_index]
    return best_bathroom

# Example usage:
# Load data
def poop():
    data = pd.read_csv("bathroom_data.csv")

    # Train the model
    model = train_model(data)

    # New bathroom data for prediction
    new_bathroom_data = pd.DataFrame({'cleanliness': [4], 'accessibility': [5], 'amenities': [4]})

    # Predict the best bathroom to use
    best_bathroom = predict_best_bathroom(model, new_bathroom_data)

    data = {
        "bathroom": best_bathroom
    }
    return json.dumps(data)

def getGPT():
    random_number = random.randint(1, 5)
    data = {
        "random_number": random_number
    }
    return json.dumps(data)

#todo write code to get info from db and turn into csv