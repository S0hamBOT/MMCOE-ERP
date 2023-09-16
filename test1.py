from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkdocviewer import *

root=Tk()
root.title("Krsna❤️Softwares")
icon=PhotoImage(file="iconphoto.png")
root.iconphoto(False,icon)
root.state("zoomed")
root.configure(bg="white")


#Image Logic Sarts

image1=(Image.open("mmcoe.png"))
resized_image1=image1.resize((250,250))
new_image1=ImageTk.PhotoImage(resized_image1)


#Image Logic Ends

#Frame Logic Starts

def showframe(frame):
    frame.tkraise()

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

frame1=LabelFrame(root,bg="white")
frame2=LabelFrame(root,bg="white")
frame3=LabelFrame(root,bg="#1D7C8F")
frame4=LabelFrame(root,bg="#1D7C8F")
frame5=LabelFrame(root,bg="#1D7C8F")
frame6=LabelFrame(root,bg="#1D7C8F")
frame7=LabelFrame(root,bg="#1D7C8F")
frame8=LabelFrame(root,bg="white")
frame9=LabelFrame(root,bg="#1D7C8F")
frame10=LabelFrame(root,bg="#1D7C8F")
frame11=LabelFrame(root,bg="#1D7C8F")
frame12=LabelFrame(root,bg="#1D7C8F")
frame13=LabelFrame(root,bg="#1D7C8F")
frame14=LabelFrame(root,bg="white")
frame15=LabelFrame(root,bg="#1D7C8F")
frame16=LabelFrame(root,bg="#1D7C8F")
frame17=LabelFrame(root,bg="#1D7C8F")
frame18=LabelFrame(root,bg="#1D7C8F")
frame19=LabelFrame(root,bg="#1D7C8F")


for frame in(frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10,frame11,frame12,frame13,frame14,frame15,frame16,frame17,frame18,frame19):
    frame.grid(row=0,column=0,sticky=NSEW)



#Frame Logic Ends
#soham-01FECO223121
#Button Logic Starts

def submit():
    var1=uservalue_entry.get()
    var2=passvalue_entry.get()

    if(var1=="a" and var2=="a"):
        showframe(frame2)
    elif(var1=="b" and var2=="b"):
        showframe(frame8)
    elif(var1=="c" and var2=="c"):
        showframe(frame14)
    else:
        messagebox.showerror("Error","Wrong Username Or Password")
    uservalue_entry.delete(0,END)
    passvalue_entry.delete(0,END)

def quit_click():
    showframe(frame1)

#Button Logic Ends








#CODE FOR 1st PAGE STARTS

title = Label(frame1,text="MMCOE",fg="red",font="raleway 60 bold",bg="white")
title.place(x=600,y=70)

motto = Label(frame1,text='“येथे बहुतांचे हित”',fg="black",font="comicsansms 20 bold ",bg="white")
motto.place(x=650,y=166)

label1=Label(frame1,text="MMCOE ERP",fg="grey",font="timesnewroman 25 bold",borderwidth=2,relief=GROOVE)
label1.place(x=650,y=300)

label2=Label(frame1,text="Username :",bg="white",font="raleway 15 bold")
label2.place(x=620,y=400)

label3=Label(frame1,text="Password :",bg="white",font="raleway 15 bold")
label3.place(x=620,y=430)

uservalue=StringVar()
passvalue=StringVar()

uservalue_entry=Entry(frame1,textvariable=uservalue)
uservalue_entry.place(x=750,y=408)
passvalue_entry=Entry(frame1,textvariable=passvalue)
passvalue_entry.place(x=750,y=433)

submit_btn=Button(frame1,text="Submit",relief=RAISED,command=submit,padx=5,pady=5)
submit_btn.place(x=730,y=480)

quit_btn=Button(frame1,text="Quit",relief=RAISED,command=quit,padx=5,pady=5)
quit_btn.place(x=735,y=680)

