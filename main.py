from tkinter import  *

root=Tk()

root.title("Billing System")
root.geometry("1270x685")
root.iconbitmap('1489436625-billingdatadollarcurrency_81879 (1).ico')
headingLabel=Label(root, text="Retail Billng System", font=("times new roman", 30, 'bold')
                   ,bg="gray20",fg="gold", bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

cusomter_details_frame=LabelFrame(root, text="Customer Details", font=("time new roman",15,"bold")
                                  ,fg="gold",db=)
cusomter_details_frame.pack()
nameLabel=Label(cusomter_details_frame, text="Name")
nameLabel.grid(row=0, column=0)

root.mainloop()
