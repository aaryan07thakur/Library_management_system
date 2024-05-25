from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class Librarymanagementsystem:
    def __init__(self,root): 
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x300+0+0")


        # ======================Variable=========================================================

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.adderss1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.dayasofbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()






        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",background="powder blue",foreground="green",
                     border=8,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,border=8,relief=RIDGE,padx=15,background="powder blue")
        frame.place(x=0,y=78,width=1365,height=400)

        # ===============DataFrameLeft=================================================

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",background="powder blue",foreground="green",
                     border=8,relief=RIDGE,font=("times new roman",20,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=377)

        lblMember=Label(DataFrameLeft,background="powder blue",text="Member Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"), width=27,state="readonly")
        comMember["value"]=("Admin staf","student","Lecturer")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="PRN No:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_No.grid(row=1,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="ID No:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=2,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.id_var,width=29)
        txtPRN_No.grid(row=2,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="First Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=3,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.firstname_var,width=29)
        txtPRN_No.grid(row=3,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Last Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=4,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.lastname_var,width=29)
        txtPRN_No.grid(row=4,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Address1:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=5,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.adderss1_var,width=29)
        txtPRN_No.grid(row=5,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Address2:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=6,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.address2_var,width=29)
        txtPRN_No.grid(row=6,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=7,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPRN_No.grid(row=7,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=8,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.mobile_var,width=29)
        txtPRN_No.grid(row=8,column=1)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Book ID:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=0,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.bookid_var,width=29)
        txtPRN_No.grid(row=0,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=1,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtPRN_No.grid(row=1,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Auther Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=2,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.auther_var,width=29)
        txtPRN_No.grid(row=2,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Data Borrowed:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=3,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtPRN_No.grid(row=3,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Data Due:",font=("arial",12,"bold",),padx=2,pady=6)
        lblPRN_No.grid(row=4,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.datedue_var,width=29)
        txtPRN_No.grid(row=4,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Days On Book:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=5,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dayasofbook_var,width=29)
        txtPRN_No.grid(row=5,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Late Return Fine:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=6,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.latereturnfine_var,width=29)
        txtPRN_No.grid(row=6,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Data Over Due:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=7,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtPRN_No.grid(row=7,column=3)

        lblPRN_No=Label(DataFrameLeft,background="powder blue",text="Actual Price:",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN_No.grid(row=8,column=2,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("times new roman",12,"bold"),textvariable=self.finalprice_var,width=29)
        txtPRN_No.grid(row=8,column=3)

        # =====================DataFrameRight======================================================================

        DataFrameRight=LabelFrame(frame,text="Book Details",background="powder blue",foreground="green",
                     border=8,relief=RIDGE,font=("arial",20,"bold"))
        DataFrameRight.place(x=810,y=5,width=520,height=377)

        self.txtBox=Text(DataFrameRight,font=("arial",10,"bold"),width=42,height=20,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        ListBooks=['Effective Java','Automate the Boring Stuff with Python,2nd Edition','Design and Build Websites First Edition',
                   "A Modern Introduction to Programming",'Head First Java, 2nd Edition','Java Concurrency in Practice 1st Edition','Modern PHP',
                    'Head First PHP & MySQL','Eloquent Ruby (Addison-Wesley Professional Ruby Series)','Python Crash Course,Project-Based',
                    'Head First Python: A Brain-Friendly Guide','Learn Python 3 the Hard Way','C# in Depth: Fourth Edition',
                    'Learning R: A Step-by-Step Function Guide to Data Analysis','Database System Concepts','SQL in 10 Minutes, Sams Teach Yourself',
                    'Atomic Habits','The Obstacle Is the Way','Ego Is the Enemy','Stillness Is the Key']
        

        def SelectBook(event=""):
            value=str(ListBox.get(ListBox.curselection()))
            x=value
            if (x=="Effective Java"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Java basic")
                self.auther_var.set("Joshua Bloch")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.999")

            elif x=="Automate the Boring Stuff with Python,2nd Edition":
                self.bookid_var.set("BKID5455")
                self.booktitle_var.set("Practical Programming for Total Beginners")
                self.auther_var.set("Al Sweigart")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.799")
            
            elif(x=="Design and Build Websites First Edition"):
                self.bookid_var.set("BKID5456")
                self.booktitle_var.set("HTML and CSS")
                self.auther_var.set("Jon Duckett")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.750")

            elif(x=="A Modern Introduction to Programming"):
                self.bookid_var.set("BKID5457")
                self.booktitle_var.set("Eloquent JavaScript, 3rd Edition")
                self.auther_var.set("Marijn Haverbeke")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.800")

            elif(x=="Head First Java, 2nd Edition"):
                self.bookid_var.set("BKID5458")
                self.booktitle_var.set("Head First Java, 2nd Edition")
                self.auther_var.set("Kathy Sierra")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.1025")

            elif(x=="Java Concurrency in Practice 1st Edition"):
                self.bookid_var.set("BKID5459")
                self.booktitle_var.set("Java Concurrency in Practice 1st Edition")
                self.auther_var.set("Brian Goetz")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.1025")

            elif(x=="Modern PHP"):
                self.bookid_var.set("BKID5460")
                self.booktitle_var.set("New Features and Good Practices 1st Edition")
                self.auther_var.set("Josh Lockhart")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.725")

            elif(x=="Head First PHP & MySQL"):
                self.bookid_var.set("BKID5461")
                self.booktitle_var.set("A Brain-Friendly Guide 1st Edition, Kindle Edition")
                self.auther_var.set("Lynn Beighley,Michael Morrison")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.825")
            

            elif(x=="Eloquent Ruby (Addison-Wesley Professional Ruby Series)"):
                self.bookid_var.set("BKID5462")
                self.booktitle_var.set("Eloquent Ruby")
                self.auther_var.set("Lynn Beighley,Michael Morrison")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.995")

            elif(x=="Python Crash Course,Project-Based"):
                self.bookid_var.set("BKID5463")
                self.booktitle_var.set("Python Crash Course")
                self.auther_var.set("Eric Matthes")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.1095")

            elif(x=="Head First Python: A Brain-Friendly Guide"):
                self.bookid_var.set("BKID5464")
                self.booktitle_var.set("Head First Python")
                self.auther_var.set("Paul Barry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.999")

            elif(x=="Learn Python 3 the Hard Way"):
                self.bookid_var.set("BKID5465")
                self.booktitle_var.set("Learn Python 3 the Hard Way")
                self.auther_var.set("Paul Barry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.159")

            elif(x=="C# in Depth: Fourth Edition"):
                self.bookid_var.set("BKID5466")
                self.booktitle_var.set("C# in Depth")
                self.auther_var.set("Jon Skeet")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.795")
            
            elif(x=="Learning R: A Step-by-Step Function Guide to Data Analysis"):
                self.bookid_var.set("BKID5467")
                self.booktitle_var.set("Learning R")
                self.auther_var.set("Richard Cotton")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.1155")

            elif(x=="Database System Concepts"):
                self.bookid_var.set("BKID5468")
                self.booktitle_var.set("Database System Concepts")
                self.auther_var.set("Abraham Silberschatz, Henry F. Korth, and S. Sudarshan")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.1055")

            elif(x=="SQL in 10 Minutes, Sams Teach Yourself"):
                self.bookid_var.set("BKID5469")
                self.booktitle_var.set("SQL in 10 Minutes, Sams Teach Yourself")
                self.auther_var.set("Ben Forta")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.755")

            elif(x=="Atomic Habits"):
                self.bookid_var.set("BKID5470")
                self.booktitle_var.set("Atomic Habits")
                self.auther_var.set("Ben Forta")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.555")

            elif(x=="The Obstacle Is the Way"):
                self.bookid_var.set("BKID5471")
                self.booktitle_var.set("The Obstacle Is the Way")
                self.auther_var.set("Ryan Holiday")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.855")

            elif(x=="Ego Is the Enemy"):
                self.bookid_var.set("BKID5472")
                self.booktitle_var.set("Ego Is the Enemy")
                self.auther_var.set("Ryan Holiday")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.955")

            elif(x=="Stillness Is the Key"):
                self.bookid_var.set("BKID5473")
                self.booktitle_var.set("Stillness Is the Key")
                self.auther_var.set("Ryan Holiday")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=30)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.dayasofbook_var.set(30)
                self.latereturnfine_var.set("Rs.20")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("RS.1095")
           
            

            

        

         #list box initializations

        ListBox=Listbox(DataFrameRight,font=("arial",10,"bold"),width=25,height=19)
        ListBox.bind("<<ListboxSelect>>",SelectBook)
        ListBox.grid(row=0,column=0,padx=2)
        listScrollbar.config(command=ListBox.yview)

        for item in ListBooks:
            ListBox.insert(END,item)
        

        # ================Buttons Frame===============================================================

        Framebutton=Frame(self.root,border=8,relief=RIDGE,padx=10,background="powder blue")
        Framebutton.place(x=0,y=478,width=1362,height=50)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=21,background="blue",foreground="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=21,background="blue",foreground="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=21,background="blue",foreground="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=21,background="blue",foreground="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=21,background="blue",foreground="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=21,background="blue",foreground="white")
        btnAddData.grid(row=0,column=5)


         # ================Information Frame===============================================================

        frameDetails=Frame(self.root,border=10,relief=RIDGE,padx=15,background="powder blue")
        frameDetails.place(x=0,y=528,width=1362,height=190)

        Table_frame =Frame(frameDetails,bd=6,relief=RIDGE,background="powder blue")
        Table_frame.place(x=0,y=2,width=1320,height=175)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","Prno","title","firstname",
                                                            "lastname","address1","address2","postid",
                                                           "mobile","bookid","booktitle","auther","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","finalprice" ),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type",)
        self.library_table.heading("Prno",text="PRN No.",)
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="first Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DayasofBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("Prno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="RN@aaryan06",database="librarymanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(     self.member_var.get(),
                                                                                                                    self.prn_var.get(),
                                                                                                                    self.id_var.get(),
                                                                                                                    self.firstname_var.get(),
                                                                                                                    self.lastname_var.get(),
                                                                                                                    self.adderss1_var.get(),
                                                                                                                    self.address2_var.get(),
                                                                                                                    self.postcode_var.get(),
                                                                                                                    self.mobile_var.get(),
                                                                                                                    self.bookid_var.get(),
                                                                                                                    self.booktitle_var.get(),
                                                                                                                    self.auther_var.get(),
                                                                                                                    self.dateborrowed_var.get(),
                                                                                                                    self.datedue_var.get(),
                                                                                                                    self.dayasofbook_var.get(),
                                                                                                                    self.latereturnfine_var.get(),
                                                                                                                    self.dateoverdue_var.get(),
                                                                                                                    self.finalprice_var.get()
                                                                                                                    ))


        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member has been inserted successfully")


    def update(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="RN@aaryan06",database="librarymanagement")
            my_cursor=conn.cursor()
            my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,postId=%s,Mobile=%s,BookId=%s,Booktitle=%s,Auther=%s,dateborrowed=%s,datedue=%s,dayasofbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where PRN_No=%s",(
                                                                                            self.member_var.get(),
                                                                                            self.id_var.get(),
                                                                                            self.firstname_var.get(),
                                                                                            self.lastname_var.get(),
                                                                                            self.adderss1_var.get(),
                                                                                            self.address2_var.get(),
                                                                                            self.postcode_var.get(),
                                                                                            self.mobile_var.get(),
                                                                                            self.bookid_var.get(),
                                                                                            self.booktitle_var.get(),
                                                                                            self.auther_var.get(),
                                                                                            self.dateborrowed_var.get(),
                                                                                            self.datedue_var.get(),
                                                                                            self.dayasofbook_var.get(),
                                                                                            self.latereturnfine_var.get(),
                                                                                            self.dateoverdue_var.get(),
                                                                                            self.finalprice_var.get(),
                                                                                            self.prn_var.get(),
                                            
            
                                                                                     ))
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("Success","Member has been updated")



    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="RN@aaryan06",database="librarymanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    def get_cursor(self,event=""):
        cursor_rows=self.library_table.focus()  
        content =self.library_table.item(cursor_rows)
        rows=content['values']


        self.member_var.set(rows[0])
        self.prn_var.set(rows[1])
        self.id_var.set(rows[2])
        self.firstname_var.set(rows[3])
        self.lastname_var.set(rows[4])
        self.adderss1_var.set(rows[5])
        self.address2_var.set(rows[6])
        self.postcode_var.set(rows[7])
        self.mobile_var.set(rows[8])
        self.bookid_var.set(rows[9])
        self.booktitle_var.set(rows[10])
        self.auther_var.set(rows[11])
        self.dateborrowed_var.set(rows[12])
        self.datedue_var.set(rows[13])
        self.dayasofbook_var.set(rows[14])
        self.latereturnfine_var.set(rows[15])
        self.dateoverdue_var.set(rows[16])
        self.finalprice_var.set(rows[17])



    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"First Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.adderss1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"DayasofBook:\t\t"+ self.dayasofbook_var.get() + "\n")
        self.txtBox.insert(END,"LatereturnFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get() + "\n")


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.adderss1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.dayasofbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="RN@aaryan06",database="librarymanagement")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")
            


if __name__ == "__main__":
    root=Tk()
    obj=Librarymanagementsystem(root)
    root.mainloop()


