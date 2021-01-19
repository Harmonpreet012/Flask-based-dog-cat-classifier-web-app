from flask import render_template, request
import os

def home():
    return render_template('home.html')

def predict():
    f= request.files['predictImage']            
    if(f.filename!=''):
        f.save(f.filename)                                    #saving file to be predicted
    
    path=f.filename
    from runtfmodel import predictMyPet
    ans = predictMyPet(path)                                                    #call prediction function
    os.remove(path)                                                             #delete image after prediction
    return render_template('showresult.html', text = ans)                       #send predicted data back



# $env:FLASK_APP = "helloflask.py"
# $env:FLASK_ENV = "development"
