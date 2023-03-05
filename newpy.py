
from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import font

master = Tk()
master.title('Banking App')


#function

def finish_reg():

     name = temp_name.get()
     age = temp_age.get()
     gender = temp_gender.get()
     password = temp_password.get()
     email = temp_email.get()
     
     all_accounts = os.listdir()
     
     if name == '' or age == ''or gender == '' or password == ''or email == '':
            notif.config(fg='red', text='Please fill all required fields')
            notif.config(fg='red',text='All fields required *')
            return
     for email_check in all_accounts:
                 if email == email_check:
                      notif.config(fg='red', text='Account already exists')
                      return
                 else:
                      new_file= open(email, 'w')
                      new_file.write(email+'\n')
                      new_file.write(name+'\n')
                      new_file.write(gender+'\n')
                      new_file.write(age+'\n')
                      new_file.write(password+'\n')
                      new_file.write('0')
                      new_file.close()
                      notif.config(fg='green', text='Acccount has been successfully created')
                     


def register ():
     #variables
     global temp_name
     global temp_age
     global temp_gender
     global temp_password
     global temp_email
     global notif
     
     temp_name = StringVar()
     temp_age =StringVar()
     temp_gender =StringVar()
     temp_password=StringVar()
     temp_email =StringVar()
     #register


     register_screen =Toplevel(master)
     register_screen.title('Register')
     Label(register_screen, text='Enter your details to register an account', font=('calibri', 14)).grid(row=0, sticky=N, pady=12)
     Label(register_screen, text='Name', font=('calibri', 14)).grid(row=1, sticky=W)
     Label(register_screen, text='Gender', font=('calibri', 14)).grid(row=2, sticky=W)
     Label(register_screen, text='Age', font=('calibri', 14)).grid(row=3, sticky=W)
     Label(register_screen, text='Email Address', font=('calibri', 14)).grid(row=4, sticky=W)
     Label(register_screen, text='Password', font=('calibri', 14)).grid(row=5, sticky=W)
     notif = Label(register_screen, font=('calibri', 14))
     notif.grid(row=7, sticky=N, pady=10)
   

     #enteries
     Entry(register_screen, textvariable =temp_name).grid(row=1, column=0)
     Entry(register_screen, textvariable =temp_gender).grid(row=2, column=0)
     Entry(register_screen, textvariable =temp_age).grid(row=3, column=0)
     Entry(register_screen, textvariable =temp_email).grid(row=4, column=0)
     Entry(register_screen, textvariable =temp_password, show='*').grid(row=5, column=0)
     Button(register_screen, text='Register', command = finish_reg, font = ('Calibri',12)).grid(row=6,sticky=N, pady=10 )
     
     
     























