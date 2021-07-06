from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
file_path= r'C:\Notebook\Technocolab intern\SVM_Linear_model.pkl'
model=pickle.load(open(file_path,'rb'))

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    opn=request.form.get('open')
    high=request.form.get('high')
    low=request.form.get('low')
    time=request.form.get('time')
    Day=request.form.get('Day')
    x,y = time.split(':')
    time = int(x)*3600+int(y)*60
    prediction=model.predict(pd.DataFrame(columns=['Time','day_of_week','open','high','low',],
                              data=np.array([time,Day,opn,high,low]).reshape(1,5)))
    print(prediction)
    return str(prediction[0])



if __name__=='__main__':
    app.run(debug=True)