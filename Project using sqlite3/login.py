from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import sqlite3
import os

class loginClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Windeo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="light gray")

        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)


        title=Label(login_frame,text="Login Here",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="Email Adress",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)

        self.txt_email=Entry(login_frame,font=("times new roman",18,"bold"),bg="lightgray",fg="black")
        self.txt_email.place(x=250,y=180,width=350,height=35)
           

        pass_=Label(login_frame,text="Password",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)

        self.txt_pass=Entry(login_frame,font=("times new roman",18,"bold"),bg="lightgray",fg="black")
        self.txt_pass.place(x=250,y=280,width=350,height=35)


        btn_reg=Button(login_frame,text="Register Here",font=("times new roman",14),bg="white",bd=0,fg="#B00857",command=self.register_window,cursor="hand2").place(x=250,y=350)

        btn_login=Button(login_frame,text="Login",font=("times new roman",14,"bold"),fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=400,y=350,width=150,height=40)

    def register_window(self):
        self.root.destroy()
        import register
    

    def login(self):
        if self.txt_email.get()==""or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid Email & Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    os.system("python Dashboard.py")
                    
                con.close()

                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)    

                          
                 
              


                




root=Tk()
obj=loginClass(root)
root.mainloop()