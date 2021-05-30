#main.py
from flask import Flask, jsonify, request

app = Flask(__name__)
predicts = [
    {
        "image": "fire.jpg",
        "latitude": "1",
        "longtitude": "1",
        "kelas": "1",
        "probabilitas": 1
    },
    {
        "image": "sky.jpg",
        "latitude": "2",
        "longtitude": "2",
        "kelas": "2",
        "probabilitas": 2
    },
    {
        "image": "river.jpg",
        "latitude": "3",
        "longtitude": "3",
        "kelas": "3",
        "probabilitas": 3
    }
]
@app.route('/predict')
def home():
    return jsonify(predicts)

@app.route('/predict', methods=['POST'])
def add_predicts():
    predict = request.get_json()
    predicts.append(predict)
    return jsonify(predicts)

if __name__ == '__main__':
  app.run(debug=True)