label4 = Label(frame1,text = "Copyright©️2023 Krsna \n All Rights Reserved",bg="white")
label4.place(x=690,y=750)

#CODE FOR 1st PAGE ENDS




'''When username=a and password=a'''

#CODE FOR 2nd PAGE STARTS

def frame3_quit():
    showframe(frame2)

name_lbl1=Label(frame2,text="Soham Jadhav\n+91 12345 67890",fg="red",font="raleway 10 bold")
name_lbl1.place(x=1425,y=5)


   #Account Details Starts

def account_a():
    showframe(frame3)


photo1=ImageTk.PhotoImage(file="boyaccount.png")
lbl=Label(frame2,image=photo1,bg="white")
lbl.place(x=100,y=50)
photo1_btn=Button(frame2,text="Account",font="bold",padx=5,pady=5,command=account_a)
photo1_btn.place(x=185,y=320)

          # CODE FOR FRAME3 STARTS
          
label5=Label(frame3,text="Name       : Soham Gopalkrishna Jadhav",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label5.place(x=100,y=50)

label6=Label(frame3,text="Address   : MMCOE, Pune",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label6.place(x=100,y=100)

label7=Label(frame3,text="Contact    : +91 1234567890",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label7.place(x=100,y=150)

label8=Label(frame3,text="Branch     : Computer Science",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label8.place(x=100,y=200)

label9=Label(frame3,text="Roll No.    : F22C20",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label9.place(x=100,y=250)

label10=Label(frame3,text="CPRN       : 01FECO223121",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label10.place(x=100,y=300)

soham_image=PhotoImage(file="soham.png")
sohamphotolabel=Label(frame3,image=soham_image,bg="#1D7C8F")
sohamphotolabel.place(x=1100,y=10)

account_quit=Button(frame3,text="Back",padx=5,pady=10,command=frame3_quit)
account_quit.place(x=720,y=650)

          # CODE FOR FRAME3 ENDS

   #Account Details End
   
   #Notes Details Start

photo2=ImageTk.PhotoImage(file="notes.png")
lbl=Label(frame2,image=photo2,bg="white")
lbl.place(x=600,y=50)
photo2_btn=Button(frame2,text="Notes",font="bold",padx=5,pady=5)
photo2_btn.place(x=700,y=320)
 
          #CODE FOR FRAME4 STARTS

'''# Create a root window
root = Tk()

# Create a DocViewer widget
v = DocViewer(root)
v.pack(side="top", expand=1, fill="both")

# Display some document
v.display_file("example.pdf")'''

v=DocViewer(frame4)
v.place(x=25,y=25)

v.display_file("syllabus.pdf")


          #CODE FOR FRAME4 ENDS
          
   #Notes Details End
   #Assignment Details Start

def assign_click():
    showframe(frame5)

photo3=ImageTk.PhotoImage(file="assignment.png")
lbl=Label(frame2,image=photo3,bg="white")
lbl.place(x=1100,y=50)
photo3_btn=Button(frame2,text="Assignment",font="bold",padx=5,pady=5,command=assign_click)
photo3_btn.place(x=1180,y=320)


          #CODE FOR FRAME5 STARTS

assignment_quit=Button(frame5,text="Back",padx=5,pady=5,command=frame3_quit)
assignment_quit.place(x=720,y=650)

lbl=Label(frame5,text="To be submitted as early as possible...",font="raleway 20 italic",bg="#1D7C8F")
lbl.place(x=50,y=50)



          #CODE FOR FRAME5 ENDS
   #Assignment Details End

   #Performance Details Start

def performance_click():
    showframe(frame6)

photo4=ImageTk.PhotoImage(file="performance.png")
lbl=Label(frame2,image=photo4,bg="white")
lbl.place(x=100,y=450)
photo4_btn=Button(frame2,text="Performance",font="bold",padx=5,pady=5,command=performance_click)
photo4_btn.place(x=170,y=710)
          #CODE FOR FRAME6 STARTS

aunit1photo=ImageTk.PhotoImage(file="sohamperformance1.png")
lblu1=Label(frame6,image=aunit1photo)
lblu1.place(x=50,y=50)

lblu1text=Label(frame6,text="Unit 1",font="raleway 20 bold",bg="#1D7C8F")
lblu1text.place(x=200,y=380)

aunit2photo=ImageTk.PhotoImage(file="sohamperformance.png")
lblu2=Label(frame6,image=aunit2photo)
lblu2.place(x=550,y=50)

lblu2text=Label(frame6,text="Unit 2",font="raleway 20 bold",bg="#1D7C8F")
lblu2text.place(x=700,y=380)

performance_quit=Button(frame6,text="Back",padx=5,pady=5,command=frame3_quit)
performance_quit.place(x=720,y=650)

lblu3text=Label(frame6,text="Unit 3",font="raleway 20 bold",bg="#1D7C8F")
lblu3text.place(x=1200,y=380)

lblu3_text=Label(frame6,text="To Be Added Soon",font="raleway 15 italic",bg="#1D7C8F")
lblu3_text.place(x=1150,y=190)

          #CODE FOR FRAME6 ENDS


   #Performance Details End

   #Discussion Details Starts

def discussion_click():
    showframe(frame7)

photo5=ImageTk.PhotoImage(file="discussion.png")
lbl=Label(frame2,image=photo5,bg="white")
lbl.place(x=580,y=450)
photo5_btn=Button(frame2,text="Discussion",font="bold",padx=5,pady=5,command=discussion_click)
photo5_btn.place(x=680,y=710)
          #CODE FOR FRAME7 STARTS

discussion_quit=Button(frame7,text="Back",padx=5,pady=5,command=frame3_quit)
discussion_quit.place(x=720,y=650)

lbl=Label(frame7,text="Connecting to the server...",font="raleway 20 italic",bg="#1D7C8F")
lbl.place(x=50,y=50)

          #CODE FOR FRAME7 ENDS
   #Discussion Details End
 
photo6=PhotoImage(file="exit.png")
exit_btn=Button(frame2,command=quit_click,padx=5,pady=5,image=photo6)
exit_btn.place(x=1100,y=450)

#CODE FOR 2nd PAGE ENDS



'''When username=b and password=b'''

#CODE FOR 2nd PAGE STARTS

def frame9_quit():
    showframe(frame8)

name_lbl2=Label(frame8,text="Samyak Waikar\n+91 12345 67890",fg="red",font="raleway 10 bold")
name_lbl2.place(x=1420,y=5)

    #Account Details Start

def bacc_click():
    showframe(frame9)

b_photo1=ImageTk.PhotoImage(file="boyaccount.png")
lbl=Label(frame8,image=b_photo1,bg="white")
lbl.place(x=100,y=50)
b_photo1_btn=Button(frame8,text="Account",font="bold",padx=5,pady=5,command=bacc_click)
b_photo1_btn.place(x=185,y=320)

        #CODE FOR FRAME9 STARTS

label5=Label(frame9,text="Name       : Samyak Waikar",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label5.place(x=100,y=50)

label6=Label(frame9,text="Address   : MMCOE, Pune",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label6.place(x=100,y=100)

label7=Label(frame9,text="Contact    : +91 1234567890",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label7.place(x=100,y=150)

label8=Label(frame9,text="Branch     : Computer Science",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label8.place(x=100,y=200)

label9=Label(frame9,text="Roll No.    : F22C64",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label9.place(x=100,y=250)

label10=Label(frame9,text="CPRN       : ***",padx=5,pady=10,font="cambria 20 bold",bg="#1D7C8F")
label10.place(x=100,y=300)

sanica_image=PhotoImage(file="samyak.png")
sanicaphotolabel=Label(frame9,image=sanica_image,bg="#1D7C8F")
sanicaphotolabel.place(x=1080,y=10)

baccount_quit=Button(frame9,text="Back",padx=5,pady=10,command=frame9_quit)
baccount_quit.place(x=720,y=650)


        #CODE FOR FRAME9 ENDS

    #Account Details End

b_photo2=ImageTk.PhotoImage(file="notes1.png")
lbl=Label(frame8,image=b_photo2,bg="white")
lbl.place(x=600,y=50)
b_photo2_btn=Button(frame8,text="Notes",font="bold",padx=5,pady=5)
b_photo2_btn.place(x=700,y=320)

b_photo3=ImageTk.PhotoImage(file="assignment1.png")
lbl=Label(frame8,image=b_photo3,bg="white")
lbl.place(x=1100,y=50)
b_photo3_btn=Button(frame8,text="Assignment",font="bold",padx=5,pady=5)
b_photo3_btn.place(x=1180,y=320)

b_photo4=ImageTk.PhotoImage(file="performance1.png")
lbl=Label(frame8,image=b_photo4,bg="white")
lbl.place(x=100,y=450)
b_photo4_btn=Button(frame8,text="Performance",font="bold",padx=5,pady=5)
b_photo4_btn.place(x=170,y=710)

b_photo5=ImageTk.PhotoImage(file="discussion1.png")
lbl=Label(frame8,image=b_photo5,bg="white")
lbl.place(x=580,y=450)
b_photo5_btn=Button(frame8,text="Discussion",font="bold",padx=5,pady=5)
b_photo5_btn.place(x=680,y=710)

b_photo6=PhotoImage(file="exit.png")
bexit_btn=Button(frame8,command=quit_click,padx=5,pady=5,image=b_photo6)
bexit_btn.place(x=1100,y=450)

#CODE FOR 2nd PAGE ENDS


'''when username=c n password=c'''
#CODE FOR 2nd PAGE STARTS

def frame15_quit():
    showframe(frame14)

name_lbl3=Label(frame14,text="Atharva Landge\n+91 12345 67890",fg="red",font="raleway 10 bold")
name_lbl3.place(x=1425,y=5)

    #Account Details Start

def account_c():
    showframe(frame15)

c_photo1=ImageTk.PhotoImage(file="boyaccount.png")
lbl=Label(frame14,image=c_photo1,bg="white")
lbl.place(x=100,y=50)
c_photo1_btn=Button(frame14,text="Account",font="bold",padx=5,pady=5,command=account_c)
c_photo1_btn.place(x=185,y=320)

            #CODE FOR FRAME15 STARTS

label11=Label(frame15,text="Name       : Atharva Landge",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label11.place(x=100,y=50)

label12=Label(frame15,text="Address   : MMCOE, Pune",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label12.place(x=100,y=100)

label13=Label(frame15,text="Contact    : +91 1234567890",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label13.place(x=100,y=150)

label14=Label(frame15,text="Branch     : Computer Science",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label14.place(x=100,y=200)

label15=Label(frame15,text="Roll No.    : F22C29",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label15.place(x=100,y=250)

label16=Label(frame15,text="CPRN       : 01FECO221023",padx=5,pady=10,font="raleway 20 bold",bg="#1D7C8F")
label16.place(x=100,y=300)

atharva_image=PhotoImage(file="atharva.png")
atharvaphotolabel=Label(frame15,image=atharva_image,bg="#1D7C8F")
atharvaphotolabel.place(x=1035,y=10)

caccount_quit=Button(frame15,text="Back",padx=5,pady=10,command=frame15_quit)
caccount_quit.place(x=720,y=650)

            #CODE FOR FRAME15 ENDS

    #Account Details End

    #Notes Details Start

c_photo2=ImageTk.PhotoImage(file="notes.png")
lbl=Label(frame14,image=b_photo2,bg="white")
lbl.place(x=600,y=50)
c_photo2_btn=Button(frame14,text="Notes",font="bold",padx=5,pady=5)
c_photo2_btn.place(x=700,y=320)

            #CODE FOR FRAME16 STARTS



            #CODE FOR FRAME16 ENDS

    #Notes Details End

    #Assignment Details Sarts

def cassign_click():
    showframe(frame17)

c_photo3=ImageTk.PhotoImage(file="assignment.png")
lbl=Label(frame14,image=b_photo3,bg="white")
lbl.place(x=1100,y=50)
c_photo3_btn=Button(frame14,text="Assignment",font="bold",padx=5,pady=5,command=cassign_click)
c_photo3_btn.place(x=1180,y=320)

            #CODE FOR FRAME17 STARTS

assignment_quit=Button(frame17,text="Back",padx=5,pady=5,command=frame15_quit)
assignment_quit.place(x=720,y=650)

lbl=Label(frame17,text="To be submitted as early as possible...",font="raleway 20 italic",bg="#1D7C8F")
lbl.place(x=50,y=50)

            #CODE FOR FRAME17 ENDS

    #Assignment Details End


    #Performance Details Start

def cperfor_click():
    showframe(frame18)

c_photo4=ImageTk.PhotoImage(file="performance.png")
lbl=Label(frame14,image=b_photo4,bg="white")
lbl.place(x=100,y=450)
c_photo4_btn=Button(frame14,text="Performance",font="bold",padx=5,pady=5,command=cperfor_click)
c_photo4_btn.place(x=170,y=710)

            #CODE FOR FRAME18 STARTS

cunit1photo=ImageTk.PhotoImage(file="sohamperformance2.png")
lblu1=Label(frame18,image=cunit1photo)
lblu1.place(x=50,y=50)

lblu1text=Label(frame18,text="Unit 1",font="raleway 20 bold",bg="#1D7C8F")
lblu1text.place(x=200,y=380)

cunit2photo=ImageTk.PhotoImage(file="sohamperformance3.png")
lblu2=Label(frame18,image=cunit2photo)
lblu2.place(x=550,y=50)

lblu2text=Label(frame18,text="Unit 2",font="raleway 20 bold",bg="#1D7C8F")
lblu2text.place(x=700,y=380)

cperformance_quit=Button(frame18,text="Back",padx=5,pady=5,command=frame15_quit)
cperformance_quit.place(x=720,y=650)

lblu3text=Label(frame18,text="Unit 3",font="raleway 20 bold",bg="#1D7C8F")
lblu3text.place(x=1200,y=380)

lblu3_text=Label(frame18,text="To Be Added Soon",font="raleway 15 italic",bg="#1D7C8F")
lblu3_text.place(x=1150,y=190)

            #CODE FOR FRAME18 ENDS

    #Peformance Details End
    
    #Discussion Details Start
def cdisc_click():
    showframe(frame19)
c_photo5=ImageTk.PhotoImage(file="discussion.png")
lbl=Label(frame14,image=b_photo5,bg="white")
lbl.place(x=580,y=450)
c_photo5_btn=Button(frame14,text="Discussion",font="bold",padx=5,pady=5,command=cdisc_click)
c_photo5_btn.place(x=680,y=710)

            #CODE FOR FRAME19 STARTS

cdiscussion_quit=Button(frame19,text="Back",padx=5,pady=5,command=frame15_quit)
cdiscussion_quit.place(x=720,y=650)

lbl=Label(frame19,text="Connecting to the server...",font="raleway 20 italic",bg="#1D7C8F")
lbl.place(x=50,y=50)


            #CODE FOR FRAME19 ENDS

    #Discussion Details End
c_photo6=PhotoImage(file="exit.png")
exit_btn=Button(frame14,command=quit_click,padx=5,pady=5,image=c_photo6)
exit_btn.place(x=1100,y=450)



#CODE FOR 2nd PAGE ENDS




lbl=Label(frame1,image=new_image1,bg="white")                   #resized image placing
lbl.place(x=1250,y=10)                                          #resized image placing



showframe(frame1)

root.mainloop()