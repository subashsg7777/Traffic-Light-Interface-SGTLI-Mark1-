import tkinter 
import time
import sys
import random

'''def close():
    print("Quit")
    sys.exit()'''
dash = tkinter.Tk()
dash.geometry("400x400")
dash.config(bg="white")
dash.title("SGTraffic Light Interface(Mark 1)")
#dash.bind("<Left>",close)
canvas = tkinter.Canvas(dash,width=400,height=400,background="white")
#canvas.create_rectangle(0,150,200,250,fill="white")
canvas.create_rectangle(150,0,200,250,fill="black")
canvas.create_rectangle(200,150,400,250,fill="black")
canvas.create_rectangle(150,200,200,500,fill="black")
#lights for road A
ar = canvas.create_oval(80,80,120,120)
ay = canvas.create_oval(80,40,120,80)
ag = canvas.create_oval(80,0,120,40)
# lights for road C 350
cr = canvas.create_oval(80,260,120,300)
cy =canvas.create_oval(80,340,120,300)
cg = canvas.create_oval(80,380,120,340)
#lights for road B
br = canvas.create_oval(220,80,260,120)
by = canvas.create_oval(260,80,300,120)
bg = canvas.create_oval(300,80,340,120)
#Generative Buttons 
#road A
ab = canvas.create_rectangle(0,125,120,160,fill="green")
canvas.create_text(65,135,text="Generate Vechicle !..",fill="black")
#Road C
cb = canvas.create_rectangle(250,80,350,40,fill="green")
canvas.create_text(305,60,text="Generate Vechicle !..",fill="black")
#Road B
bb = canvas.create_rectangle(270,325,375,300,fill="green")
canvas.create_text(320,310,text="Generate Vechicle !..",fill="black")

def Generatea(event):
    print("Pressing !..")
    front = "TN63CW"
    number = random.randint(1000,9999)
    vn = front+str(number)
    print("Vechicle Number :",vn)
    color = canvas.itemcget(ar,"fill")
    gcolor = canvas.itemcget(ag,"fill")
    print("red : "+color)
    print("green : "+gcolor)
    if (color == "white" and gcolor == ""):
        print("Challan Created for Vechicle Number :"+vn)

def Generateb(event):
    print("Pressing !..")
    front = "TN63CW"
    number = random.randint(1000,9999)
    vn = front+str(number)
    print("Vechicle Number :",vn)
    color2 = canvas.itemcget(br,"fill")
    gcolor2 = canvas.itemcget(bg,"fill")
    print("red : "+color2)
    print("green : "+gcolor2)
    if (color2 == "white" and gcolor2 == ""):
        print("Challan Created for Vechicle Number :"+vn)

def Generatec(event):
    print("Pressing !..")
    front = "TN63CW"
    number = random.randint(1000,9999)
    vn = front+str(number)
    print("Vechicle Number :",vn)
    color3 = canvas.itemcget(cr,"fill")
    gcolor3 = canvas.itemcget(cg,"fill")
    print("red : "+color3)
    print("green : "+gcolor3)
    if (color3 == "white" and gcolor3 == ""):
        print("Challan Created for Vechicle Number :"+vn)

#binding road Generator to keyboard
dash.bind("<KeyPress-a>",Generatea)
dash.bind("<KeyPress-b>",Generateb)
dash.bind("<KeyPress-c>",Generatec)

def signaling():
    dash.update()
    print("Working !...")
    #initial configuration 
    canvas.itemconfig(ar,fill="red")
    canvas.itemconfig(br,fill="green")
    canvas.itemconfig(cr,fill="green")
    dash.update()
    st = time.monotonic()
    while True:
        ct = time.monotonic()
        et = ct-st
        if et >= 30:
            break
        #marking road a with yellow signal and turning of red 
    canvas.itemconfig(ar,fill="white")
    canvas.itemconfig(ay,fill="yellow")
    dash.update()
    st2 = time.monotonic()
    while True:
        ct2 = time.monotonic()
        et2 = ct2-st2
        if et2 >= 10:
            break
    #changing to green in road A and Red to road B
    canvas.itemconfig(ay,fill="white")
    canvas.itemconfig(ag,fill="green")
    canvas.itemconfig(br,fill="red")
    canvas.itemconfig(cr,fill="green")
    dash.update()
    st3 = time.monotonic()
    while True:
        ct3 = time.monotonic()
        et3 = ct3-st3
        if et3 >= 30:
            break
        #changing the yellow sign for Road B
    canvas.itemconfig(br,fill="white")
    canvas.itemconfig(by,fill="yellow")
    dash.update()
    st4 = time.monotonic()
    while True:
        ct4 = time.monotonic()
        et4 = ct4-st4
        if et4 >= 10:
            break
    #greening the Road B and turnig on the red in Road C
    canvas.itemconfig(br,fill="white")
    canvas.itemconfig(by,fill="white")
    canvas.itemconfig(bg,fill="green")
    canvas.itemconfig(cr,fill="red")
    dash.update()
    st5 = time.monotonic()
    while True:
        ct5 = time.monotonic()
        et5 = ct5 - st5
        if et5 >= 30:
            break
        #waiting for yellow signal of Road C
    canvas.itemconfig(cr,fill="white")
    canvas.itemconfig(cy,fill="yellow")
    dash.update()
    st6 = time.monotonic()
    while True:
        ct6 = time.monotonic()
        et6 = ct6 - st6
        if et6 >= 10:
            break
    #turning the last singnal on (Green)
    canvas.itemconfig(cr,fill="white")
    canvas.itemconfig(cy,fill="white")
    canvas.itemconfig(cg,fill="green")
    dash.update()
    st7 = time.monotonic()
    while True:
        ct7 = time.monotonic()
        et7 = ct7 - st7
        if  et7 >= 30:
            break
        #waring yellow for C
    canvas.itemconfig(cy,fill="yellow")
    dash.update()
    st8 = time.monotonic()
    while True:
        ct8 = time.monotonic()
        et8 = ct8 - st8
        if et8 >= 10:
            break
    #setting all for default
    canvas.itemconfig(br,fill="white")
    canvas.itemconfig(by,fill="white")
    canvas.itemconfig(bg,fill="white")
    canvas.itemconfig(ar,fill="white")
    canvas.itemconfig(ay,fill="white")
    canvas.itemconfig(ag,fill="white")
    canvas.itemconfig(cr,fill="white")
    canvas.itemconfig(cy,fill="white")
    canvas.itemconfig(cg,fill="white")
    dash.update()
    st9 = time.monotonic()
    while True:
        ct9 = time.monotonic()
        et9 = ct9 - st9
        if et9 >= 2:
            break
canvas.pack()
while True:
    signaling()
