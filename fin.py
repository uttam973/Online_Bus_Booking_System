#helps in creating a GUI interface
import tkinter as tk
from tkinter import *
#helps in styling tkinter widget set
from tkinter import ttk
#helps in displaying pop up messages 
from tkinter import messagebox
#provides calendar and dateentry widgets
from tkcalendar import DateEntry
#displaying of date and time in proper format
import datetime
from datetime import date
from datetime import datetime
#dialog box where we use askstring for user to give input within dialog box
from tkinter.simpledialog import askstring

#seat= remove buttons give entry alone with validation
#front end working
from tkinter import *  
from PIL import ImageTk,Image  



def user():
    
    global app
    app=Toplevel()
    app.geometry("2000x1400")
    app.title("BUS RESERVATION SYSTEM")

    global img
    path = path ="C:\\Users\\aarav\\Downloads\\skyy.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(app, image=img)
    panel.pack(fill=BOTH,anchor=W)

    Frame_login=Frame(app,bg="light blue")
    Frame_login.place(x=550,y=150,height=550,width=500)

    global e3
    e3=Entry(app,text="From",font=("Montserrat",11))
    e3.place(x=600,y=330,height=30,width=250)
    
    global e4
    e4=Entry(app,text="To",font=("Montserrat",11))
    e4.place(x=600,y=430,height=30,width=250)

   
    global cal
    today = date.today()
    cal = DateEntry(app,selectmode='day',year=today.year,month=today.month,day=today.day+1,mindate=date.today(),maxdate=date(2022,2,28),date_pattern='yyyy-mm-dd',background="red",foreground="white")
    cal.place(x=600,y=530,height=30,width=250)
    
    global x
    x=e3.get()
    global y
    y=e4.get()
    
  
    l1=Label(app,text="Online Bus Booking",font=("Algerian",30,"bold"),bg="light blue",fg="black").place(x=600,y=200)
    
    l2=Label(app,text="From",font=("Algerian",10),bg="light blue",fg="black").place(x=600,y=300)
    
    l3=Label(app,text="To",font=("Algerian",10),bg="light blue",fg="black").place(x=600,y=400)
  
    l4=Label(app,text="Date Of Departure",font=("Algerian",10),bg="light blue",fg="black").place(x=600,y=500)
    
    Button(app,text="Search",command=bookbus,height=2,width=30,bg="yellow").place(x=700,y=600)

           


def booking():
    From=["Bangalore","bangalore","Mumbai","Goa","Sion","sion","mumbai","goa","Delhi","delhi","Punjab","punjab"]
    To=["Bangalore","Mumbai","mumbai","Goa","goa","Sion","sion","bangalore","Delhi","delhi","Punjab","punjab"]
    
    global e3
    global e4

    
    x=e3.get()
    y=e4.get()
    global bk
    bk=Toplevel()
    bk.geometry("2000x1400")
    bk.configure(background="white")
    bk.title("Bus Booking Site")

    global img2
    path = "C:\\Users\\aarav\\Downloads\\skyy.png"
    img2 = ImageTk.PhotoImage(Image.open(path))
    panel = Label(bk, image=img)
    panel.pack(fill=BOTH,anchor=W)
    
    bookframe=Frame(bk,height=300,width=500,bg="light blue")
    bookframe.place(x=550,y=150)
    l=Label(bk,text="Departure and Arrival",font=("Montserrat",15,"bold"),bg="light blue")    
    l.place(x=570,y=150)
    Label(bk,text="Departure:",font=("Montserrat",10),bg="light blue").place(x=570,y=200)   
    labelfrom=Label(bk,text=e3.get(),bg="light blue").place(x=650,y=200)                      
    Label(bk,text="Arrival:",font=("Montserrat",10),bg="light blue").place(x=570,y=240)       
    labelto=Label(bk,text=e4.get(),bg="light blue").place(x=650,y=240)                        
    Label(bk,text="..........................................................................................................................................",bg="light blue").place(x=570,y=280)
    Label(bk,text="Bus: ",font=("Montserrat",10),bg="light blue").place(x=570,y=310)
        
    if (x in From[0:2]) and (y in To[1:3]):        
        options=[
                        "VRL Travels",
                        "National Travels",
                        "SRS Travels"
                ]
        
        
        global combo
        combo=ttk.Combobox(bk,value=options)
        combo.place(x=650,y=310)
        combo.current(0)
                
                    
                        
                        
    elif (x in From[4:6]) and (y in To[3:5]):
        options=[
                        "Anand Travels",
                        "Ivy Travels(Rajdhani)",
                        "zingbus"
                ]
        
        combo=ttk.Combobox(bk,value=options)
        combo.place(x=650,y=310)
        combo.current(0)
                    
    elif (x in From[10:]) and (y in To[8:10]):
        options=[
                        "JKM Travels",
                        "zingbus",
                        "IntrCity SmartBus"
                ]
        
        combo=ttk.Combobox(bk,value=options)
        combo.place(x=650,y=310)
        combo.current(0)

    global e          
    l=Label(bk,text="Seat",font=("Montserrat",10),bg="light blue")
    l.place(x=810,y=310)
        
    e=Entry(bk,text="Seat Chosen")
    e.place(x=860,y=310)
                    
    Label(bk,text="..........................................................................................................................................",bg="light blue").place(x=570,y=340)
                
    Label(bk,text="Fare Details ",font=("Montserrat",10),bg="light blue").place(x=570,y=380)
    Label(bk,text="800",font=("Montserrat",10),bg="light blue").place(x=650,y=380)
    Button(bk,text="PROCEED TO BOOK",command=bookticket,bg="yellow").place(x=730,y=410)
   

        
