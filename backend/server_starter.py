from flask import Flask
import flask
import json
from flask_cors import CORS

from sklearn.neighbors import KNeighborsClassifier

from project_somerville import *

app = Flask(__name__)
CORS(app)

def getConfusionMatrix(prediction_data):
    # print(prediction_data)
    confusion_matrix_dict = {}
    ground_truth = prediction_data['ground_truth']
    
    for keys in prediction_data:
        truePositive = sum([prediction == label for (_, prediction), (_, label) in zip(prediction_data[keys].items(), ground_truth.items()) if label == 1])
        trueNegative = sum([prediction == label for (_, prediction), (_, label) in zip(prediction_data[keys].items(), ground_truth.items()) if label == 0])
        falsePositive = sum([prediction != label for (_, prediction), (_, label) in zip(prediction_data[keys].items(), ground_truth.items()) if label == 0])
        falseNegative = sum([prediction != label for (_, prediction), (_, label) in zip(prediction_data[keys].items(), ground_truth.items()) if label == 1])

        # TODO: calculate confusion matrix

        confusion_matrix_dict.update({keys : {"truePositive": truePositive, 
                                            "trueNegative": trueNegative, 
                                            "falsePositive": falsePositive, 
                                            "falseNegative": falseNegative} })

    return confusion_matrix_dict

@app.route("/")
def hello():
    return "Whoops, Wrong Page!"

@app.route('/confusionMatrix', methods=["GET"])
def confusionMatrix():
    print("users endpoint reached...")
    with open("model_predictions.json", "r") as f:
        prediction_data = json.load(f)
    
    with open("somerville_happiness_2018_data.json", "r") as f:
        happiness_data = json.load(f)

    confusion_matrix = getConfusionMatrix(prediction_data)

    projection_result = project_somerville()

    data = [prediction_data, happiness_data, confusion_matrix, projection_result]

    return flask.jsonify(data)

if __name__ == "__main__":
    app.debug = True
    app.run("localhost", 6969)