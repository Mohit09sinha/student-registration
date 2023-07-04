from pyclbr import Function
from tkinter import*
from tkinter import ttk
root=Tk()

root.title("Student Registration Form")
root.geometry("500x500+300+200")



# Function Declaration

def show_data():
    if check_var.get()=='ON' :
        get_data= f'Name:{name_var.get()}\nEmail:{email_var.get()}\nGender:{gender_var.get()}'
        out.config(text=get_data,font=('arial',17))       
    else:
        out.config(text="Please Accept our Terms And Conditions",font=('arial',18,'italic'))
    
        

title=Label(root,text="STUDENT ENTRY FORM",font=('times new roman',25,'bold'),fg='gold',bg='black')
title.pack()

frame=Frame(root,bd=3,relief=RIDGE,bg='grey')
frame.place(x=8,y=50,width=480,height=440)


name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
check_var=StringVar()


# Labels

name=Label(frame,text="Student Name",font=('arial',15,'bold'),width=14)
name.grid(row=0,column=0,padx=5,pady=10)

email=Label(frame,text="Student Email ID",font=('arial',15,'bold'),width=14)
email.grid(row=1,column=0,padx=5,pady=10)


gender=Label(frame,text="Gender",font=('arial',15,'bold'),width=14)
gender.grid(row=2,column=0,padx=5,pady=10,sticky=W)


# Radiobutton

male=Radiobutton(frame,variable=gender_var,text='Male',value='Male',font=('arial',14,'bold'),width=8)
male.grid(row=2,column=1,sticky=W)
gender_var.set('Male')

female=Radiobutton(frame,variable=gender_var,text='Female',value='Female',font=('arial',14,'bold'),width=8)
female.place(x=320,y=107)



# Checkbutton
check=Checkbutton(frame,variable=check_var,onvalue='ON',offvalue='OFF',text='Accept our Terms and Conditions',font=('arial',15,'bold'))
check.place(x=85,y=160)
check_var.set('OFF')


# Button

btn=Button(frame,command=show_data,text='Save Data',font=('arial',15,'bold'),width=14,bg='black',fg='white')
btn.place(x=170,y=213)



# Entry

namee=Entry(frame,textvariable=name_var,font=('arial',15,'bold'),width=25)
namee.grid(row=0,column=1,padx=5,pady=10)

emaile=Entry(frame,textvariable=email_var,font=('arial',15,'bold'),width=25)
emaile.grid(row=1,column=1,padx=5,pady=10)



frame1=Frame(root,bd=3,relief=RIDGE,bg='white')
frame1.place(x=18,y=330,width=460,height=150)

out=Label(frame1,text="",font=('arial',10,'bold'),justify='center')
out.grid(row=0,column=0,padx=5,pady=10)


root.mainloop()