import numpy as np
from flask import Flask, abort, jsonify, request
import _pickle as pickle

my_random_forest = pickle.load(open("iris_rfc.pkl", "rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    # all types of error checking should go here
    data = request.get_json(force=True)
    # convert our json into numpy array
    predict_request = [data['sl'], data['sw'], data['pl'], data['pw']]
    predict_request = np.array(predict_request)     # np array goes into random forest. prediction comes out
    y_hat = my_random_forest.predict(predict_request)   #return our prediction
    
    output = [y_hat[0]]
    return(jsonify(results=output))
    
if __name__ == '__main__':
    app.run(port = 9004, debug = True)
    
    