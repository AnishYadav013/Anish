from tkinter import *
import datetime

root0 = Tk()
root0.geometry('700x700')
root0.title("Parking System")
root0.configure(background="white")
photo = PhotoImage(file="images.png")
label = Label(root0, image = photo)
label.pack()
l0 = Label(root0,text="CAR PARK",font=("bold", 30))
l0.place(x=245,y=260)
l0.config(bg="white")

def tkexit0():
    root0.destroy()

def login():
    root1 = Tk()
    root1.geometry('700x700')
    root1.title("CAR PARK/Home")
    l0 = Label(root1,text="CAR PARK",font=("bold", 30))
    l0.place(x=245,y=70)

    l1 = Label(root1,text="To register a vehicle:-PRESS INSERT",font=("bold", 15))
    l1.place(x=180,y=180)

    l2 = Label(root1,text="To check-out a vehicle:-PRESS DELETE",font=("bold", 15))
    l2.place(x=165,y=280)

    l3 = Label(root1,text="To see all vehicle records:-PRESS RECORDS",font=("bold", 15))
    l3.place(x=145,y=380)

    def tkexit1():
        root1.destroy()

    Button(root1,text="INSERT",width=10,bg='brown',fg='white',command=insert).place(x=110,y=500)
    Button(root1,text="CHECK-OUT",width=10,bg='brown',fg='white',command=delete).place(x=310,y=500)
    Button(root1,text="RECORDS",width=10,bg='brown',fg='white',command=records).place(x=510,y=500)
    Button(root1,text="EXIT",width=10,bg='brown',fg='white',command=tkexit1).place(x=310,y=570)

def insert():
    root2 = Tk()
    root2.geometry('700x700')
    root2.title("CAR PARK/Register")
    l0 = Label(root2,text="CAR PARK",font=("bold", 30))
    l0.place(x=245,y=70)
    
    a = 0
    l = ["Enter Car No.:","Enter Owner's Name:"]
    for i in range(0,2):
        li = Label(root2,text=l[i],width=40,font=("bold",12))
        li.place(x=30,y=180+a)
        a = a+60

    e1 = Entry(root2)
    e1.place(x=370,y=180)

    e2 = Entry(root2)
    e2.place(x=370,y=240,width=250)

    def tkexit2():
        root2.destroy()

    def insertDB():
        f = open("park.txt","a")
        date = str((datetime.datetime.now()).strftime("%Y-%m-%d    %H:%M:%S"))+"    \n"
        l=[str(e1.get())+"    ",str(e2.get())+"    ",date]
        f.writelines(l)
        f.close()
        l0 = Label(root2,text="Registered",width=20,font=("bold", 20))
        l0.place(x=185,y=450)

    Button(root2,text="SUBMIT",width=15,bg='brown',fg='white',command=insertDB).place(x=292,y=590)
    Button(root2,text="EXIT",width=10,bg='brown',fg='white',command=tkexit2).place(x=310,y=630)  

def delete():    
    root3 = Tk()
    root3.geometry('700x700')
    root3.title("CAR PARK/Check Out")
    l0 = Label(root3,text="CAR PARK",font=("bold", 30))
    l0.place(x=245,y=70)

    l1 = Label(root3,text="Enter Car No.:",width=55,font=("bold", 12))
    l1.place(x=30,y=180)
    e1 = Entry(root3)
    e1.place(x=370,y=180)

    def tkexit3():
        root3.destroy()

    def deleteDB():
        c=int(0)
        f=open("park.txt", "r")
        lines = f.readlines()
        f.close()
        car_no = str(e1.get())
        f=open("park.txt", "w")
        for i in lines:
            a=i.split("    ")
            if a[0] == car_no:
                l0 = Label(root3,text="Checked Out",width=20,font=("bold", 20))
                l0.place(x=185,y=450)
            elif a[0] != car_no:
                f.write(i)
                c+=1
            if(len(lines)==c):
                    l1 = Label(root3,text="Not Found",width=20,font=("bold", 20))
                    l1.place(x=185,y=450)
        f.close()

    Button(root3,text="SUBMIT",width=15,bg='brown',fg='white',command=deleteDB).place(x=292,y=590)
    Button(root3,text="EXIT",width=10,bg='brown',fg='white',command=tkexit3).place(x=310,y=630)
            
def records():
    root4 = Tk()
    root4.geometry('700x700')
    root4.title("CAR PARK/Records")
    l0 = Label(root4,text="CAR PARK",font=("bold", 30))
    l0.place(x=245,y=70)

    a=0
    f = open("park.txt","r")
    while(1):
        line=f.readline()
        if line == "":
            break
        li=line.split("    ")
        la = Label(root4,text=li[0],width=10,font=("bold", 10),bg="white",height=1,anchor=N)
        la.place(x=75,y=120+a)
        lb = Label(root4,text=li[1],width=30,font=("bold", 10),bg="white",height=1,anchor=N)
        lb.place(x=185,y=120+a)
        lc = Label(root4,text=li[2]+"   "+li[3],width=20,font=("bold", 10),bg="white",height=1,anchor=N)
        lc.place(x=455,y=120+a)
        a = a+25
    f.close()
    def tkexit4():
        root4.destroy()
        
    Button(root4, text="EXIT",width=10,bg='brown',fg='white',command=tkexit4).place(x=310,y=630)

Button(root0,text="LOGIN",width=15,bg='brown',fg='white',command=login).place(x=295,y=500)        
Button(root0,text="EXIT",width=15,bg='brown',fg='white',command=tkexit0).place(x=295,y=550)

root0.mainloop()




