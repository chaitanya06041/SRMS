from tkinter import*
from PIL import Image,ImageTk
from Course import CourseClass
from Report import reportClass
from student import StudentClass
from result import resultClass
from tkinter import messagebox
import os
import sqlite3
import pymysql
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Students Result Management System")
        self.root.geometry("1350x700+50+50")
        self.root.config(bg="white")

        title=Label(self.root,text="Students Result Management System",font=("times new roman",20,"bold","italic"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50) 
        #menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)
        btn_course=Button(M_Frame,text="Course", font=("calibri",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student", font=("calibri",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result", font=("calibri",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result", font=("calibri",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout", font=("calibri",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit", font=("calibri",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)
        
        

        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("calibri",20),bg="orange",fg="black", bd=10, relief=RIDGE)
        self.lbl_course.place(x=180,y=530,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("calibri",20),bg="blue", fg="black",bd=10, relief=RIDGE)
        self.lbl_student.place(x=510,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("calibri",20),fg="black",bg="green", bd=10, relief=RIDGE)
        self.lbl_result.place(x=840,y=530,width=300,height=100)

        #Content Window
        self.bg_img=Image.open("IMAGE/bg.jpeg")     
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=215,y=180,width=920,height=350)
        self.update_details()

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
           
    def update_details(self):
        con=pymysql.connect(host="localhost",user="root",database="employee2")
        cur=con.cursor()
        try:
            cur.execute("select * from coursetable_2 ")
            rows=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(rows))}]") 

            cur.execute("select * from student_table_2 ")
            rows=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(rows))}]") 

            cur.execute("select * from result_t ")
            rows=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(rows))}]") 
            
            




            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")




    
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
    