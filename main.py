from tkinter import  *

root=Tk()

root.title("Billing System")
root.geometry("1270x685")
root.iconbitmap('1489436625-billingdatadollarcurrency_81879 (1).ico')
headingLabel=Label(root, text="Retail Billng System", font=("times new roman", 30, 'bold')
                   ,bg="gray20",fg="gold", bd=12, relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

cusomter_details_frame=LabelFrame(root, text="Customer Details", font=("time new roman",15,"bold"),
                                  fg="gold",bd=8,relief=GROOVE,bg="gray20")
cusomter_details_frame.pack(fill=X)

nameLabel=Label(cusomter_details_frame, text="Name",font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
nameLabel.grid(row=0, column=0, padx=20)

nameEntry=Entry(cusomter_details_frame, font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0, column=1,padx=8)

phoneLabel=Label(cusomter_details_frame, text="Phone Number",font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
phoneLabel.grid(row=0, column=2, padx=20,pady=2)

PhoneEntry=Entry(cusomter_details_frame, font=('arial',15),bd=7,width=18)
PhoneEntry.grid(row=0, column=3,padx=8)

billnumberLabel=Label(cusomter_details_frame, text="Bill Number",font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
billnumberLabel.grid(row=0, column=4, padx=20,pady=2)

BillEntry=Entry(cusomter_details_frame, font=('arial',15),bd=7,width=18)
BillEntry.grid(row=0, column=5,padx=8)

searchButton=Button(cusomter_details_frame, text="SEARCH",font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productFrame=Frame(root)
productFrame.pack(pady=10)

cosmeticFrame=LabelFrame(productFrame,text="Cosmetics",font=("time new roman",15,"bold"),
                                  fg="gold",bd=8,relief=GROOVE,bg="gray20")
cosmeticFrame.grid(row=0,column=0)

bathshopLabel=Label(cosmeticFrame,text="Bath Shop" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
bathshopLabel.grid(row=0, column=0,pady=9,padx=10)

bathshopEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
bathshopEntry.grid(row=0, column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticFrame,text="Face Cream" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
facecreamLabel.grid(row=1, column=0,pady=9,padx=10)

facecreamEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
facecreamEntry.grid(row=1, column=1,pady=9,padx=10)


FaceWashLabel=Label(cosmeticFrame,text="Face Wash" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
FaceWashLabel.grid(row=2, column=0,pady=9,padx=10)

FaceWashEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
FaceWashEntry.grid(row=2, column=1,pady=9,padx=10)

root.mainloop()