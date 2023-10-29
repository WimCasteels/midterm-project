import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_depth=4_samples=200.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('Mushroom')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    poison = y_pred >= 0.5

    result = {
        'poison_probability': float(y_pred),
        'poisonous': bool(poison)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)