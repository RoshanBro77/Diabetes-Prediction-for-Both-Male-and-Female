import io
import joblib
from tkinter import *

def isNumber(ans):
    
    if ans.strip().isdigit():
        
        return ans
    else:
        
        return 3


def convertGender(ans):
    if(ans == "Male" or ans == "male" or ans == "m" or ans == "M"):
        print(ans)
        
        return 1
    elif(ans == "Female" or ans == "female" or ans == "f" or ans == "F"):
        print(ans)
        
        return 0
    else:
        valid=False
        return 3


def convert(ans):
    if(ans == "Yes" or ans == "y" or ans == "Y" or ans == "yes"):
        print(ans)
       
        return 1

    elif(ans == "No" or ans == "n" or ans == "N" or ans == "no"):
        print(ans)
      
        return 0
    else:
        
        return 3

def start():
    Label(master, text="").grid(row=20,column=2)
    try:
        Age = (Entry1.get())
        age = isNumber(Age)
        Gender = (Entry2.get())
        gen = convertGender(Gender)
        Polyuria = (Entry3.get())
        ria = convert(Polyuria)
        Polydipsia = (Entry4.get())
        sia = convert(Polydipsia)
        Swl = (Entry5.get())
        swl = convert(Swl)
        Weak = (Entry6.get())
        weak = convert(Weak)
        Polyphagia = (Entry7.get())
        gia = convert(Polyphagia)
        GeniThru = (Entry8.get())
        thru = convert(GeniThru)
        visualblurring = (Entry9.get())
        vsl = convert(visualblurring)
        Itch = (Entry10.get())
        itch = convert(Itch)
        Irrr = (Entry11.get())
        irr = convert(Irrr)
        delahe = (Entry12.get())
        hear = convert(delahe)
        Para = (Entry13.get())
        para = convert(Para)
        MS = (Entry14.get())
        ms = convert(MS)
        Alp = (Entry15.get())
        alp = convert(Alp)
        Obesity = (Entry16.get())
        ob = convert(Obesity)
        model = joblib.load('file.pkl')
        a = [age, gen, ria, sia, swl, weak, gia, thru,
        vsl, itch, irr, hear, para, ms, alp, ob]
        output = model.predict([a])
        if (output!="Positive" and output!="Negative"):
            Label(master, text="Something went wrong re-run the program").grid(row=20,column=2)
        elif (output == "Positive"):
            Label(master, text="You have Diabeties take care of you").grid(row=22,column=2)
        
        elif(output == "Negative"):
            
            Label(master, text="You don't have Diabetic so hurray  ").grid(row=22,column=2)
        else:
            Label(master, text="Something went wrong re-run the program").grid(row=20,column=2)
    except:
        Label(master, text="Something went wrong re-run the program").grid(row=20,column=2)
   
       
    
        
            

        
master =Tk ()
master.geometry('700x500')
master.resizable(0,0)
master.title("Diabetes Prediction")
label = Label(master, text = "Diabetes Prediction",bg = "white",fg = "black").grid(row=0,column=2)

Entry1 = Entry(master)
Entry2 = Entry(master)
Entry3 = Entry(master)
Entry4 = Entry(master)
Entry5 = Entry(master)
Entry6 = Entry(master)
Entry7 = Entry(master)
Entry8 = Entry(master)
Entry9 = Entry(master)
Entry10 = Entry(master)
Entry11 = Entry(master)
Entry12 = Entry(master)
Entry13 = Entry(master)
Entry14 = Entry(master)
Entry15 = Entry(master)
Entry16= Entry(master)
    



Entry1.grid(row=3,column=2,columnspan=2)
Entry2.grid(row=4,column=2)
Entry3.grid(row=6,column=2)
Entry4.grid(row=7,column=2)
Entry5.grid(row=8,column=2)
Entry6.grid(row=9,column=2)
Entry7.grid(row=10,column=2)
Entry8.grid(row=11,column=2)
Entry9.grid(row=12,column=2)
Entry10.grid(row=13,column=2)
Entry11.grid(row=14,column=2)
Entry12.grid(row=15,column=2)
Entry13.grid(row=16,column=2)
Entry14.grid(row=17,column=2)
Entry15.grid(row=18,column=2)
Entry16.grid(row=19,column=2)
Label(master, text = "Enter Your Age: ").grid(row=3)
Label(master, text = "Enter Your Gender Type-'Male' or 'Female' or 'm' or 'f': ").grid(row=4)
Label(master, text = "Reply 'y' for Yes and 'n' for No only! ").grid(row=5,column=2)
Label(master, text = "Are you noticing accessive secretion of urine? ").grid(row=6)
Label(master, text = "Are you having unusual thirst?").grid(row=7)
Label(master, text = "Are you having sudden weight loss? ").grid(row=8)
Label(master, text = "Are you feeling weakness? ").grid(row=9)
Label(master, text = "Are you having excessive appetite or eating? ").grid(row=10)
Label(master, text = "Do you have infection or symptoms of infection near genital parts? ").grid(row=11)
Label(master, text = "Are You having visual issues recently i.e Lack of sharpness of vision? ").grid(row=12)
Label(master, text = "Do you have Itching? ").grid(row=13)
Label(master, text = "Do you easily annoyed or irritated? ").grid(row=14)
Label(master, text = "Do you have delayed hearing? ? ").grid(row=15)
Label(master, text = "Do you have mild paralysis or the weakening of a muscle? ").grid(row=16)
Label(master, text = "Are you facing muscle stiffness? ").grid(row=17)
Label(master, text = "Are your hair usually falls out in small patches on the scalp? ").grid(row=18)
Label(master, text = "Are you overweight? ").grid(row=19)
Button(master, text="Predict",command=start).grid()


mainloop()
    
    
    
