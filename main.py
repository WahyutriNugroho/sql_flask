#main.py
from flask import Flask, jsonify, request
from db import get_predicts, add_predict

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def predicts():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        get_predicts(request.get_json())
        return 'Data Added'

    return add_predict()    

if __name__ == '__main__':
    app.run()
