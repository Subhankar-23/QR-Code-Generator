from logging import root
from tkinter import*
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
from turtle import title

class QR_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+250+55") #dimension of the window
        self.root.title("QR Code Generator | Subhankar") #title of the window
        self.root.resizable(False,False) #not to resize the window
        title=Label(self.root,text="QR Code Generator",font=("times new roman",39),bg='#053246',fg="white").place(x=0,y=0,relwidth=1)

#Employee Details Frame
#------Variables------
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_deg=StringVar()
        self.var_spz=StringVar()
        self.var_bld=StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_Frame.place(x=50,y=100,width=500,height=380)
        title=Label(emp_Frame,text="Student Details",font=("goudy old style",19),bg='#043256',fg="white").place(x=0,y=0,relwidth=1)
#details field
        lbl_emp_id=Label(emp_Frame,text="Enrollment No",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_emp_name=Label(emp_Frame,text="Full Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_emp_deg=Label(emp_Frame,text="Degree",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_emp_spz=Label(emp_Frame,text="Specialization",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        lbl_emp_bld=Label(emp_Frame,text="Blood Group",font=("times new roman",15,'bold'),bg='white').place(x=20,y=220)
#entry fields
        txt_emp_id=Entry(emp_Frame,font=("times new roman",14),textvariable=self.var_id,bg='#dbdeff').place(x=200,y=61)
        txt_emp_name=Entry(emp_Frame,font=("times new roman",14),textvariable=self.var_name,bg='#dbdeff').place(x=200,y=101)
        txt_emp_dept=Entry(emp_Frame,font=("times new roman",14),textvariable=self.var_deg,bg='#dbdeff').place(x=200,y=141)
        txt_emp_des=Entry(emp_Frame,font=("times new roman",14),textvariable=self.var_spz,bg='#dbdeff').place(x=200,y=181)
        txt_emp_bld=Entry(emp_Frame,font=("times new roman",14),textvariable=self.var_bld,bg='#dbdeff').place(x=200,y=221)
#buttons
        btn_generate=Button(emp_Frame,text="Generate QR",command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=80,y=280,width=190,height=30)
        btn_clear=Button(emp_Frame,text="Reset",command=self.clear,font=("times new roman",18,'bold'),bg='#5ABE3B',fg='white').place(x=290,y=280,width=130,height=30)
#Success Msg
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",16,'bold'),bg='white',fg='#5ABE3B')
        self.lbl_msg.place(x=0,y=320,relwidth=1)
#QR Code Frame
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=260,height=380)
        title=Label(qr_Frame,text="QR Code",font=("goudy old style",19),bg='#043256',fg="white").place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_Frame,text="QR Not\nAvailable",font=("times new roman",13),bg='#23293d',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=40,y=90,height=180,width=180)
        btn_clear=Button(qr_Frame,text="Download",font=("times new roman",17,'bold'),bg='#5ABE3B',fg='white').place(x=50,y=300,width=160,height=30)

#functions
    def generate(self):
        if self.var_id.get()=='' or self.var_name.get()=='' or self.var_deg.get()=='' or self.var_spz.get()=='' or self.var_bld.get()=='':
                self.msg='All fields are required!'
                self.lbl_msg.config(text=self.msg,fg="red")
        else:
                qr_data=(f"Enrollment No: {self.var_id.get()}\nStudent Name: {self.var_name.get()}\nDegree: {self.var_deg.get()}\nSpecialization: {self.var_spz.get()}\nBlood Group: {self.var_bld.get()}")
                qr_code=qrcode.make(qr_data)

                #QR Code Image
                qr_code=resizeimage.resize_cover(qr_code,[180,180])  #to give a proper shape
                qr_code.save("D:\Python Programs\QR Code\QR_"+str(self.var_id.get())+'.png')
                self.im=ImageTk.PhotoImage(qr_code)
                self.qr_code.config(image=self.im)

                self.msg='QR Generated Successfully!!'
                self.lbl_msg.config(text=self.msg,fg="green")

    def clear(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_deg.set('')
        self.var_spz.set('')
        self.var_bld.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')



       
root=Tk()
obj=QR_generator(root)
root.mainloop()