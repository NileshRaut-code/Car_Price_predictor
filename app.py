from unicodedata import numeric
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('./model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():

    a1 = request.form.get("1")
    a2 = request.form.get("2")
    a3 = request.form.get("3")
    a4 = request.form.get("4")
    a5 = request.form.get("5")
    a6 = request.form.get("6")
    a7 = request.form.get("7")
    a8= request.form.get("8")
    a9 = request.form.get("9")
    a10 = request.form.get("10")
    a11 = request.form.get("11")
    a12 = request.form.get("12")
    a13 = request.form.get("13")
    a14 = request.form.get("14")
    a15 = request.form.get("15")
    a16 = request.form.get("16")
   

    
    

    
    
    prediction = model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16]])
    print(prediction)
    return str(prediction)



if __name__ == "__main__":
    app.run(debug=True)

