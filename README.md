# Hospital-Management-System

import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def main():
       root = Tk()
       app = Windows1(root)
       root.mainloop()



class Windows1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('670x540+300+100')  # x-axis,y-axis,0,0 are location from top leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
        self.Username= StringVar()
        self.Password= StringVar()
        self.master.configure(background='black')
        self.master.resizable(False,False)




        self.LabelTitle = Label(self.frame, text="    Hospital Management System    ", font=("arial", 30, "bold"),
                                background="#4A646C",bd=10,  relief="sunken" )
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)



        self.loginframe1= Frame(self.frame, width=1000, height=300, bd=10, relief="groove", background="#C19A6B")
        self.loginframe1.grid(row=1, column=0)

        self.loginframe2 = Frame(self.frame, width=1000, height=100, bd=10, relief="groove", background="#C19A6B")
        self.loginframe2.grid(row=2, column=0, pady=15)

        self.loginframe3 = Frame(self.frame, width=1000, height=200, bd=10, relief="groove", background="#5F9EA0")
        self.loginframe3.grid(row=6, column=0, pady=5)

        self.button_reg= Button(self.loginframe3, text= "Patient Registration Window", state=DISABLED, background="#CD9575",font=("arial", 15,"bold"),
        command=self.Registration_window)
        self.button_reg.grid(row=0, column=0, padx=10, pady=10)

        self.button_Hos = Button(self.loginframe3, text="Hospital Management Window",state=DISABLED,background="#CD9575", font=("arial", 15, "bold"),
        command = self.Hospital_window)
        self.button_Hos.grid(row=0, column=1, padx=10, pady=10)


        self.button_Dr_appoint = Button(self.loginframe3, text="Doctor Management Window",state=DISABLED,background="#CD9575", font=("arial", 15, "bold"),
        command= self.dr_Appoint_window)
        self.button_Dr_appoint.grid(row=1, column=0, padx=10, pady=10)

        self.button_med_stock = Button(self.loginframe3, text="Medicine Stock Window",state=DISABLED, background="#CD9575",font=("arial", 15, "bold"),
        command = self.Medicine_stock)
        self.button_med_stock.grid(row=1, column=1, padx=10, pady=10)


        # now will be make user name and password


        self.LabelUsername= Label(self.loginframe1, text= "User Name", font=("arial", 20, "bold"),background="#C19A6B", bd=3)
        self.LabelUsername.grid(row=0, column=0)

        self.textUsername = Entry(self.loginframe1, font=("arial", 20, "bold"), bd=3, textvariable= self.Username)
        self.textUsername.grid(row=0, column=1, padx=40, pady=15)

        self.LabelPassword= Label(self.loginframe1, text= "Password", font=("arial", 20, "bold"),background="#C19A6B", bd=3)
        self.LabelPassword.grid(row=1, column=0)

        self.textPassword = Entry(self.loginframe1, font=("arial", 20, "bold"), show="*",bd=3, textvariable=self.Password)
        self.textPassword.grid(row=1, column=1, padx=40, pady=15)


        # we will make login logout reset button

        self.button_login= Button(self.loginframe2, text="Login", width=10,background="#FF1493", font=("arial", 18, "bold"),
                                 command=self.login_system )
        self.button_login.grid(row=0, column=0, padx=10, pady=10)

        self.button_reset = Button(self.loginframe2, text="Reset", width=10,background="#FF1493", font=("arial", 18, "bold"),
                                command=self.reset_btn )
        self.button_reset.grid(row=0, column=3, padx=10, pady=10)

        self.button_Exit = Button(self.loginframe2, text="Exit", width=10,background="#FF1493", font=("arial", 18, "bold"),
                                 command=self.exit_btn)
        self.button_Exit.grid(row=0, column=6, padx=10, pady=10)


    def login_system(self):
        user= self.Username.get()
        pswd= self.Password.get()




        if(user == str("admin") and (pswd ==str ("akr"))):
            self.button_reg.config(state=NORMAL)
            self.button_Hos.config(state=NORMAL)
            self.button_Dr_appoint.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)

        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "you have entered invalid username or password")
            self.button_reg.config(state=DISABLED)
            self.button_Hos.config(state=DISABLED)
            self.button_Dr_appoint.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)
            # if user name or password incorrect then it will be go its disabled state

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()



    def reset_btn(self):
            self.button_reg.config(state=DISABLED)
            self.button_Hos.config(state=DISABLED)
            self.button_Dr_appoint.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)


        # because when we will reset still we have not given correct user id and password

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def exit_btn(self):
        self.exit_btn= tkinter.messagebox.askyesno("Pharmacy management system", "Are you sure you want to exit?")
        if self.exit_btn>0:
            # we will close that master screen
           self.master.destroy()
           return





        # first we will define our window
    def Registration_window(self):
        self.newWindow= Toplevel(self.master)
        self.app= Registration(self.newWindow)




    def Hospital_window(self):
        self.newWindow= Toplevel(self.master)
        self.app=Hospital(self.newWindow)


    def dr_Appoint_window(self):
        self.newWindow= Toplevel(self.master)
        self.app=  Doctor(self.newWindow)


    def Medicine_stock(self):
        self.newWindow= Toplevel(self.master)
        self.app= Windows5(self.newWindow)





