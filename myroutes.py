from flask import render_template, request
import os

def home():
    return render_template('home.html')

def predict():
    f= request.files['predictImage']            
    if(f.filename!=''):
        f.save('images/'+f.filename)                                    #saving file to be predicted
    
    path="C:\\Users\\harmpon\\Desktop\\Flask pet identifier\\images\\"+f.filename    #path to the image file(change this as per your system)
    from runtfmodel import predictMyPet
    ans = predictMyPet(path)                                                    #call prediction function
    os.remove(path)                                                             #delete image after prediction
    return render_template('showresult.html', text = ans)                       #send predicted data back



# $env:FLASK_APP = "helloflask.py"
# $env:FLASK_ENV = "development"