def bookbus():
    From=["Bangalore","bangalore","Mumbai","Goa","Sion","sion","mumbai","goa","Delhi","delhi","Punjab","punjab"]
    To=["Bangalore","Mumbai","mumbai","Goa","goa","Sion","sion","bangalore","Delhi","delhi","Punjab","punjab"]
    x=e3.get()
    y=e4.get()

    if x in From and y in To:
        global book
        book=Toplevel()
        book.geometry("2000x1400")
        book.configure(background="white")
        book.title("Bus Booking Site")
      
        global img1
        path = "C:\\Users\\aarav\\Downloads\\skyy.png"
        img1= ImageTk.PhotoImage(Image.open(path))
        panel = Label(book, image=img)
        panel.pack(fill=BOTH,anchor=W)
        

        x1=Label(book,text="Journey From "+e3.get()+" to "+e4.get(),bg='light blue',fg="red",font=("Montserrat",25))
        x1.place(x=1,y=1)

        Label(book,text="Bus",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(y=60)
        Label(book,text="Available seats",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=300,y=60)
        Label(book,text="Departure time",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=700,y=60)
        Label(book,text="Arrival time",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=1000,y=60)
        Label(book,text="Duration",font=("Montserrat",10),height=2,width=40,bg="black",fg="white").place(x=1280,y=60)                    
                
        if (x in From[0:2]) and (y in To[1:3]):
            l1=Label(book,text="VRL Travels",font=("Montserrat",10),height=10,width=50,bg="light blue").place(y=100)
                
            l1=Label(book,text="VRL Travels",font=("Montserrat",10),height=10,width=50,bg="light blue").place(y=100)
                
            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=100)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=130)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=100)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=130)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=100)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=130)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=100)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=130)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=100)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=130)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=200)
            b11=Button(book,text="D2",bg="red",state=DISABLED).place(x=450,y=230)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=200)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=230)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=200)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=230)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=200)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=230)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=200)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=230)
               
                
                

            Label(book,text="16:00",font=("Montserrat",10),height=10,width=50,bg="light blue").place(x=700,y=100)
            Label(book,text="9:00",font=("Montserrat",10),height=10,width=50,bg="light blue").place(x=1000,y=100)
            Label(book,text="17h 00m",font=("Montserrat",10),height=10,width=50,bg="light blue").place(x=1260,y=100)
                
            Label(book,text="National travels",font=("Montserrat",10),height=13,width=50,bg="light blue").place(y=270)
                
            b1=Button(book,text="C1",bg="green",command=booking).place(x=450,y=300)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=330)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=300)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=330)
            b3=Button(book,text="C5",bg="green",command=booking).place(x=550,y=300)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=330)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=300)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=330)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=300)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=330)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=400)
            b11=Button(book,text="D2",bg="green",command=booking).place(x=450,y=430)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=400)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=430)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=400)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=430)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=400)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=430)
            b5=Button(book,text="D9",bg="green",command=booking).place(x=650,y=400)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=430)
                
               
                
                
            Label(book,text="15:35",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=700,y=270)
            Label(book,text="11:00",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=1000,y=270)
            Label(book,text="19h 25m",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=1260,y=270)
                
                
            Label(book,text="SRS Travels",font=("Montserrat",10),height=13,width=50,bg="light blue").place(y=490)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=520)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=550)
            b2=Button(book,text="C3",bg="red",command=DISABLED).place(x=500,y=520)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=550)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=520)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=550)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=520)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=550)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=520)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=550)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=620)
            b11=Button(book,text="D2",bg="red",state=DISABLED).place(x=450,y=650)
            b2=Button(book,text="D3",bg="red",command=DISABLED).place(x=500,y=620)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=650)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=620)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=650)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=620)
            b44=Button(book,text="D8",bg="red",state=DISABLED).place(x=600,y=650)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=620)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=650)
                
            Label(book,text="21:00",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=700,y=490)
            Label(book,text="14:30",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=1000,y=490)
            Label(book,text="17h 30m",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=1260,y=490)
            
           
        elif (x in From[4:6]) and (y in To[3:5]):
               
            Label(book,text="Anand Travels",font=("Montserrat",10),height=10,width=50,bg="light blue").place(y=100)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=100)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=130)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=100)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=130)
            b3=Button(book,text="C5",bg="green",command=booking).place(x=550,y=100)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=130)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=100)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=130)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=100)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=130)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=200)
            b11=Button(book,text="D2",bg="green",command=booking).place(x=450,y=230)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=200)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=230)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=200)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=230)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=200)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=230)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=200)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=230)

            Label(book,text="17:10",font=("Montserrat",10),height=10,width=50,bg="light gray").place(x=700,y=100)
            Label(book,text="08:00",font=("Montserrat",10),height=10,width=50,bg="light gray").place(x=1000,y=100)
            Label(book,text="14h 50m",font=("Montserrat",10),height=10,width=50,bg="light gray").place(x=1260,y=100)
                
            Label(book,text="Ivy Travels(Rajdhani)",font=("Montserrat",10),height=13,width=50,bg="light blue").place(y=270)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=300)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=330)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=300)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=330)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=300)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=330)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=300)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=330)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=300)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=330)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=400)
            b11=Button(book,text="D2",bg="green",command=booking).place(x=450,y=430)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=400)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=430)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=400)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=430)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=400)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=430)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=400)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=430)
                
            Label(book,text="19:50",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=700,y=270)
            Label(book,text="10:30",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=1000,y=270)
            Label(book,text="14h 40m",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=1260,y=270)

            Label(book,text="zingbus",font=("Montserrat",10),height=13,width=50,bg="light gray").place(y=490)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=520)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=550)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=520)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=550)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=520)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=550)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=520)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=550)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=520)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=550)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=620)
            b11=Button(book,text="D2",bg="red",state=DISABLED).place(x=450,y=650)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=620)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=650)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=620)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=650)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=620)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=650)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=620)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=650)
                
            Label(book,text="17:00",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=700,y=490)
            Label(book,text="09:10",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=1000,y=490)
            Label(book,text="16h 10m",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=1260,y=490)
               
        elif (x in From[10:]) and (y in To[8:10]):
                
            Label(book,text="JKM Travels",font=("Montserrat",10),height=10,width=50,bg="light gray").place(y=100)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=100)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=130)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=100)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=130)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=100)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=130)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=100)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=130)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=100)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=130)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=200)
            b11=Button(book,text="D2",bg="red",state=DISABLED).place(x=450,y=230)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=200)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=230)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=200)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=230)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=200)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=230)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=200)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=230)
                
            Label(book,text="05:30",font=("Montserrat",10),height=10,width=50,bg="light gray").place(x=700,y=100)
            Label(book,text="11:00",font=("Montserrat",10),height=10,width=50,bg="light gray").place(x=1000,y=100)
            Label(book,text="5h 30m",font=("Montserrat",10),height=10,width=50,bg="light gray").place(x=1260,y=100)

            Label(book,text="zingbus",font=("Montserrat",10),height=13,width=50,bg="light gray").place(y=270)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=300)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=330)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=300)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=330)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=300)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=330)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=300)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=330)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=300)
            b55=Button(book,text="C10",bg="green",command=booking).place(x=650,y=330)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=400)
            b11=Button(book,text="D2",bg="red",state=DISABLED).place(x=450,y=430)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=400)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=430)
            b3=Button(book,text="D5",bg="green",command=booking).place(x=550,y=400)
            b33=Button(book,text="D6",bg="green",command=booking).place(x=550,y=430)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=400)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=430)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=400)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=430)
                
            Label(book,text="08:00",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=700,y=270)
            Label(book,text="15:00",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=1000,y=270)
            Label(book,text="07h 00m",font=("Montserrat",10),height=13,width=50,bg="light gray").place(x=1260,y=270)

            Label(book,text="IntrCity SmartBus",font=("Montserrat",10),height=13,width=50,bg="light blue").place(y=490)

            b1=Button(book,text="C1",bg="red",state=DISABLED).place(x=450,y=520)
            b11=Button(book,text="C2",bg="red",state=DISABLED).place(x=450,y=550)
            b2=Button(book,text="C3",bg="green",command=booking).place(x=500,y=520)
            b22=Button(book,text="C4",bg="green",command=booking).place(x=500,y=550)
            b3=Button(book,text="C5",bg="red",state=DISABLED).place(x=550,y=520)
            b33=Button(book,text="C6",bg="green",command=booking).place(x=550,y=550)
            b4=Button(book,text="C7",bg="red",state=DISABLED).place(x=600,y=520)
            b44=Button(book,text="C8",bg="red",state=DISABLED).place(x=600,y=550)
            b5=Button(book,text="C9",bg="red",state=DISABLED).place(x=650,y=520)
            b55=Button(book,text="C10",bg="red",state=DISABLED).place(x=650,y=550)

            b1=Button(book,text="D1",bg="green",command=booking).place(x=450,y=620)
            b11=Button(book,text="D2",bg="red",state=DISABLED).place(x=450,y=650)
            b2=Button(book,text="D3",bg="green",command=booking).place(x=500,y=620)
            b22=Button(book,text="D4",bg="green",command=booking).place(x=500,y=650)
            b3=Button(book,text="D5",bg="red",state=DISABLED).place(x=550,y=620)
            b33=Button(book,text="D6",bg="red",state=DISABLED).place(x=550,y=650)
            b4=Button(book,text="D7",bg="red",state=DISABLED).place(x=600,y=620)
            b44=Button(book,text="D8",bg="green",command=booking).place(x=600,y=650)
            b5=Button(book,text="D9",bg="red",state=DISABLED).place(x=650,y=620)
            b55=Button(book,text="D10",bg="green",command=booking).place(x=650,y=650)
          
            Label(book,text="21:15",font=("Montserrat",10),height=13,width=50,bg="light blye").place(x=700,y=490)
            Label(book,text="01:30",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=1000,y=490)
            Label(book,text="04h 15m",font=("Montserrat",10),height=13,width=50,bg="light blue").place(x=1260,y=490)

              
        else:
            messagebox.showerror("Invalid","No bus found")
    else:
        messagebox.showerror("Invalid","No bus found")
    

                
