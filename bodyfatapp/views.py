from django.shortcuts import render
from joblib import load
import pandas as pd
import numpy as np

model=load('./savedModel/model.joblib')

# Create your views here.
def index(request):

    if request.method=="POST":
        age=float(request.POST['Age'])
        weight=float(request.POST['Weight'])*2.20462
        height=float(request.POST['Height'])*0.39370079
        neck=float(request.POST['Neck'])
        abdomen=float(request.POST['Abdomen'])
        thigh=float(request.POST['Thigh'])
        knee=float(request.POST['Knee'])
        ankle=float(request.POST['Ankle'])
        bicep=float(request.POST['Biceps'])
        forearm=float(request.POST['Forearm'])
        wrist=float(request.POST['Wrist'])

        

        inputs=pd.DataFrame(data=({"Age":[age], "Weight":[weight], "Height":[height], "Neck":[neck],
                "Abdomen":[abdomen],"Thigh":[thigh], "Knee":[knee],
                "Ankle":[ankle],"Biceps":[bicep],"Forearm":[forearm],"Wrist":[wrist]}),index=[0])
        
        y_pred=model.predict(inputs)
        
        if age>=20 and age<=39:
            if y_pred[0]>8 and y_pred[0]<19:
                y_pred="Normal body fat percent" + " " +str(round(y_pred[0],2))+"%"
                
        
            elif y_pred[0]> 19:
                y_pred="High body fat percent"  + " " +str(round(y_pred[0],2))+"%"
        
            else:
                y_pred="Low body fat percent"  + " " +str(round(y_pred[0],2))+"%"
        
        elif age>=40 and age<=59:
            if y_pred[0]>=11 and y_pred[0]<=21:
                y_pred="Normal bodyfat percent" + " " +str(round(y_pred[0],2))+"%"
        
            elif y_pred[0]> 21:
                y_pred="High body fat percent "  + " " +str(round(y_pred[0],2))+"%"
        
            else:
                y_pred="Low body fat percent"  + " " +str(round(y_pred[0],2))+"%"
        
        else:
            if y_pred[0]>13 and y_pred[0]<24:
                y_pred="Normal bodyfat percent" + " " +str(round(y_pred[0],2))+"%"
            elif y_pred[0]> 24:
                y_pred="High body fat percent"  + " " +str(round(y_pred[0],2))+"%"
            else:
                y_pred="Low body fat percent"  + " " +str(round(y_pred[0],2))+"%"

        return render(request,"index.html",{"result":y_pred})
    return render(request,"index.html")