# importing libraries 
# For the GUI (Graphical User Interface)
import tkinter as tk  
from functools import partial   
import numpy as nm  
# For plotting
import matplotlib.pyplot as mtp 
# For reading csv files 
import pandas as pd
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
#feature Scaling  
from sklearn.preprocessing import StandardScaler 
#Fitting Decision Tree classifier to the training set  
from sklearn.tree import DecisionTreeClassifier  
#Creating the Confusion matrix  
from sklearn.metrics import confusion_matrix  
from PIL import Image, ImageTk
   
   
def predictie(label_result, n1, n2, n3, n4, n5, n6): 
    
    #glicemie
    num1 = (n1.get())  
    #tensiune arteriala
    num2 = (n2.get()) 
    #inaltime (cm)
    num3 = (n3.get())
    #greutate (kg)
    num4 = (n4.get()) 
    #insulina
    num5 = (n5.get())
    #varsta
    num6 = (n6.get())
    
    greutate = int(num4)
    inaltime = int(num3)/100
    BMI = greutate/(inaltime*inaltime)
    print("BMI = ", BMI)
    
    #importing datasets  
    data_set= pd.read_csv('diabetes_bun.csv')  
        
    #Extracting Independent and dependent Variable
    x= data_set.iloc[:, 1:6].values  
    y= data_set.iloc[:, 6].values 
    
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.14, random_state=0)
    
    st_x= StandardScaler()  
    x_train= st_x.fit_transform(x_train)    
    x_test= st_x.transform(x_test) 
      
    classifier= DecisionTreeClassifier(criterion='entropy', random_state=0)  
    classifier.fit(x_train, y_train)  
    
    #Predicting the test set result  
    y_pred= classifier.predict(x_test)
    
    list1 = [[num1, num2, BMI, num5, num6]]
    list1= st_x.transform(list1)
    
    rezultat = classifier.predict(list1)
    
    cm = confusion_matrix(y_test, y_pred)  
    
    # outcome values order in sklearn
    tp, fn, fp, tn = confusion_matrix(y_test,y_pred,labels=[1,0]).reshape(-1)

    print('tp fp')
    print('fn tn')
    
    print(tp, fp)
    print(fn, tn)
    
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    
    print('accuracy = ', accuracy)
    print('precision = ', precision)
    print('recall = ', recall)
    
    #cat la suta din fp si fn reprezinta fp
    indicator1 = fp / (fp + fn)
    #cat la suta din fp si fn reprezinta fn -> persoane care au diabet, dar predictia spune ca nu au
    indicator2 = fn / (fp + fn)
    #cat la suta reprezinta predictiile corecte
    indicator3 = (tp + tn) / (tp + tn + fp + fn)
    #cat la suta reprezinta predictiile incorecte
    indicator4 = (fp + fn) / (tp + tn + fp + fn)
    
    print('indicator1 = ', indicator1)
    print('indicator2 = ', indicator2)
    print('indicator3 = ', indicator3)
    print('indicator4 = ', indicator4)  
     
    if rezultat == 0:
        label_result.config(text="%d" % rezultat, fg="green") 
    if rezultat == 1:
        label_result.config(text="%d" % rezultat, fg="red")
    return  
   
root = tk.Tk()    
  
root.title('Predictia diabetului')  

# Create a photoimage object of the image in the path
image1 = Image.open("D:\MASTER\Master an 1 sem 1\TCRI\Proiect TCRI\Surse Python\diabetes_background.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)
width, height = image1.size
root.geometry('1024x682')
   
number1 = tk.StringVar()  
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()  
number5 = tk.StringVar() 
number6 = tk.StringVar() 

labelNum1 = tk.Label(root,  
                  text = "GLICEMIE", font=("Ariel Bold", 15),bg="white").place(x = 130, 
                                           y = 180)
labelNum2 = tk.Label(root,  
                  text = "TENSIUNE ARTERIALA", font=("Ariel Bold", 15),bg="white").place(x = 130, 
                                           y = 220)
labelNum3 = tk.Label(root,  
                  text = "INALTIME(cm)", font=("Ariel Bold", 15),bg="white").place(x = 130, 
                                           y = 260)
labelNum4 = tk.Label(root,  
                  text = "GREUTATE(kg)", font=("Ariel Bold", 15),bg="white").place(x = 130, 
                                           y = 300)
labelNum5 = tk.Label(root,  
                  text = "INSULINA", font=("Ariel Bold", 15),bg="white").place(x = 130, 
                                           y = 340)
labelNum6 = tk.Label(root,  
                  text = "VARSTA", font=("Ariel Bold", 15),bg="white").place(x = 130, 
                                           y = 380)


  
labelResult = tk.Label(root, bg="white", font=("Ariel Bold", 40))  
  
labelResult.place(x=795, y=290)  
  
entryNum1 = tk.Entry(root, textvariable=number1, fg="black",width=20, bd=3,font=("Ariel Bold", 10, "bold")).place(x = 380, 
                                           y = 185) 
entryNum1 = tk.Entry(root, textvariable=number2, fg="black",width=20, bd=3,font=("Ariel Bold", 10, "bold")).place(x = 380, 
                                           y = 225)
entryNum1 = tk.Entry(root, textvariable=number3, fg="black",width=20, bd=3,font=("Ariel Bold", 10, "bold")).place(x = 380, 
                                           y = 265)
entryNum1 = tk.Entry(root, textvariable=number4, fg="black",width=20, bd=3,font=("Ariel Bold", 10, "bold")).place(x = 380, 
                                           y = 305)
entryNum1 = tk.Entry(root, textvariable=number5, fg="black",width=20, bd=3,font=("Ariel Bold", 10, "bold")).place(x = 380, 
                                           y = 345)
entryNum1 = tk.Entry(root, textvariable=number6, fg="black",width=20, bd=3,font=("Ariel Bold", 10, "bold")).place(x = 380, 
                                           y = 385)
  
predictie = partial(predictie, labelResult, number1, number2, number3, number4, number5, number6)  
  
buttonCal = tk.Button(root, text="SUBMIT", command=predictie, bg="white", fg="orange",  bd=4, height = 1, width = 7, padx=0, pady=0, font=("Ariel Bold", 15, "bold")).place(x = 270, 
                                           y = 425)  

root.mainloop()  