def bookticket():
        global win
        win=Toplevel()
        win.geometry("2000x1400")
        win.title("Passenger Information")

        global img3
        path = "C:\\Users\\aarav\\Downloads\\skyy.png"
        img3 = ImageTk.PhotoImage(Image.open(path))
        panel = Label(win, image=img)
        panel.pack(fill=BOTH,anchor=W)
    
        frame1=Frame(win,height=650,width=650,bg="light blue")
        frame1.place(x=530,y=60)
        
                
        gender = tk.IntVar()
        label1=Label(win,text="Passenger Details",font=("Algerian",25),bg="light blue").place(x=700,y=70)
        label2=Label(win,text="Name",font=("Algerian",15),bg="light blue").place(x=600,y=120)
        global entry2
        entry2=Entry(win,text="Name",font=("Montserrat"))
        entry2.place(x=600,y=170)
        
        global entry5
        entry5=Entry(win,text="Email ID",width=30,font=("Montserrat"))
        entry5.place(x=600,y=470)
        
        global entry6
        entry6=Entry(win,text="Phone",font=("Montserrat"),bg="white")
        entry6.place(x=600,y=570)
        label3=Label(win,text="Gender",font=("Montserrat",15),bg="light blue").place(x=600,y=220)
        radiobutton_1 = tk.Radiobutton(win, text='Male', variable=gender, value=1,bg="light blue")
        radiobutton_1.place(x=600,y=270)
        radiobutton_2 = tk.Radiobutton(win, text='Female', variable=gender, value=2,bg="light blue")
        radiobutton_2.place(x=600,y=320)
        label4=Label(win,text="Contact Details",font=("Algerian",15),bg="light blue").place(x=600,y=370)
        label5=Label(win,text="Email ID",font=("Algerian",15),bg="light blue").place(x=600,y=420)
        label6=Label(win,text="Phone",font=("Algerian",15),bg="light blue").place(x=600,y=520)


        def paying():
            a=entry2.get()
            b=entry5.get()
            c=entry6.get()
            root.withdraw()
            
            
            if a=='' or b=='' or c=='':
                messagebox.showerror("Invalid","Please enter all the details")
                
            elif len(c)<10:
                messagebox.showerror("Invalid","Please enter the right Phone Number")
                
            elif b.endswith("@gmail.com")!=True:
                messagebox.showerror("Invalid","Please enter the right email")
                
            elif a.isalpha()!=True:
                messagebox.showerror("Invalid Name","Please enter valid Name")
                           
            else:
                global r
                r=Toplevel()
                r.geometry("800x500")
                r.title("Payment")
                r.configure(bg="white")

                canvas=Canvas(r, width=800,height=70,bg="light green")
                canvas.place(y=20)

                # Add a line in canvas widget
                canvas.create_line(1,5,900,5, fill="green", width=5)

                l1=Label(r,text="Amount payable: Rs.800",font=("Montserrat",15),bg="light green")
                l1.place(x=7,y=40)

                canvas.create_line(1,70,900,70, fill="green", width=5)

                l2=Label(r,text="Select card type:",font=("Montserrat",15),bg="white")
                l2.place(x=10,y=120)

                radiobutton_1 = Radiobutton(r,value=1,bg="white")
                radiobutton_1.place(x=190,y=125)
                
                global img7
                path2 = "C:\\Users\\aarav\\Downloads\\logo (1).png"
                img7 = ImageTk.PhotoImage(Image.open(path2))
                pane2 = Label(r, image=img7,bg="white")
                pane2.place(x=220,y=120)

                global ent3
                l3=Label(r,text="Card no",font=("Montserrat",15),bg="white")
                l3.place(x=90,y=180)
                ent3=Entry(r,text="Card no",font=("Montserrat",15),bg="light yellow")
                ent3.place(x=190,y=180)

                global ent4
                l4=Label(r,text="Name on the card",font=("Montserrat",15),bg="white")
                l4.place(x=10,y=230)
                ent4=Entry(r,text="Name on the card",font=("Montserrat",15),bg="light yellow")
                ent4.place(x=190,y=230)

                global cal
                l5=Label(r,text="Expiry date",font=("Montserrat",15),bg="white")
                l5.place(x=60,y=280)
                today = date.today()
                cal = DateEntry(r,selectmode='day',year=today.year,month=today.month,day=today.day+1,mindate=date.today(),date_pattern='yyyy-mm-dd',background="red",foreground="white")
                cal.place(x=190,y=280,height=30,width=250)

                global ent5
                l6=Label(r,text="CVV",font=("Montserrat",15),bg="white")
                l6.place(x=120,y=330)
                ent5=Entry(r,text="CVV",font=("Montserrat",15),bg="light yellow")
                ent5.place(x=190,y=330)

                global img8
                path3 = "C:\\Users\\aarav\\Downloads\\logo2 (1).png"
                img8 = ImageTk.PhotoImage(Image.open(path3))
                pane3 = Label(r, image=img8,bg="white")
                pane3.place(x=480,y=400)

                    
                b=Button(r,text="Proceed to pay",command=message,height=2,width=30,bg="light blue")
                b.place(x=250,y=400)
                
        Button(win,text="Continue",command=paying,height=2,width=30,bg="yellow").place(x=730,y=620)
    
        
        
