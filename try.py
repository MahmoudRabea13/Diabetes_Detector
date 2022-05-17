from flask import Flask, render_template, template_rendered, request, redirect
import pickle 
import numpy as np
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
input_data = []
model = pickle.load(open('final_model.sav','rb'))
app = Flask(__name__)
def preprocess(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    return input_data_reshaped
def loadmodel(input):
    return model.predict(input)
@app.route("/",methods=["POST","GET"])
def welcome():
    return render_template("welcome.html")
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        input_data=[]
        input_data.append(float(request.form["Pregnancies"]))
        input_data.append(float(request.form["Glucose"]))
        input_data.append(float(request.form["BloodPressure"]))
        input_data.append(float(request.form["SkinThickness"]))
        input_data.append(float(request.form["Insulin"]))
        input_data.append(float(request.form["BMI"]))
        input_data.append(float(request.form["DiabetesPedigreeFunction"]))
        input_data.append(float(request.form["Age"]))
        last_data = preprocess(input_data)
        out = loadmodel(last_data)
        if  out[0] == 0:
            content = "NOT Diabetes"
        else:
            content = "Diabetes"
    else:
        print("error but it work bro :)")
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
