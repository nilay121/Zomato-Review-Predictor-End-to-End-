# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:19:59 2021

@author: NILAY
"""

from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import pickle
import numpy as np

model_pipe=pickle.load(open('pipeline_zomato.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.htm')

@app.route('/predict',methods=['POST','GET'])
def predictions():
    city_val=request.form['city']
    cusi_val=request.form['cuisine']
    tb=request.form['table_booking']
    on_delivery=request.form['online_delivering']
    db_now=request.form['delivering_now']
    locality=request.form['locality']
    so_menu=request.form['switch_to_order_menu']
    cost_pp=request.form['cost']
    votes=request.form['votes']
    cpp_votes=(int(cost_pp)/2)*int(votes)
    data={
        'City':[city_val],
        'Cuisines':[cusi_val],
        'avg_cost':[int(cost_pp)],
        'table_booking':[tb],
        'online_delivery':[on_delivery],
        'is_delivering_now':[db_now],
        'Locality':[locality],
        'Votes':[int(votes)],
        'switch_to_order_menu':[so_menu],
        'cpp_votes':[cpp_votes]
        }
    df_obt=pd.DataFrame(data)
    review_pred=model_pipe.predict(df_obt).round(1)

    return render_template('index.htm',Make_Prediction=f"The predicted review is {review_pred[0]}")

if __name__=='__main__':
    app.run(debug=True,port=4444)