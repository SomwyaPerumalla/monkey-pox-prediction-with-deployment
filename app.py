from flask import Flask, render_template, request
# import jsonify
# import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Model_pox.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method== 'POST':

        Swollen_Tonsils = request.form['Swollen Tonsils']
        if(Swollen_Tonsils=='Yes'):
            Swollen_Tonsils=1
        else:
            Swollen_Tonsils=0
        Solitary_Lesion = request.form['Solitary Lesion']
        if(Solitary_Lesion=='Yes'):
            Solitary_Lesion=1
        else:
            Solitary_Lesion=0	
        Penile_Oedema = request.form['Penile Oedema']
        if(Penile_Oedema=='Yes'):
            Penile_Oedema=1
        else:
            Penile_Oedema=0        
        Oral_Lesions = request.form['Oral Lesions']
        if(Oral_Lesions=='Yes'):
            Oral_Lesions=1
        else:
            Oral_Lesions=0
        Sore_Throat = request.form['Sore Throat']
        if(Sore_Throat=='Yes'):
            Sore_Throat=1
        else:
            Sore_Throat=0
        Rectal_Pain = request.form['Rectal Pain']
        if(Rectal_Pain=='Yes'):
            Rectal_Pain=1
        else:
            Rectal_Pain=0
        HIV_Infection = request.form['HIV Infection']
        if(HIV_Infection=='Yes'):
            HIV_Infection=1
        else:
            HIV_Infection=0
        Sexually_Transmitted_Infection= request.form['Sexually Transmitted Infection']
        if(Sexually_Transmitted_Infection=='Yes'):
            Sexually_Transmitted_Infection=1
        else:
            Sexually_Transmitted_Infection=0 
        Sys_Ill= request.form['Systemic Illness']
        if(Sys_Ill=='Fever'):
            Fever=1
            Pains=0
            Lymph_Nodes=0
        elif(Sys_Ill=='Muscle Aches and Pain'):
            Fever=0
            Pains=1
            Lymph_Nodes=0
        elif(Sys_Ill=='Swollen Lymph Nodes'):
            Fever=0
            Pains=0
            Lymph_Nodes=1
        else:
            Fever=0
            Pains=0
            Lymph_Nodes=0          
        prediction=model.predict([[Rectal_Pain,Sore_Throat,Penile_Oedema,Oral_Lesions,Solitary_Lesion,Swollen_Tonsils,HIV_Infection,Sexually_Transmitted_Infection,Fever,Pains,Lymph_Nodes]])  
        print(prediction)
        
        if prediction[0]==0:
            return render_template('index.html',prediction_texts="Congratulations you dont have any monkey-pox symptoms")
        else:
            return render_template('index.html',prediction_texts="Sorry you are like to have Monkey-pox please check with doctor")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)