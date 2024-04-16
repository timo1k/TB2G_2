from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import pickle
import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split

app = Flask(__name__)
CORS(app)

# Load pipeline and model using the binary files
model = pickle.load(open('poopie_model.pkl', 'rb'))
data = pd.read_csv('bathroom_data_set.csv')
# Define the rating scale
reader = Reader(rating_scale=(1, 5))

# Load the dataset into Surprise format
dataset = Dataset.load_from_df(data[['building', "Floor-Section", "rating" ]], reader)

# Split the dataset into training and testing sets
trainset, testset = train_test_split(dataset, test_size=0.4, random_state=42)



@app.route('/startFunction')
def success():
   try:
      all_bathrooms = dataset.build_full_trainset().build_anti_testset()
      all_predictions = model.test(all_bathrooms)

      # Rank bathrooms based on predicted ratings
      ranked_bathrooms = sorted(all_predictions, key=lambda x: x.est, reverse=True)
   except Exception as e:
      print(e)
      return (f"error: {e}", 500)

   return (list(ranked_bathrooms[:10]), 200)

@app.route('/poop')
def poop():
   return "poop"


@app.route('/error')
def error():
   return 'error'

if __name__ == '__main__':
   app.run(debug=True, port=8080)
