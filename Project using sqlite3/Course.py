from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Students Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()   

        #Title
        title=Label(self.root, text="Manage Course Details",font=("times new roman",20,"bold"), bg="#033054", fg="white")
        title.place(x=10,y=15,relwidth=1,height=35)

        #Variable
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()




        #widgets
        lbl_courseName=Label(self.root, text="Course Name", font=("times new roman",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root, text="Course Duration", font=("times new roman",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges=Label(self.root, text="Course Charges", font=("times new roman",15,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root, text="Course Description", font=("times new roman",15,"bold"),bg="white").place(x=10,y=180)

        #Entries
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,  font=("times new roman",15,"bold"),bg="#F0F0F0")
        self.txt_courseName.place(x=180,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,  font=("times new roman",15,"bold"),bg="#F0F0F0").place(x=180,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges, font=("times new roman",15,"bold"),bg="#F0F0F0").place(x=180,y=140,width=200)
        self.txt_description=Text(self.root,  font=("times new roman",15,"bold"),bg="#F0F0F0")
        self.txt_description.place(x=180,y=180, width=400,height=150)


        #buttons
        self.btn_add=Button(self.root,text="Save", font=("times new roman",15,"bold"), bg="#2196f3", fg="white",command=self.add,cursor="hand2")
        self.btn_add.place(x=150,y=400, width=110,height=40)
        self.btn_update=Button(self.root,text="Update", font=("times new roman",15,"bold"), bg="#4caf50", fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400, width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete", font=("times new roman",15,"bold"), bg="#f44336", fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400, width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear", font=("times new roman",15,"bold"), bg="#607d8b", fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400, width=110,height=40)


        #Search Panel
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root, text="Search by Course", font=("times new roman",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_course=Entry(self.root,textvariable=self.var_search ,font=("times new roman",15,"bold"),bg="#F0F0F0").place(x=880,y=60,width=180)

        btn_search=Button(self.root,text="Search", font=("times new roman",15,"bold"), bg="#03a9f4", fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=1070,y=60, width=120,height=28)

        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=728,y=100,width=460,height=340)


        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","Charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("Charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]="headings"
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("Charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
       
#-------------_________________________------------------        

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name is Required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully")
                    self.show()
                                         


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

            #________----------------------------_____________-
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name is Required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Updated Successfully")
                    self.show()
                                         


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
#_________________-------------------________________
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)      
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            #____________----------------------------__________
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)      
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name is Required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select Course ftom the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName

        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
    #self.var_course.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])


    def clear(self):
        self.show()
    
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        #self.var_course.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)
    


    
 
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()
