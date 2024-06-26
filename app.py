import numpy as np
from flask import Flask, request,render_template
import pickle
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
model = pickle.load(open('model1.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction == 1:
        output="Placed"
    else:
        output ="Not Placed"

    #output = np.around(prediction)
    

    return render_template('index.html', prediction_text='Prediction Result:{}'.format(output))
'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    #For direct API calls trought request
'''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
'''
if __name__ == "__main__":
    app.run(debug=True)
    