def message():
    a=ent3.get()
    b=ent4.get()
    c=cal.get_date()
    d=ent5.get()
    if a=='' or b=='' or c=='' or d=='':
        messagebox.showerror("Invalid","Enter all details")
    elif len(a)>16 or len(a)<16 or a.isdigit()!=True:
        messagebox.showerror("Invalid","Enter right Card No")
    elif b.isalpha()!=True:
        messagebox.showerror("Invalid","Enter right Name")
    elif len(d)>3 or len(d)<3:
        messagebox.showerror("Invalid","Enter right CVV")
    else:
        m=messagebox.askquestion("Success","Ticket Booked Sucessfully.Do you want to view your ticket?")
                
        if m=="yes":
            ticket=Toplevel()
            ticket.title("Ticket")
            ticket.geometry("500x250")
            ticket.config(bg="light blue")
            l1=Label(ticket,text="PASSENGER TICKET",font=("Constantia",10,"bold"),bg="red",fg="white")
            l1.place(width=500)
            l2=Label(ticket,bg="orange")
            l2.place(y=25,width=500,height=5)
            l3=Label(ticket,text="DATE",font=("Constantia",12,"bold"),bg="light blue")
            l3.place(y=40)
            l33=Label(ticket,text=cal.get_date(),font=("Constantia",12),bg="light blue")
            l33.place(x=70,y=40)
            l4=Label(ticket,text="SEAT",font=("Constantia",12,"bold"),bg="light blue")
            l4.place(y=75)
            l44=Label(ticket,text=e.get(),font=("Constantia",12),bg="light blue")
            l44.place(x=70,y=75)
            l5=Label(ticket,text="FROM",font=("Constantia",12,"bold"),bg="light blue")
            l5.place(y=110)
            l55=Label(ticket,text=e3.get(),font=("Constantia",12),bg="light blue")
            l55.place(x=70,y=110)
            l5=Label(ticket,text="To",font=("Constantia",12,"bold"),bg="light blue")
            l5.place(y=145)
            l55=Label(ticket,text=e4.get(),font=("Constantia",12),bg="light blue")
            l55.place(x=70,y=145)
            l6=Label(ticket,bg="orange")
            l6.place(y=200,width=500,height=5)
            l7=Label(ticket,text="BUS TICKET",font=("Constantia",15,"bold"),bg="red",fg="white")
            l7.place(y=208,width=500,height=43)

            global img4
            path4 = "C:\\Users\\aarav\\Downloads\\qr code.png"
            img4 = ImageTk.PhotoImage(Image.open(path4))
            pane4 = Label(ticket, image=img4)
            pane4.place(x=300,y=80)
           
            
            root.deiconify()
            b=Button(root,text="Login",command=Login,height=2,width=30,bg="white")
            b.place(x=1075,y=580)
            
        else:
                        
            root.deiconify()
            b=Button(root,text="Login",command=Login,height=2,width=30,bg="white")
            b.place(x=1075,y=580)
                       
                   
                       
        


    
