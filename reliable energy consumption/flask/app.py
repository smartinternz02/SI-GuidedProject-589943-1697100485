from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
app=Flask(__name__)
model=pickle.load(open('RESOURCE_ENERGY.pkl','rb'))  
@app.route("/")
@app.route("/home",methods=["GET","POST"])
def Home():
    return render_template("index.html")


@app.route("/inspect",methods=["GET","POST"])  
def inspect():
    return render_template("inspect.html") 


@app.route("/output",methods=["GET","POST"])  
def output():
    GlobalReactivePower=float(request.form['GlobalReactivePower']) 
    Global_intensity=float(request.form['Global_intensity'])   
    Sub_metering_1= float(request.form['Sub_metering_1']) 
    Sub_metering_2= float(request.form['Sub_metering_2'])  
    Sub_metering_3= float(request.form['Sub_metering_3'])
    x=[[GlobalReactivePower,Global_intensity,Sub_metering_1,Sub_metering_2,Sub_metering_3]]
    output=round(model.predict(x)[0],3)
    return render_template('output.html',output=output)
if __name__=="__main__":
    app.run(debug=True)