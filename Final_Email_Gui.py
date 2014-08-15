from smtplib import *
from getpass import *
from re import *
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication
from tkFileDialog import *
from Tkinter import *
from tkMessageBox import *
import csv
import codecs
import os
from Tkinter import *
from PIL import ImageTk,Image

'''
#Server Setup
server = SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
to = 'munjalprateek31@gmail.com'
from_id = raw_input('Enter sender\'s id : ')
password = getpass('Enter password : ')
server.login(from_id,password)
server.ehlo()

msg = MIMEMultipart()

#Enter subject
sub = raw_input('Enter Subject : ')
msg['Subject']=sub
msg['From']=from_id
msg['To']=to

path = askopenfilename()
if(path!=''):
    extension = path.split('.')[1]
    FileName = (path[::-1].split('/')[0])[::-1]
    ref = open(path).read()
    attachment = MIMEApplication(ref,_subtype=extension)
    attachment.add_header('content-disposition','attachment',filename=FileName)
    msg.attach(attachment)
    print '%s Attached Successfully'%FileName

server.sendmail(from_id,[to],msg.as_string())
print 'Successfully Sent'
server.close()


'''
#GUI

filesToBeAttached =[]
index = 0
msg = MIMEMultipart()
from_id=''
password=''
subject=''

def attachCSV():
    flag = 0
    path=askopenfilename()
    extension = path.split('.')[1]
    if(extension!='csv'):
        showerror('Sorry','Please attach a Csv File Only')
        return
    FileName = (path[::-1].split('/')[0])[::-1]
    if(path!=''):
    #    f = open(path,'r')
        read = csv.reader(codecs.open(path,'rU','utf-16'))
        for email in read:
            email = "".join(email)
            if(match(r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z0-9]*$',email)==None):
                showerror('ALERT','%s Is Not A Valid E-mail,So Unable To Add'%email)
            else:
                flag = 1
                to.append(email)
    for i in to:
        print i
    if(flag==1):
        showinfo('CONGRATS','%s ATTACHED SUCCESSFULLY'%FileName)
    return

def send():
    Button(root,text='Attach Files',command=attachFiles,state='disable').place(x=70,y=400)
    for files in filesToBeAttached:
        msg.attach(files)
    print "Sending ---> ",to
    del to[0]
    print "After Deleting ---> ",to

    msg['From']=from_id
    msg['Subject']=sub.get()
    server.sendmail(from_id,to,msg.as_string())
    showinfo('CONGRATS','Successfully Sent')
    os.system('rmdir temp')
    server.close()    

def attachHtml():
    path = askopenfilename()
    if(path!=''):
        FileName = (path[::-1].split('/')[0])[::-1]
        attachment = MIMEText(open(path).read(),'html')
        filesToBeAttached.append(attachment)
        showinfo('Congrats','%s Attached Successfully'%FileName)
     
def attachFiles():
    path = askopenfilename()
    if(path!=''):
        extension = path.split('.')[1]
        FileName = (path[::-1].split('/')[0])[::-1]
        ref = open(path).read()
        attachment = MIMEApplication(ref,_subtype=extension)#+'.'+ext)
        attachment.add_header('content-disposition','attachment',filename=FileName)
        filesToBeAttached.append(attachment)
        showinfo('Congrats','%s Attached Successfully'%FileName)
        

def completedAdding():
    Entry(root,textvariable=reciever,state='disable').place(x=200,y=300)
    Button(root,text='ADD',state='disable').place(x=380,y=296)
    Button(root,text='DONE ADDING',state='disable').place(x=450,y=296)
    Button(root,text='Attach Files',command=attachFiles).place(x=70,y=400)
    Button(root,text='Attach Html',command=attachHtml).place(x=70,y=450)
    Button(root,text='SEND-MAIL',command=send).place(x=380,y=400)
    

def addReciever():    
    count=0
    rec_id = reciever.get()
    for i in to:
            if((search(rec_id,i)!=None)and(i!='')):
                    showinfo('OOPS!!!','Id Already Added')
                    return
            elif(match(r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z0-9]*$',rec_id)==None):            
                showinfo('ALERT',rec_id+' does not Exist')
                return
            else:
                    count = count + 1
                    if(count==len(to)):
                            to.append(rec_id)
                            showinfo('SUCCESS','%s ADDED SUCCESSFULLY'%rec_id)
                            return
   
def show():
    from_id = fromId.get()
    if(match(r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z0-9]*$',from_id)==None):
        showerror('ALERT','Wrong ID..!!')
        return
    password = pwd.get()
    try:
        server.login(from_id,password)
        showinfo('Authorization Successfull','You Logged in Successfully')
    except SMTPAuthenticationError:
        showerror('Authorization Failed','Sorry Wrong Password or Username')
        return
    Label(root,text='Reciever\'s Id').place(x=110,y=300)
    Entry(root,textvariable=reciever,state='normal').place(x=200,y=300)
    Entry(root,state='disable').place(x=200,y=100)
    Entry(root,state='disable').place(x=200,y=130)
    Button(root,text='Attach CSV File',command=attachCSV).place(x=380,y=340)
    Button(root,text='SUBMIT',state='disable').place(x=230,y=160)
    Button(root,text='ADD',command=addReciever).place(x=380,y=296)
    Button(root,text='DONE ADDING',command=completedAdding).place(x=450,y=296)
    Label(root,text='Subject').place(x=110,y=195)
    Entry(root,textvariable=sub).place(x=200,y=195)
    
root = Tk()

server = SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
        
to = ['']
fromId = StringVar()
sub=StringVar()
pwd = StringVar()
reciever = StringVar()
root.geometry('500x500+200+200')
root.title('AUTO-EMAIL-SENDER')

#Setting Background
img = Image.open('/home/prateek/Desktop/background.jpg')
tkimage = ImageTk.PhotoImage(img)
l1 = Label(root,image = tkimage).pack()
Label(root).pack(side = "bottom", fill = "both", expand = "yes")

#label for sender id and pwd
Label(root,text='Sender\'s id ').place(x=110,y=100)
Label(root,text='Password').place(x=110,y = 130)
Entry(root,textvariable=fromId).place(x=200,y=100)
Entry(root,textvariable=pwd,show="*").place(x=200,y=130)
Button(root,text='SUBMIT',command=show).place(x=230,y=160)

root.mainloop()