def addbus():
    From=e3.get()
    To=e4.get()
    Bus=combo.get()
    date=cal.get_date()
    seat=e.get()
    name=entry2.get()
    email=entry5.get()
    phone=entry6.get()

  
    
    app=Tk()
    app.title('Bus reservation site')
    app.geometry("500x400")

    Label(app,text="Bus booked",font=("Montserrat",20,"bold")).place(x=10)
    Label(app,text="Bus",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(y=60)
    Label(app,text="Departure",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=300,y=60)
    Label(app,text="Arrival",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=700,y=60)
    Label(app,text="Date",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=1000,y=60)
    Label(app,text="Seat",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=1280,y=60)
    
   
    global l1
    global l2
    global l3
    global l4
    global l4
    global l5
    global l6
    global l7
    global l8
    l1=Label(app,text=Bus,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l1.place(y=100)
    l2=Label(app,text=From,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l2.place(x=300,y=100)
    l3=Label(app,text=To,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l3.place(x=700,y=100)
    l4=Label(app,text=date,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l4.place(x=1000,y=100)
    l5=Label(app,text=seat,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l5.place(x=1280,y=100) 
    

    Label(app,text="Passenger Details",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=500,y=300)

    Label(app,text="Name",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(y=350)
    Label(app,text="Email Id",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=300,y=350)
    Label(app,text="Phone No",font=("Montserrat",10),height=2,width=50,bg="black",fg="white").place(x=700,y=350)
    
    l6=Label(app,text=name,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l6.place(y=390)
    l7=Label(app,text=email,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l7.place(x=300,y=390)
    l8=Label(app,text=phone,font=("Montserrat",10),height=10,width=50,bg="light gray")
    l8.place(x=700,y=390)
    
    Button(app,text="Delete",command=deletebus,height=2,width=30).place(x=50,y=600)
    Button(app,text="Modify",command=modifybus,height=2,width=30).place(x=500,y=600)

def deletebus():
    root.withdraw()
    From=e3.get()
    To=e4.get()
    Bus=combo.get()
    date=cal.get_date()
    seat=e.get()
    name=entry2.get()
    email=entry5.get()
    phone=entry6.get()

    l1.config(text="")
    l2.config(text="")
    l3.config(text="")
    l4.config(text="")
    l5.config(text="")
    l6.config(text="")
    l7.config(text="")
    l8.config(text="")
   
     
    messagebox.showinfo("Booking Cancelled","Booking has been cancelled. Passenger has been notified.")
    app.destroy()
    book.destroy()
    win.destroy()
    bk.destroy()


def modifybus():
    root.withdraw()
    Bus=combo.get()
    date=cal.get_date()
    bus = askstring('Bus', 'Bus')
    Date = askstring('Date', 'Date in "YYYY-MM-DD"')
    l1.config(text=bus)
    l4.config(text=Date)
    messagebox.showinfo("Booking Modified","Booking has been modified. Passenger has been notified.")
    
def Login():
    app.withdraw()
    book.withdraw()
    win.withdraw()
    bk.withdraw()
    r.withdraw()
    
    uname=e1.get()
    password=e2.get()
    
    if uname=="" and password=="":
        messagebox.showinfo("Invalid","Please enter the  credentials")
    elif(uname=="Admin" and password=="Login"):
        messagebox.showinfo("Login Success","You have successfully logged in")
        addbus()
    else:
        messagebox.showerror("Invalid","Username/Password is incorrect")        

    
    










#__main__
        
root=Tk()

root.geometry("2000x1400")
picture=PhotoImage(file=r"C:\\Users\\aarav\\Desktop\\gh.png")
picture1=Label(root,image=picture)
picture1.pack(fill=Y,anchor=W)
root.title("BUS RESERVATION SYSTEM")



#Login Frame

Frame_login=Frame(root,bg="light blue")
Frame_login.place(x=970,y=150,height=550,width=450)

Label(root,text="Log In",font=("Algerian",30,"bold"),foreground="black",bg="light blue").place(x=1140,y=200)
Label(root,text="UserName",bg="light blue", font=("light blue",10)).place(x=1025,y=330)
Label(root,text="Password",bg="light blue", font=("light blue",10)).place(x=1020,y=430)

#Labels within login frame

e1=Entry(root,bg="white",font=("Montserrat",11)) 
e1.place(x=1015,y=350,height=40,width=350)

e2=Entry(root,bg="white",font=("Montserrat",11))
e2.place(x=1015,y=450,height=40,width=350)
e2.config(show="*")



b=Button(root,text="Login",state=DISABLED,height=2,width=30,bg="white")
b.place(x=1075,y=580)
Button(root,text="Continue as User",command=user,height=2,width=30,bg="white").place(x=1075,y=640)




























