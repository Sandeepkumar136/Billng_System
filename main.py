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
bathshopLabel.grid(row=0, column=0,pady=9,padx=10,sticky="W")

bathshopEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
bathshopEntry.grid(row=0, column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticFrame,text="Face Cream" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
facecreamLabel.grid(row=1, column=0,pady=9,padx=10,sticky="W")

facecreamEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
facecreamEntry.grid(row=1, column=1,pady=9,padx=10)


FaceWashLabel=Label(cosmeticFrame,text="Face Wash" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
FaceWashLabel.grid(row=2, column=0,pady=9,padx=10,sticky="W")

FaceWashEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
FaceWashEntry.grid(row=2, column=1,pady=9,padx=10)


HairSprayLabel=Label(cosmeticFrame,text="Hair Spray" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
HairSprayLabel.grid(row=3, column=0,pady=9,padx=10,sticky="W")

HairSprayEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
HairSprayEntry.grid(row=3, column=1,pady=9,padx=10)


HairigelLabel=Label(cosmeticFrame,text="Hair Gel" ,font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
HairigelLabel.grid(row=4, column=0,pady=9,padx=10,sticky="W")

HairigelEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
HairigelEntry.grid(row=4, column=1,pady=9,padx=10)


bodylotionLabel=Label(cosmeticFrame,text="Body lotion", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
bodylotionLabel.grid(row=5, column=0,pady=9,padx=10,sticky="W")

bodylotionEntry=Entry(cosmeticFrame,font=("time new roman",15,"bold"),width=10,bd=5)
bodylotionEntry.grid(row=5, column=1,pady=9,padx=10)

groceryFrame=LabelFrame(productFrame,text="Grocery",font=("time new roman",15,"bold"),
                                  fg="gold",bd=8,relief=GROOVE,bg="gray20")
groceryFrame.grid(row=0,column=1)


RiceLabel=Label(groceryFrame,text="Rice", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
RiceLabel.grid(row=0, column=0,pady=9,padx=10,sticky="W")

RiceEntry=Entry(groceryFrame,font=("time new roman",15,"bold"),width=10,bd=5)
RiceEntry.grid(row=0, column=1,pady=9,padx=10)

oilLabel=Label(groceryFrame,text="Oil", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
oilLabel.grid(row=1, column=0,pady=9,padx=10,sticky="W")

oilEntry=Entry(groceryFrame,font=("time new roman",15,"bold"),width=10,bd=5)
oilEntry.grid(row=1, column=1,pady=9,padx=10)


daalLabel=Label(groceryFrame,text="Daal", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
daalLabel.grid(row=2, column=0,pady=9,padx=10,sticky="W")

daalEntry=Entry(groceryFrame,font=("time new roman",15,"bold"),width=10,bd=5)
daalEntry.grid(row=2, column=1,pady=9,padx=10)


WheatLabel=Label(groceryFrame,text="Wheat", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
WheatLabel.grid(row=3, column=0,pady=9,padx=10,sticky="W")

WheatEntry=Entry(groceryFrame,font=("time new roman",15,"bold"),width=10,bd=5)
WheatEntry.grid(row=3, column=1,pady=9,padx=10)


sugerLabel=Label(groceryFrame,text="Suger", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
sugerLabel.grid(row=4, column=0,pady=9,padx=10,sticky="W")

sugerEntry=Entry(groceryFrame,font=("time new roman",15,"bold"),width=10,bd=5)
sugerEntry.grid(row=4, column=1,pady=9,padx=10)


teaLabel=Label(groceryFrame,text="Tea", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
teaLabel.grid(row=5, column=0,pady=9,padx=10,sticky="W")

teaEntry=Entry(groceryFrame,font=("time new roman",15,"bold"),width=10,bd=5)
teaEntry.grid(row=5, column=1,pady=9,padx=10)


drinksFrame=LabelFrame(productFrame,text="Cold Drinks",font=("time new roman",15,"bold"),
                                  fg="gold",bd=8,relief=GROOVE,bg="gray20")
drinksFrame.grid(row=0,column=2)

mazaLabel=Label(drinksFrame,text="Mazza", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
mazaLabel.grid(row=0, column=0,pady=9,padx=10,sticky="W")

mazaEntry=Entry(drinksFrame,font=("time new roman",15,"bold"),width=10,bd=5)
mazaEntry.grid(row=0, column=1,pady=9,padx=10)

pepsiLabel=Label(drinksFrame,text="Pepsi", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
pepsiLabel.grid(row=1, column=0,pady=9,padx=10,sticky="W")

pepsiEntry=Entry(drinksFrame,font=("time new roman",15,"bold"),width=10,bd=5)
pepsiEntry.grid(row=1, column=1,pady=9,padx=10)

spriteLabel=Label(drinksFrame,text="Sprite", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
spriteLabel.grid(row=2, column=0,pady=9,padx=10,sticky="W")

spriteEntry=Entry(drinksFrame,font=("time new roman",15,"bold"),width=10,bd=5)
spriteEntry.grid(row=2, column=1,pady=9,padx=10)

dewLabel=Label(drinksFrame,text="Dew", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
dewLabel.grid(row=3, column=0,pady=9,padx=10,sticky="W")

dewEntry=Entry(drinksFrame,font=("time new roman",15,"bold"),width=10,bd=5)
dewEntry.grid(row=3, column=1,pady=9,padx=10)

frootiLabel=Label(drinksFrame,text="Frooti", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
frootiLabel.grid(row=4, column=0,pady=9,padx=10,sticky="W")

frootiEntry=Entry(drinksFrame,font=("time new roman",15,"bold"),width=10,bd=5)
frootiEntry.grid(row=4, column=1,pady=9,padx=10)

cocacolaLabel=Label(drinksFrame,text="Coca Cola", font=("time new roman",15,"bold"),bg="gray20"
                ,fg="white")
cocacolaLabel.grid(row=5, column=0,pady=9,padx=10,sticky="W")

cocacolaEntry=Entry(drinksFrame,font=("time new roman",15,"bold"),width=10,bd=5)
cocacolaEntry.grid(row=5, column=1,pady=9,padx=10)

billFrame=Frame(productFrame, bd=8, relief=GROOVE)

billFrame.grid(row=0, column=3, padx=10)

billarealabel=Label(billFrame, text="Label Area", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE)
billarealabel.pack(fill=X)


scrollbar=Scrollbar(billFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea=Text(billFrame, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)
root.mainloop()