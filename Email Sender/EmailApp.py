import os
import smtplib
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from email import encoders
from tkinter import messagebox
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter.filedialog import askopenfilenames
## hover effect on button
class HButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
##=============================== Send Email =============================================================
  

### ======================  creating widgets =====================
def createwidget():
        #======================= USer Email ID=====================
    labelfromEmail=Label(root,text="EMAIL - ID :", bg='darkolivegreen4',font=('',12,''))
    labelfromEmail.grid(row=0,column=0,pady=5,padx=5)

    root.entryfromEmail= Entry(root,width=50,textvariable=fromEmail,bg='light gray',border=1,font=('',13,''))
    root.entryfromEmail.grid(row=0,column=1,padx=5,pady=5)
            #===============password =====================
    labelPassword=Label(root,text="PASSWORD : ", bg='darkolivegreen4',font=('',12,''))
    labelPassword.grid(row=1,column=0,pady=5,padx=5)

    root.entryPassword= Entry(root,width=50,textvariable=passwordEmail,show='*',bg='light gray',border=1,font=('',13,''))
    root.entryPassword.grid(row=1,column=1,padx=5,pady=5)
            #================= show hide Button ===================================
    root.visible=ImageTk.PhotoImage(file='visibility.png')
    root.showhideButton=HButton(root,image=root.visible,border=0, relief='flat', bg="white",cursor='hand2',command=showpassword,width=20)
    root.showhideButton.place(x=591,y=39)

    labeltoEmail=Label(root,text='TO EMAIL - ID :',bg='darkolivegreen4',font=('',12,''))
    labeltoEmail.grid(row=2,column=0,padx=5,pady=10)

    root.entrytoEmail=Entry(root,width=50,textvariable=toEmail,bg='light gray',border=1,font=('',13,''))
    root.entrytoEmail.grid(row=2,column=1,padx=5,pady=5)

    labelSubjetEmail=Label(root,text='SUBJECT : ',bg='darkolivegreen4',font=('',12,''))
    labelSubjetEmail.grid(row=3,column=0,padx=5,pady=5)

    root.entry_subjectEmail=Entry(root,width=50,textvariable=subjectEmail,font=('',13,''))
    root.entry_subjectEmail.grid(row=3,column=1,padx=5,pady=5)

    labelattachmentEmail= Label(root,text="ATTACHMENT : ",bg='darkolivegreen4',font=('',12,''))
    labelattachmentEmail.grid(row=4,column=0,padx=5,pady=5)
    
    root.entryattachmentEmail=Text(root,width=60,height=5)
    root.entryattachmentEmail.grid(row=4,column=1,padx=5,pady=5)
    
    attachmentBTN=HButton(root,text='BROWSE',command=fileBrowse,width=10, fg="red", bg="black",font=('',13,''))
    attachmentBTN.grid(row=4,column=2,padx=5,pady=5)

    labelbodyEmail= Label(root,text='Message',bg='darkolivegreen4',font=('',12,''))
    labelbodyEmail.grid(row=5,column=0,padx=5,pady=5)

    root.bodyEmail= Text(root,width=80,height=17,font=('times new roman',13,''))
    root.bodyEmail.place(x=25,y=290)

    sendEmailBTN=HButton(root,text='SEND >>', fg="purple", bg="cyan4",activeforeground='red',activebackground='black',cursor='hand2',font=('',14,''),border=0,command=sendEmail,width=10)
    sendEmailBTN.place(x=425,y=650)


    exitBTN=HButton(root,text='EXIT X',cursor='hand2',activeforeground='red',activebackground='black', fg="purple", bg="cyan4",font=('',14,''),border=0,command=emailExist,width=10)
    exitBTN.place(x=620,y=650)
    
def hidepassword():
    root.visible=ImageTk.PhotoImage(file='visibility.png')
    root.showhideButton.config(image= root.visible,cursor='hand2',command=showpassword,width=18)
    root.entryPassword.config(show='*')
        
