import pickle
from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from src.Pipeline.predict_pipeline import CustomData, PredictPipline


app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            age=request.form.get('age'),
            bmi=request.form.get('bmi'),
            hypertension=request.form.get('hypertension'),
            heart_disease=request.form.get('heart_disease'),
            avg_glucose_level=request.form.get('avg_glucose_level'),
            Residence_type=request.form.get('Residence_type'),
            smoking_status=request.form.get('smoking_status'),
            work_type=request.form.get('work_type'),
            ever_married=request.form.get('ever_married')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictPipline()
        results=predict_pipeline.predict(pred_df)
        return render_template('home.html',results=results[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
