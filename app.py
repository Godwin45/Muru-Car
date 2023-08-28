from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) 

@app.route('/',methods=['GET'])  
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET']) 
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            engine_rpm =int(request.form['engine_rpm'])
            lub_oil_pressure =float(request.form['lub_oil_pressure'])
            fuel_pressure =float(request.form['fuel_pressure'])
            coolant_pressure =float(request.form['coolant_pressure'])
            lub_oil_temp =float(request.form['lub_oil_temp'])
            coolant_temp =float(request.form['coolant_temp'])
     
            data = [engine_rpm,lub_oil_pressure,fuel_pressure,coolant_pressure,lub_oil_temp,coolant_temp]
            data = np.array(data).reshape(1, 6)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)