def showpassword():
    
    root.NOvisible=ImageTk.PhotoImage(file='NOvisibility.png')
    root.showhideButton.config(image=root.NOvisible,cursor='hand2',command=hidepassword,width=20)
    root.entryPassword.config(show='')

def fileBrowse():
    root.clicked=1
    root.filename=askopenfilenames(initialdir=r'C:\Users\91972\Desktop')
    #looping through selected files 
    for files in root.filename:
        #// fectching only file name using os.path.basename() method 
        filename=os.path.basename(files)
        root.entryattachmentEmail.insert('1.0',filename+'\n')
    

def emailExist():
    MsgBox=messagebox.askquestion("Exit Application",'Are you sure you want to exit ?')
    if MsgBox=='yes':
        root.destroy()



def sendEmail():
    root.status=''
    # Fetching all the user-input parameters and storing in respective variables
    fromEmail1 = fromEmail.get()
    passwordEmail1 = passwordEmail.get()
    toEmail1 = toEmail.get()
    subjectEmail1 = subjectEmail.get()
    if fromEmail1=='' and passwordEmail1=='':
       root.status= messagebox.showerror("ERROR",'Enter  Sender Email and Password')
    elif toEmail1=='':
       root.status= messagebox.showerror('ERROR','Provide receiver Email Address')

    if root.status!='ok':
        bodyEmail1 = root.bodyEmail.get('1.0', END)

        # Creating instance of class MIMEMultipart()
        message = MIMEMultipart()
        # Storing the email details in respective fields
        message['From'] = fromEmail1
        message['To'] = toEmail1
        message['Subject'] = subjectEmail1
        # Attach message with MIME instance
        message.attach(MIMEText(bodyEmail1))

        # Iterating through the files in attachment list
        if root.clicked==1:
            for files in root.filename:
                # Opening and reading the file into attachment
                attachment = open(files, 'rb').read()
                # Creating instance of MIMEBase and naming it as emailAttach
                emailAttach = MIMEBase('application', 'octet-stream')
                # Changing the payload into encoded form
                emailAttach.set_payload(attachment)
                # Encoding the attachment into base 64
                encoders.encode_base64(emailAttach)
                # Adding headers to the files
                emailAttach.add_header('Content-Disposition', 'attachment; filename= %s' % os.path.basename(files))
                # Attaching the instane emailAttach to the message instance
                message.attach(emailAttach)
        # Sending the email with attachments
        try:
            # Create a smtp session
            print('coming to try .. connecting to server')
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            # Starting TLS for security
            smtp.starttls()
            # Authenticate the user
            smtp.login(fromEmail1, passwordEmail1)
            # Sending the email with Mulitpart message converted into string
            smtp.sendmail(fromEmail1, toEmail1, message.as_string())
            messagebox.showinfo('SUCCESS', 'EMAIL SENT TO ' + str(toEmail1))
            # Terminating the session
            logout = smtp.quit()

        # Catching authenctication error
        except smtplib.SMTPAuthenticationError:
            print(smtplib.SMTPAuthenticationError)
            messagebox.showerror('ERROR', 'INVALID USERNAME OR PASSWORD')
        # Catching connection error
        except smtplib.SMTPConnectError:
            messagebox.showerror('ERROR', 'PLEASE TRY AGAIN LATER')
        except:
            messagebox.showerror('ERROR', 'Check Internet Connection..')
            


    
   

##messagebox.showwarning("warning","please make sure you have sleep")
##messagebox.showerror("Error","NOT Allowed")
##   


root=Tk()

root.title('MY MAIL')
root.config(background='cyan4')
root.resizable(0,0)
root.iconbitmap(r'emailicon.ico')
root.geometry('790x720+280+40')
root.clicked=0
root.status=''
toEmail=StringVar()
fromEmail=StringVar()
passwordEmail=StringVar()
subjectEmail=StringVar()

# create widget
createwidget()

#infinite loop to run application
root.mainloop()