def login_session():
     global login_email
     all_accounts = os.listdir()
     login_email = temp_login_email.get()
     login_password = temp_login_password.get()

     for email in all_accounts:
        if email == login_email:
            file = open(email, "r")
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[4]
            name = file_data[1]
            
            #Account Menu
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                #Labels
                Label(account_dashboard, text= "Account Menu", font=('Calibri', 12)).grid(row=0,sticky=N, pady=10)
                Label(account_dashboard, text= "Hey "+ name, font=('Calibri', 12)).grid(row=1, sticky=N, pady=5)
                #Buttons
                Button(account_dashboard, text ='Profile', font=('calibri', 12), width=30, command= profile).grid(row=2, sticky=N, padx=10)
                Button(account_dashboard, text ='Deposit money', font=('calibri', 12), width=30, command= deposit).grid(row=3, sticky=N, padx=10)
                Button(account_dashboard, text ='Withdraw money', font=('calibri', 12), width=30, command= withdraw).grid(row=4, sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_no.config(fg="red", text="Password incorrect!!")
                return
     login_no.config(fg="red", text="No account found !!")
    

     

    
    
    
    
    




def deposit():
    #variables
     global amount
     global deposit_notif
     global current_bal
     global deposit_not
     amount =StringVar()
     file = open(login_email, 'r')
     file_data = file.read()
     user_details = file_data.split('\n')
     user_balance = user_details[5]


     deposit_screen = Toplevel(master)
     deposit_screen.title('Deposit')


     Label(deposit_screen, text = 'Deposit', font = ('Calibri', 12)).grid(row=0, sticky=N, pady=10)
     current_bal = Label(deposit_screen, text = 'Current balance : £'+user_balance, font = ('Calibri', 12))
     current_bal.grid(row=1, sticky=W)
     Label(deposit_screen, text = 'Amount: ', font = ('Calibri', 12)).grid(row=2, sticky=N, pady=10)
     deposit_notif  = Label(deposit_screen,font = ('Calibri', 12))
     deposit_notif.grid(row=4, sticky=W)
     #entry
     Entry(deposit_screen, textvariable = amount).grid(row=2, column=1)

     #Button
     Button(deposit_screen, text='Finish', font = ('Calibri', 12),command= finish).grid(row=7, sticky=W, pady=5)
def finish():
     if amount.get() =='':
          deposit_notif.config(text='Amount is required', fg='red')
          return
     if float(amount.get())<=0:
          deposit_notif.config(text='Negative currency is not accepted', fg='red')
          return
     file = open(login_email, 'r+')
     file_data =file.read()
     details = file_data.split('\n')
     current_balance = details[5]
     updated_balance = current_balance
     updated_balance= float(updated_balance) + float(amount.get())
     file_data = file_data.replace(current_balance, str(updated_balance))
     file.seek(0)
     file.truncate(0)
     file.write(file_data)
     file.close()

     current_bal.config(text='current balance : £' + str(updated_balance), fg='green')
     deposit_notif.config(text='Balance updated', fg='green')

def withdraw():
      #variables
     global withdraw_amount
     global withdraw_notif
     global current_bal
     
     withdraw_amount =StringVar()
     file = open(login_email, 'r')
     file_data = file.read()
     user_details = file_data.split('\n')
     user_balance = user_details[5]


     withdraw_screen = Toplevel(master)
     withdraw_screen.title('Withdraw')


     Label(withdraw_screen, text = 'Withdraw', font = ('Calibri', 12)).grid(row=0, sticky=N, pady=10)
     current_bal = Label(withdraw_screen, text = 'Current balance : £'+user_balance, font = ('Calibri', 12))
     current_bal.grid(row=1, sticky=W)
     Label(withdraw_screen, text = 'Amount: ', font = ('Calibri', 12)).grid(row=2, sticky=N, pady=10)
     withdraw_notif  = Label(withdraw_screen,font = ('Calibri', 12))
     withdraw_notif.grid(row=4, sticky=W)
     #entry
     Entry(withdraw_screen, textvariable = withdraw_amount).grid(row=2, column=1)

     #Button
     Button(withdraw_screen, text='Finish', font = ('Calibri', 12),command= finish_withdraw).grid(row=7, sticky=W, pady=5)


def finish_withdraw():
     if withdraw_amount.get() =='':
          withdraw_notif.config(text='Amount is required', fg='red')
          return
     if float(withdraw_amount.get())<=0:
          withdraw_notif.config(text='Negative currency is not accepted', fg='red')
          return
     file = open(login_email, 'r+')
     file_data =file.read()
     details = file_data.split('\n')
     current_balance = details[5]

     if float(withdraw_amount.get())> float(current_balance):
          withdraw_notif.config(text='Insufficient Funds', fg='red')
          return




     updated_balance = current_balance
     updated_balance= float(updated_balance) - float(withdraw_amount.get())
     file_data = file_data.replace(current_balance, str(updated_balance))
     file.seek(0)
     file.truncate(0)
     file.write(file_data)
     file.close()

     current_bal.config(text='current balance : £' + str(updated_balance), fg='green')
     withdraw_notif.config(text='Balance updated', fg='green')
def profile():
     file= open(login_email)
     file_data = file.read()
     user_details =file_data.split('\n')
     user_name =user_details[1]
     user_age =user_details[3]
     user_gender= user_details[2]
     user_email= user_details[0]
     user_balance = user_details[5]



     
     profile_screen = Toplevel(master)
     profile_screen.title('Profile')
     Label(profile_screen, text='Profile', font = ('calibri', 12)).grid(row=0, sticky=N, pady=10)
     Label(profile_screen, text='Name: '+user_name, font = ('calibri', 12)).grid(row=1, sticky=W, pady=10)
     Label(profile_screen, text='Age: '+user_age, font = ('calibri', 12)).grid(row=2, sticky=W, pady=10)
     Label(profile_screen, text='Gender: '+user_gender, font = ('calibri', 12)).grid(row=3, sticky=W, pady=10)
     Label(profile_screen, text='Email: '+user_email, font = ('calibri', 12)).grid(row=4, sticky=W, pady=10)
     Label(profile_screen, text='Balance: £'+user_balance, font = ('calibri', 12)).grid(row=5, sticky=W, pady=10) 


    
             
           
          
               
          
     
               
               
     


def login():

     #var
     global temp_login_email
     global temp_login_password
     global temp_login_name
     global login_no
     global login_screen
     temp_login_email = StringVar()
     temp_login_password = StringVar()


      #loginscreen
     login_screen = Toplevel(master)
     login_screen.title('Login')


      
     #label
     Label(login_screen, text='Login to your account', font=('Calibri',12)).grid(row=0, sticky=N, pady=10)
     Label(login_screen, text='Email Address', font=('Calibri',12)).grid(row=1, sticky=W)
     Label(login_screen, text='Password', font=('Calibri',12)).grid(row=2, sticky=W)
     login_no = Label(login_screen, font=('Calibri',14))
     login_no.grid(row=4, sticky=N)


     #Button
     Button(login_screen, text='Login', command = login_session, width=15, font=('Calibri',12)).grid(row=3, sticky=W, pady=5, padx=5)


    

     Entry(login_screen, textvariable = temp_login_email).grid(row=1, column=1, padx=5)
     Entry(login_screen, textvariable = temp_login_password, show ='*').grid(row=2, column=1, padx=5)
    

      
#image
img = Image.open('picture.jpeg')
img = img.resize((300,150))
img = ImageTk.PhotoImage(img)



#Labels
Label (master, text ='Merit Banking', font =('Calibri', 15)).grid(row=0,sticky=N, pady=10)
Label (master, text ='The best way to bank', font =('Calibri', 15)).grid(row=1,sticky=N, pady=10)
Label (master, image=img).grid(row=2, sticky=N, pady=15)


#Button
Button(master, text='Register', font=('calibri',12), width=20, command= register).grid(row=3,sticky=N)
Button(master, text='Login', font=('calibri',12), width=20, command=login).grid(row=4,sticky=N,pady=10)
   

               
                   
master.mainloop()                 





 

     
 
 


















     


