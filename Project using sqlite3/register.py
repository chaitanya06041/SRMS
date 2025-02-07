from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import sqlite3
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Windeo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="light gray")
        #BG Image

        #Register
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1, text="Register Here",font=("times new roman" ,20, "bold"),bg="white", fg="green").place(x=50,y=30)


        #----------------------
       


        f_name=Label(frame1, text="First Name",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_fname.place(x=50,y=130,width=200)


        l_name=Label(frame1, text="Last Name",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_lname.place(x=370,y=130,width=200)

        #------------------
        contact=Label(frame1, text="Contact No.",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_contact.place(x=50,y=200,width=200)


        email=Label(frame1, text="Email",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_email.place(x=370,y=200,width=200)

        #------------------
        question=Label(frame1, text="Security Question",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman", 13),state='readonly',justify=CENTER)

        self.cmb_quest['values']=("Select","Your Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=200)
        self.cmb_quest.current(0)


        answer=Label(frame1, text="Answer",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_answer.place(x=370,y=270,width=200)


        #----------_________----------------
        password=Label(frame1, text="Password",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_password.place(x=50,y=340,width=200)


        cpassword=Label(frame1, text="Confirm password",font=("times new roman" ,15, "bold"),bg="white", fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman", 15),bg="light gray")
        self.txt_cpassword.place(x=370,y=340,width=200)



        #---------Terms-----------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",bg="white",font=("times new roman",12),variable=self.var_chk,onvalue=1,offvalue=0).place(x=50,y=380)

        #--------------------------
        btn_register=Button(frame1,text="REGISTER NOW",font=("times new roman",15,"bold"),cursor="hand2",command=self.register_data,bg="green",fg="white").place(x=50,y=420)

        btn_login=Button(frame1,text="LOGIN",font=("times new roman",15,"bold"),cursor="hand2",bg="blue",fg="white",command=self.login_window).place(x=300,y=420)
        #----------___________-----------

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
    
        
        
        
    def clear(self):
        self.txt_fname.delete(0,END)    
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" :
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password and Confrim Password should be same",parent=self.root) 
        elif self.var_chk.get()==0:
             messagebox.showerror("Error","Please Accept Terms & Conditions",parent=self.root) 
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("Select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()

                if row!=None:
                    messagebox.showerror("Error","User Already Exist, Try With Another Email",parent=self.root)
                else:

                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmb_quest.get(),
                        self.txt_answer.get(),
                        self.txt_password.get()
                        ))
                    con.commit()
                    con.close()
                
                    messagebox.showinfo("Success","Register Successful",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
             

              
             










root=Tk()
obj=Register(root)
root.mainloop()
        