class Windows2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient management system")
        self.master.geometry('1350x750+0+0')  # x-axis,y-axis,0,0 are location from top leftmost
        self.frame = Frame(self.master)
        self.frame.pack()




class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration system ")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="black")


        # we will take live time date by using time module

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref= StringVar()
        Mobile_no= StringVar()
        Pincode= StringVar()
        Address= StringVar()
        Firstname= StringVar()
        Lastname= StringVar()

        ###### this var1,2,3,4,5 are for combobox
        var1= StringVar()
        var2= StringVar()
        var3= StringVar()
        var4= StringVar()
        var5= IntVar() # we will keep as int bcz we will keep here Numerical value

        Membership= StringVar()
        Membership.set("0") # when membership checkbox in unclicked or reset has done it will automatically


        ############# Functions ##############

        def exitbtt():
            exitbtt= tkinter.messagebox.askyesno("Member Registration Form","Are you sure want to exit?")
            if exitbtt>0:
                root.destroy()
                return

        def resetbtt():
            Firstname.set("")
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membership.grid(state=DISABLED)


        def reeesetbtt():
            reeesetbtt= tkinter.messagebox.askokcancel("Member Registration Form","You want to add new Record")
            if reeesetbtt>0:
                resetbtt()
            elif reeesetbtt<=0:
                resetbtt()
                detail_labeltxt.delete("1.0", END)

        def Reference_number():
            ranumber= random.randint(10000, 9999999)
            randomnumber= str(ranumber)
            Ref.set(randomnumber)


        def membership_fees():
            if(var5.get() == 1): # when checkbox is clicked
                member_membership.configure(state=NORMAL)
                item=float(1500) # it is random price of membership plan you can change according to you
                Membership.set(str(item)+"Rs")
            elif(var5.get() == 0):
                # when unchecked
                member_membership.configure(state=DISABLED)
                Membership.set("0")

        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END,"\t"+Date_of_Registration.get()+"  \t"+Ref.get()+"\t\t"+
            Firstname.get()+ '    \t'+ Lastname.get()+ "  \t"+ Mobile_no.get()+" \t"+" \t"+ Address.get()+" \t" + Pincode.get() +
                    "  \t" + member_gendercmb.get() + "  \t" + Membership.get() + "\n")


        ###################### TITLE ###################
        title = Label(self.root, text="Member Registration Form", font=("monotype corsiva", 30, "bold"),bd=5,
                    relief=GROOVE, bg="#E6005C", fg="#000000")
        title.pack(side=TOP, fill=X)


        ################ Member Frame ###############
        Manage_Frame= Frame(self.root, bd=4, relief=RIDGE, bg="#001a66")
        Manage_Frame.place(x=20, y=100, width=450, height=630)



        ######## text, label, comboboxes in manage frame #############
        Cus_title= Label(Manage_Frame, text="Customer Details", font=("arial",20,"bold"),bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        member_date1b1 = Label(Manage_Frame, text="Date", font=("arial",15,"bold"), bg="#001a66", fg="white")
        member_date1b1.grid(row=1, column=0, pady=5, padx=10, sticky="w")


        member_datetxt= Entry(Manage_Frame, font=("arial",15,"bold"), textvariable=Date_of_Registration)
        member_datetxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_ref1b1 = Label(Manage_Frame, text="Reference ID", font=("arial",15,"bold"), bg="#001a66",
                              fg="white")
        member_ref1b1.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        member_reftxt = Entry(Manage_Frame, font=("arial", 15, "bold"), state=DISABLED, textvariable=Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fname1b1 = Label(Manage_Frame, text="First Name", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_fname1b1.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable= Firstname)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")


        member_lname1b1 = Label(Manage_Frame, text="Last Name", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_lname1b1.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lnametxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Lastname)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobile1b1 = Label(Manage_Frame, text="Mobile No", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_mobile1b1.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobiletxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_address1b1 = Label(Manage_Frame, text="Address", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_address1b1.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_addresstxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincode1b1 = Label(Manage_Frame, text="Pincode", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_pincode1b1.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_pincodetxt = Entry(Manage_Frame, font=("arial", 15, "bold"), textvariable=Pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_gender1b1 = Label(Manage_Frame, text="Gender", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_gender1b1.grid(row=8, column=0, pady=5, padx=10, sticky="w")

        member_gendercmb= ttk.Combobox(Manage_Frame, textvariable=var4, state="readonly", font=("arial",15,"bold"),
                                       width=19)
        member_gendercmb['values']= ("","Male","Female","Other")
        member_gendercmb.current(0) # when nothing it will be set as empty which we have given at index 0
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        member_id_proof1b1 = Label(Manage_Frame, text="ID Proof", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_id_proof1b1.grid(row=9, column=0, pady=5, padx=10, sticky="w")

        member_id_proofcmb = ttk.Combobox(Manage_Frame, textvariable=var3, state="readonly", font=("arial", 15, "bold"),
                                        width=19)
        member_id_proofcmb['values'] = ("", "Aadhar Card", "Pan Card", "Driving Licence","Student ID")
        member_id_proofcmb.current(0)  # when nothing it will be set as empty which we have given at index 0
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtype1b1 = Label(Manage_Frame, text="Member Type", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_memtype1b1.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        member_memtypecmb = ttk.Combobox(Manage_Frame, textvariable=var2, state="readonly", font=("arial", 15, "bold"),
                                        width=19)
        member_memtypecmb['values'] = ("", "Ayushman Card", "Insurance", "Pay with leaving")
        member_memtypecmb.current(0)  # when nothing it will be set as empty which we have given at index 0
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_paymentwith1b1 = Label(Manage_Frame, text="Payment", font=("arial", 15, "bold"), bg="#001a66", fg="white")
        member_paymentwith1b1.grid(row=11, column=0, pady=5, padx=10, sticky="w")

        member_paymentwithcmb = ttk.Combobox(Manage_Frame, textvariable=var1, state="readonly", font=("arial", 15, "bold"),
                                        width=19)
        member_paymentwithcmb['values'] = ("", "Cash", "Debit Card-RuPay","Debit Card-Visa", "Debit Card-Mastercard","Credit Card", "Phonepe", "Google Pay")
        member_paymentwithcmb.current(0)  # when nothing it will be set as empty which we have given at index 0
        member_paymentwithcmb.grid(row=11, column=1, pady=5, padx=10, sticky="w")


        member_membership= Checkbutton(Manage_Frame, text="Membership fees", variable=var5, onvalue=1,  offvalue=0, font=("arial",15,"bold"),
                                       bg="#001a66",fg="white",command=membership_fees )
        member_membership.grid(row=12, column=0, sticky="w")
        member_membership= Entry(Manage_Frame, font=("arial",15,"bold"),state=DISABLED, justify=RIGHT,textvariable=Membership)
        member_membership.grid(row=12, column=1, pady=5, padx=10, sticky="w")




        ######### Details Frame ##############
        detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        detail_frame.place(x=500, y=100, width=820, height=630)


        detail_label= Label(detail_frame, font=("arial",10,"bold"), pady=10, padx=2, width=95,
            text=" Date\t  Ref Id\t    Firstname    Lastname    Mobile No    Address    Pincode    Gender   Membership")
        detail_label.grid(row=0, column=0, columnspan=4, sticky="w")
        detail_labeltxt= Text(detail_frame, width=123, height=34, font=("arial",10))
        detail_labeltxt.grid(row=1,column=0, columnspan=4)


        ############# we will add button in detail frame ############

        receiptbtn= Button(detail_frame,padx=15, bd=5, font=("arial",12,"bold"),
                           bg="#ff9966",width=20, text="Receipt", command= Receipt)
        receiptbtn.grid(row=2, column=0)

        resetbtn = Button(detail_frame, padx=15, bd=5, font=("arial", 12, "bold"),
                          bg="#ff9966", width=20, text="Reset", command=reeesetbtt)
        resetbtn.grid(row=2, column=1)

        exitbtn = Button(detail_frame, padx=15, bd=5, font=("arial", 12, "bold"),
                         bg="#ff9966", width=20, text="Exit",command=exitbtt)
        exitbtn.grid(row=2, column=2)






class Windows3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital management system")
        self.master.geometry('1350x750+0+0')  # x-axis,y-axis,0,0 are location from top leftmost
        self.frame = Frame(self.master)
        self.frame.pack()



class Hospital():
    def __init__(self,root):
        self.root= root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0") # we will consider full screen(maximum window)
        self.root.configure(background="black")


        ###################### variable declaration #####################


        Ref= StringVar()
        cmbTabletnames= StringVar()
        HospitalCode= StringVar()
        Number_of_Tablets= StringVar()
        Lot=StringVar()
        IssueDate= StringVar()
        ExpiryDate= StringVar()
        DailyDose= StringVar()
        SideEffects= StringVar()
        MoreInformation= StringVar()
        StorageAdvice= StringVar()
        Medication= StringVar()
        PatientId= StringVar()
        PatientNHnumver= StringVar()
        PatientName= StringVar()
        Dateofbirth= StringVar()
        PatientAddress= StringVar()
        Prescription= StringVar()
        NHSnumber= StringVar()

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        ################# generate Random Number Automatically

        def Reference_numfunc():
            ranumber= random.randint(10000,9999999)
            randomnumber= str(ranumber)
            Ref.set(randomnumber)


        def prescriptionfunc():
            Reference_numfunc()
            TextPrescription.insert(END,"Patient ID: \t\t"+PatientId.get()+"\n")
            TextPrescription.insert(END, "Patient Name: \t\t" + PatientName.get() + "\n")
            TextPrescription.insert(END, "Tablet: \t\t" + cmbTabletnames.get() + "\n")
            TextPrescription.insert(END, "Number_of_tablet: \t\t" + Number_of_Tablets.get() + "\n")
            TextPrescription.insert(END, "Daily Dose: \t\t" + DailyDose.get() + "\n")
            TextPrescription.insert(END, "Issued Date: \t\t" + IssueDate.get() + "\n")
            TextPrescription.insert(END, "ExpiryDate: \t\t" + ExpiryDate.get() + "\n")
            TextPrescription.insert(END, "Storage Advice: \t\t" + StorageAdvice.get() + "\n")
            TextPrescription.insert(END, "More Information: \t\t" + MoreInformation.get() + "\n")
            return


        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescriptiondata.insert(END, Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+
            PatientName.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+
            cmbTabletnames.get()+"\t"+Number_of_Tablets.get()+"\t\t"+IssueDate.get()+"\t\t"+
            ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+StorageAdvice.get()+"\t\t"+PatientId.get()+"\n")
            return









        def exitbtn():
            exitbtn= tkinter.messagebox.askyesno("Hospital Management System","Are you sure want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return


        def deletefunc():
            Ref.set("")
            cmbTabletnames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumver.set("")
            PatientName.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptiondata.delete("1.0",END)
            return
        def resetfunc():
            Ref.set("")
            cmbTabletnames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumver.set("")
            PatientName.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0", END)
            return





        ######################### Title  #######################
        title= Label(self.root,text="Hospital Management System", font=("monotype corsiva",42,"bold"),bd=5,
                         relief=GROOVE, bg="#2eb8b8")
        title.pack(side=TOP, fill=X)


        #############   Frames  ######################

        Manage_Frame= Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame=Frame(self.root,width=1510, height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10, y=460)

        Data_Frame=LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#266e73")
        Data_Frame.place(x=10, y=510)


        ################### Frames #############################
        Data_FrameLeft= LabelFrame(Manage_Frame, width=1050, text="General Information",
        font=("arial",20,"italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc" )
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Prescription",
        font=("arial", 15, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)



        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Prescription Data",
                 font=("arial", 12, "italic bold"), height=390, bd=4, relief=RIDGE, bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)


        ################# Labels ############
        Datelbl= Label(Data_FrameLeft, font=("arial",12,"bold"),width=20,text="Date", padx=2, bg="#0099cc")
        Datelbl.grid(row=0, column=0, pady=5, sticky=W)
        Datetxt= Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        ########### Ref #####
        Reflbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Reference Number", padx=2, bg="#0099cc")
        Reflbl.grid(row=1, column=0, pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), state=DISABLED, width=27, textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        ######## Patient Id

        PatientIdlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Id", padx=2,
                       bg="#0099cc")
        PatientIdlbl.grid(row=2, column=0, pady=5, sticky=W)
        PatientIdtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientId)
        PatientIdtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        ######### Patient Name

        PatientNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Name", padx=2,
                             bg="#0099cc")
        PatientNamelbl.grid(row=3, column=0, pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientName)
        PatientNametxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        ################## Date Of Birth

        Dateofbirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of birth", padx=2,
                               bg="#0099cc")
        Dateofbirthlbl.grid(row=4, column=0, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        ############## Address

        Addresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Address", padx=2,
                               bg="#0099cc")
        Addresslbl.grid(row=5, column=0, pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PatientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        ####### NHS number

        NHSnumberlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text=" NHS Unique number", padx=2,
                           bg="#0099cc")
        NHSnumberlbl.grid(row=6, column=0, pady=5, sticky=W)
        NHSnumbertxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable= NHSnumber)
        NHSnumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        ########## Tablet Name

        Tabletlbl= Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Tablet",padx=2, bg="#0099cc")
        Tabletlbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        Tabletcmb=ttk.Combobox(Data_FrameLeft, textvariable=cmbTabletnames, width=25, state="readonly",
                               font=("arial",12,"bold"))
        Tabletcmb['values']=("","Paracetamol","Dan-p","Dio-l one","Calpol", "Almodipine Besylate","Nexium","Singulair",
                             "Plavix","Amoxicillian","Limcin-900")
        Tabletcmb.current(0) # we will keep index 0 when nothing is selected
        Tabletcmb.grid(row=7, column=1, padx=10, pady=5)


        ####### No of Tablets to take


        No_of_Tabletslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text=" No of Tablets", padx=2,
                           bg="#0099cc")
        No_of_Tabletslbl.grid(row=8, column=0, pady=5, sticky=W)
        No_of_Tabletstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable= Number_of_Tablets)
        No_of_Tabletstxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)


        ### now we will make 2nd column of other details in same frame

        ###### Hospital Code


        HospitalCodelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Hospital Code", padx=2,
                           bg="#0099cc")
        HospitalCodelbl.grid(row=0, column=2, pady=5, sticky=W)
        HospitalCodetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)


        ### Storage Advice whwre to keep medicine


        StorageAdvicelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Storage Advice", padx=2,
                                bg="#0099cc")
        StorageAdvicelbl.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=StorageAdvice, width=23, state="readonly",
                                 font=("arial", 12, "bold"))
        StorageAdvicecmb['values'] = ("","Under room temp","below 5*C","below 0*C","Refrigration" )

        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5, sticky=E)


        ####### Lot number of medicines

        Lot_nolbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Lot Number", padx=2,
                                bg="#0099cc")
        Lot_nolbl.grid(row=2, column=2, pady=5, sticky=W)
        Lot_notxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Lot)
        Lot_notxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        ######## Issue Date

        IssueDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Issue", padx=2,
                          bg="#0099cc")
        IssueDatelbl.grid(row=3, column=2, pady=5, sticky=W)
        IssueDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=IssueDate)
        IssueDatetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)


        ####### Expiry Date

        ExpiryDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of Expiry", padx=2,
                             bg="#0099cc")
        ExpiryDatelbl.grid(row=4, column=2, pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        ########## Daily Dose

        Dailydoselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Daily Dosage", padx=2,
                              bg="#0099cc")
        Dailydoselbl.grid(row=5, column=2, pady=5, sticky=W)
        Dailydosetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=DailyDose)
        Dailydosetxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        ######## side Effects

        SideEffectslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Side Effects", padx=2,
                             bg="#0099cc")
        SideEffectslbl.grid(row=6, column=2, pady=5, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=SideEffects)
        SideEffectstxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        # More information like meet dr or any other related to patient which is important but not covered in list

        MoreInformationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="More Information", padx=2,
                               bg="#0099cc")
        MoreInformationlbl.grid(row=7, column=2, pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        ####### Medication (yes/no)

        Medicationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Medication",
                                   padx=2,bg="#0099cc")
        Medicationlbl.grid(row=8, column=2, pady=5, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=25, textvariable=Medication)
        Medicationtxt.grid(row=8, column=3, padx=10, pady=5, sticky=E)




        #### Text field for prescription
        TextPrescription= Text(Data_FrameRight, font=("arial",12,"bold"), width=55, height=17, padx=3, pady=5)
        TextPrescription.grid(row=0,column=0)


        ############ Text for Prescription data

        TextPrescriptiondata = Text(Data_Framedata, font=("arial", 12, "bold"), width=205, height=17,)
        TextPrescriptiondata.grid(row=1, column=0)

        ###### Now we will add button to our middle frame

        Prescriptionbtn= Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground="#fcceb2",font=("arial",15,"bold"), width=22, command=prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Recieptbtn = Button(Button_Frame, text="Prescription Data", bg="#ffaab0", activebackground="#fcceb2",font=("arial", 15, "bold"), width=22, command=prescriptiondatafunc)
        Recieptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground="#fcceb2",font=("arial", 15, "bold"), width=22, command= resetfunc )
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground="#fcceb2",font=("arial", 15, "bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2",font=("arial", 15, "bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15, )

        prescriptiondatarow=  Label(Data_Framedata, bg="white", font=("arial",12,"bold"),
        text="Date\tReference Id\tPatient Name\tDate of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatientID")
        prescriptiondatarow.grid(row=0, column=0, sticky=W,)






class Windows4:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor management system")
        self.master.geometry('1350x750+0+0')  # x-axis,y-axis,0,0 are location from top leftmost
        self.frame = Frame(self.master)
        self.frame.pack()


class Doctor():
    def __init__(self,root):
        self.root=root
        self.root.title("Doctor Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")


        ########## we will declare  all functions together ##############

        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrId=StringVar()
        Drname=StringVar()
        Dateofbirth=StringVar()
        Spes=StringVar()
        GovtPri=StringVar()
        Surgeries=StringVar()
        Experiences=StringVar()
        Nurses=StringVar()
        DrMobile=StringVar()
        PtName=StringVar()
        Apptime=StringVar()
        PtAge=StringVar()
        PtAddress=StringVar()
        PtMobile=StringVar()
        Disease=StringVar()
        Case=StringVar()
        BenefitCard=StringVar()


        def exitbtn():
            exitbtn=tkinter.messagebox.askyesno("Doctor management System","Are you sure you want to exit ?")
            if exitbtn>0:
                root.destroy()
            return

        def resetfunc():
            DrId.set("")
            Drname.set("")
            Dateofbirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PtAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return

        def deletefunc():
            DrId.set("")
            Drname.set("")
            Dateofbirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PtAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0", END)
            TextPrescriptionData.delete("1.0", END)
            return

        def Patient_idFunc():
            ranumber=random.randint(10000,999999)
            randomnumber=str(ranumber)
            DrId.set(randomnumber)

        def prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"
            +Drname.get()+"\t\t"+Dateofbirth.get()+"\t\t"+Spes.get()+"\t\t"+GovtPri.get()+"\t\t"+
            Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t\t"+DrMobile.get()+"\t\t"+
            PtName.get()+"\t\t"+Case.get()+"\t"+PtAge.get()+"\n")
            return

        def prescriptionfunc():
            Patient_idFunc()
            TextPrescription.insert(END, "Date: \t\t" + Date_of_Registration.get() + "\n")
            TextPrescription.insert(END, "Patient Name: \t\t" + PtName.get() + "\n")
            TextPrescription.insert(END, "Appointment Time: \t\t" + Apptime.get() + "\n")
            TextPrescription.insert(END, "Age: \t\t" + PtAge.get() + "\n")
            TextPrescription.insert(END, "Address: \t\t" + PtAddress.get() + "\n")
            TextPrescription.insert(END, "Disease: \t\t" + Disease.get() + "\n")
            TextPrescription.insert(END, "Case: \t\t" + Case.get() + "\n")
            TextPrescription.insert(END, "Benefit Card: \t\t" + BenefitCard.get() + "\n")
            TextPrescription.insert(END, "To meet Dr: \t\t" + Drname.get() + "\n")
            TextPrescription.insert(END, "Dr.Mobile No: \t\t" + DrMobile.get() + "\n")
            return





        ##### Titlr Label ###################

        title= Label(self.root, text="Doctor Management System", font=("monotype corsiva",42,"bold"),bd=5, relief=GROOVE, bg="#b7d8d6",
                     fg="black")
        title.pack(side=TOP, fill=X)

        ######## Frame
        Manage_Frame= Frame(self.root, width=1510, bd=5, height=400, relief=RIDGE, bg="#789e9e")
        Manage_Frame.place(x=10, y=80)

        Buttons_Frame = Frame(self.root, width=1510, bd=4, height=400, relief=RIDGE, bg="#eef3db")
        Buttons_Frame.place(x=10, y=460)

        Data_Frame = Frame(self.root, width=1510, bd=4, height=400, relief=RIDGE, bg="#eef3db")
        Data_Frame.place(x=10, y=510)

        Data_FrameLeft= LabelFrame(Manage_Frame, width=1050, text= "General Information",
            font=("arial",20," italic bold"), height=390, bd=7, pady=1, relief=RIDGE, bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Doctor's Details",
                                    font=("arial", 12, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#b7d8d6")
        Data_Framedata.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Patient's Details",
                                     font=("arial", 15, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#789e9e")
        Data_FrameRight.pack(side=RIGHT)

        ###### Doctor's Id

        DrIdlbl= Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Doctor ID", bg="#789e9e")
        DrIdlbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        DrIdtxt= Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27, state=DISABLED, textvariable=DrId)
        DrIdtxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        DrNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Doctor Name", bg="#789e9e")
        DrNamelbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        DrNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27,  textvariable=Drname)
        DrNametxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        Dateofbirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Date of birth", bg="#789e9e")
        Dateofbirthlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27,  textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        Speslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Specialization", bg="#789e9e")
        Speslbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        Spestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27,  textvariable=Spes)
        Spestxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        Govtprilbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Govt/private", bg="#789e9e")
        Govtprilbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Govtpricmb=ttk.Combobox(Data_FrameLeft, textvariable=GovtPri, width=25, state="readonly", font=("arial",12,"bold"))
        Govtpricmb["values"]= ["","Goverment","Private"]
        Govtpricmb.current(0)
        Govtpricmb.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        Surgerieslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Surgeries", bg="#789e9e")
        Surgerieslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Surgeriestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Surgeries)
        Surgeriestxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        Experiencelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Experience", bg="#789e9e")
        Experiencelbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        Experiencetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Experiences)
        Experiencetxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Nurseslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Nurses Under Dr", bg="#789e9e")
        Nurseslbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        Nursestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Nurses)
        Nursestxt.grid(row=7, column=1, padx=10, pady=5, sticky=E)

        DrMobilelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Dr Mobile No", bg="#789e9e")
        DrMobilelbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        DrMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=DrMobile)
        DrMobiletxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        Datelbl= Label(Data_FrameLeft, font=("arial",12,"bold"), width=20, text="Date", padx=2, bg="#789e9e")
        Datelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Datetxt= Entry(Data_FrameLeft, font=("arial",12,"bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column =3, padx=10, pady=5, sticky=E)

        Ptnamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Name", padx=2, bg="#789e9e")
        Ptnamelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        Ptnametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtName)
        Ptnametxt.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        Apptimelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Appointment Time", padx=2,
                          bg="#789e9e")
        Apptimelbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Apptimetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Apptime)
        Apptimetxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        PtAgelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Age", padx=2,
                           bg="#789e9e")
        PtAgelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        PtAgetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtAge)
        PtAgetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        PtAddresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Address", padx=2,
                            bg="#789e9e")
        PtAddresslbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        PtAddresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtAddress)
        PtAddresstxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        PtMobilelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Mobile No", padx=2,
                         bg="#789e9e")
        PtMobilelbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        PtMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=PtMobile)
        PtMobiletxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)



        Diseaselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Patient Disease", padx=2,
                             bg="#789e9e")
        Diseaselbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        Diseasetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=Disease)
        Diseasetxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        Caselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Case",padx=2, bg="#789e9e")
        Caselbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable=Case, width=25, state="readonly",
                                  font=("arial", 12, "bold"))
        Casecmb["values"] = ["", "New Case","Old Case"]
        Casecmb.current(0)
        Casecmb.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        BenefitCardlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), width=20, text="Benefit Card", padx=2, bg="#789e9e")
        BenefitCardlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable=BenefitCard, width=25, state="readonly",
                               font=("arial", 12, "bold"))
        BenefitCardcmb["values"] = ("", "Ayusman Card","Health Insuarance","Senior Citizen","Army card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8, column=3, padx=10, pady=5, sticky=E)



        ######### TextPrescription ###########
        TextPrescription= Text(Data_FrameRight, font=("Arial",12,"bold"), width=55, height=17, padx=3, pady=5)
        TextPrescription.grid(row=0, column=0)
        TextPrescriptionData= Text(Data_Framedata, font=("Arial",12,"bold"), width=203, height=12)
        TextPrescriptionData.grid(row=1, column=0)

        ############# buttons ########
        Prescriptionbtn= Button(Buttons_Frame, text="Patient Information",bg="#fe615a",activebackground="#cc6686",
                font=("arial",15,"bold"), width=22, command=prescriptionfunc )
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        DoctorDetailbtn = Button(Buttons_Frame, text="Doctor's Details", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=prescriptiondatafunc)
        DoctorDetailbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Buttons_Frame, text="Reset", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Buttons_Frame, text="Delete", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Buttons_Frame, text="Exit", bg="#fe615a", activebackground="#cc6686",
                                 font=("arial", 15, "bold"), width=22,command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)


        Prescriptiondatarow=Label(Data_Framedata, bg="white", font=("arial",12,"bold"),
        text="Date\tDoctor Id\tDoctor Name\tDate of Birth\tSpecialization\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name\tCase\tPt.Age")
        Prescriptiondatarow.grid(row=0, column=0, sticky=W)









class Windows5:
    def __init__(self, master):
        self.master = master
        self.master.title("Medicine system")
        self.master.geometry('1700x900+0+0')  # x-axis,y-axis,0,0 are location from top leftmost
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == "__main__":
    main()




