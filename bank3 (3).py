

from tkinter import messagebox
import tkinter as Tk
from tkinter import *
import tkinter.ttk as ttk
import pymysql
import datetime
import re
import os
class Passbook:
      def __init__(self):
            self.db=pymysql.connect('localhost','root','root','bank')
            self.cur=self.db.cursor()
            self.show()
      def show(self):
            root=Toplevel()
            #scrollbar
            scr_bar =Scrollbar(root)
            #scr_bar =Scrollbar(window) 

            #MENTION NUMBER OF COLUMNS
            w, h = root.winfo_screenwidth(), root.winfo_screenheight()
            root.geometry("%dx%d+0+0" % (w, h))

            #scrollbar
            #scr_bar =Scrollbar(root)
            #scr_bar =Scrollbar(window) 
            #MENTION NUMBER OF COLUMNS
            w, h = root.winfo_screenwidth(), root.winfo_screenheight()
            root.geometry("%dx%d+0+0" % (w, h))
            Pass_label=Label(root,text="Pass Book",font=("Arial black", 50),fg="steel blue")
            Pass_label.place(x=520,y=0)
            cols=("column1", "column2","column3", "column4", "column5", "column6")
            tree= ttk.Treeview(root, column=cols, show='headings',height=29)
            tree.heading("#1", text="Trans Id")
            tree.heading("#2", text="Date")
            tree.heading("#3", text="Reason")
            tree.heading("#4", text="Withdraw")
            tree.heading("#5", text="Deposit")
            tree.heading("#6", text="Balance")
            tree.place(x=10,y=100)

            for col in cols:
                tree.column(col, width=222, anchor="center")
            root.update()
            
            self.cur.execute('select * from trial')
            
            rows=self.cur.fetchall()
            for row in rows:
                  tree.insert("", END, values=row)
class Login:
      def __init__(self):
            self.db=pymysql.connect('localhost','root','root','bank')
            self.cur=self.db.cursor()
      def register(self):
          global register_screen
          register_screen = Toplevel(main_screen)
          register_screen.resizable(0,0)
          register_screen.title("Register")
          register_screen.geometry("300x250")
          register_screen.configure(bg="slateblue")

          global username
          global password
          global username_entry

          global password_entry
          username = StringVar()
          password = StringVar()

          Label(register_screen, text="Please enter details below", bg="greenyellow").pack()
          username_lable = Label(register_screen,bg="peachpuff", text="Username ").pack()
          username_entry = Entry(register_screen, textvariable=username,border=3)
          username_entry.pack()
          password_lable = Label(register_screen,bg="peachpuff", text="Password  ")
          password_lable.pack()
          password_entry = Entry(register_screen, textvariable=password,border=3, show='*')
          password_entry.pack()
          Button(register_screen, text="Register", width=10, height=1, bg="tomato", command = self.register_user).pack()


# Designing window for login 

      def login(self):
          global login_screen
          login_screen = Toplevel(main_screen)
          login_screen.resizable(0,0)
          login_screen.title("Login")
          login_screen.geometry("300x250")
          login_screen.configure(bg="slateblue")
          Label(login_screen, text="Please enter details below to login",bg="lime").pack()
        

          global username_verify
          global password_verify

          username_verify = StringVar()
          password_verify = StringVar()

          global username_login_entry
          global password_login_entry

          Label(login_screen,bg="peachpuff",text="Username * ").pack()
          username_login_entry = Entry(login_screen,textvariable=username_verify,border=3)
          username_login_entry.pack()
          
          Label(login_screen,bg="peachpuff", text="Password * ").pack()
          password_login_entry = Entry(login_screen, textvariable=password_verify,border=3, show= '*')
          password_login_entry.pack()
          
          logi_button=Button(login_screen, text="Login",bg="tomato", width=10, height=1, command = self.login_verify).pack()
          
# Implementing event on register button

      def register_user(self):

          username_info = username.get()
          password_info = password.get()
          row=self.cur.execute('select * from profile')
          self.cur.execute('Insert into profile values(%s,%s,%s)',(str(row+1),username_info,password_info))
          self.db.commit()
          file = open(username_info, "w")
          file.write(username_info + "\n")
          file.write(password_info)
          file.close()

          username_entry.delete(0, END)
          password_entry.delete(0, END)
          Label(register_screen, text="Registration Success",fg="green", font=("calibri", 11)).pack()
          a=messagebox.showinfo('Successful','Registration Success',parent=register_screen)
          if a:
                register_screen.destroy()
# Implementing event on login button 

      def login_verify(self):
          username1 = username_verify.get()
          password1 = password_verify.get()
          username_login_entry.delete(0, END)
          
          password_login_entry.delete(0, END)
          self.cur.execute('select pname,pass from profile')
          list_of_files = self.cur.fetchall()
          flag=False
          for row in list_of_files: 
            if username1 == row[0]:
              if password1 == row[1]:
                  self.login_sucess()
                  flag=True
                  g=GUI()
                  g.tran_main()
                  break
          print(flag)
          if flag is False:
            self.password_not_recognised()

# Designing popup for login success

      def login_sucess(self):
          messagebox.showinfo('Login Successful','Welcome')

# Designing popup for login invalid password


      def password_not_recognised(self):
          messagebox.showwarning('Not Correct','Password not correct')

# Designing popup for user not found
      """
      def user_not_found(self):
         messagebox.showerror('Not correct','User not found')
      """
# Deleting popups

      def delete_login_success(self):
          login_success_screen.destroy()
          g=GUI()
          g.tran_main()


      def delete_password_not_recognised(self):
          password_not_recog_screen.destroy()
          
          


      def delete_user_not_found_screen(self):
          
          user_not_found_screen.destroy()


# Designing Main(first) window

      def main_account_screen(self):
          global main_screen
          main_screen = Tk()
          main_screen.resizable(0,0)
          main_screen.geometry("600x550")
          main_screen.title("Account Login")
          main_screen.configure(bg="steel blue")
          Label(text="Select Your Choice",bg="mediumspringgreen", width="300", height="2", font=("Calibri", 13)).pack()
          
          Log_Button=Button(text="Login", height="2", width="30", bg="tomato",foreground="navyblue", command = self.login)
          Log_Button.place(x=195,y=150)
          
          reg_Button=Button(text="Register", height="2", width="30", bg="tomato",foreground="navyblue", command=self.register)
          reg_Button.place(x=195,y=200)

          main_screen.mainloop()


class Transaction:
      def __init__(self):
        # CONNECT TO DATABASE
        self.db = pymysql.connect("localhost","root","root","bank")
        self.conn=self.db.cursor()

      def create_table(self):
        self.conn.execute('create table %s(tid int,date Date,reason varchar(20),withdraw int,deposit int,balance int)', re.replace(name," ","_"))

      def insert_transaction(self, tid,date,reason,withdraw,deposit,balance,table,window):
        self.conn.execute('insert into '+table.replace(" ","_")+' values(%s,%s,%s,%s,%s,%s)',(str(tid),date,reason,str(withdraw),str(deposit),str(balance)))
        self.db.commit()
        window.destroy()

      def time(self):
        x = datetime.datetime.now()
        date=x.year+'/'+x.month+'/'+x.day

      def insert_customer(self):
        #For sender
        reason=""
        self.conn.execute('insert into %s values(%s,%s,%s,%s,%s)',(re.replace(name," ","_"),tid,date,reason,withdraw,deposit,balance))
        #For Receiver
        reason="From "+name
        self.conn.execute('insert into %s values(%s,%s,%s,%s,%s)',(re.replace(name," ","_"),tid,date,reason,deposit,withdraw,balanc))
        db.commit()

      def passb_print(self):
        name="Trial"
        self.conn.execute('select * from %s', re.replace(name," ","_"))

class GUI:
            
      def transaction(self):
            t=Transaction()
            #jo=TopLevel()

            jo=Tk()
            jo.geometry("650x250")
            jo.title("Bank")
            jo.resizable(0,0)
            jo.configure(bg="gold")

            id_lbl=Label(jo,text="Id:",bg="gold",font=('arial',10,'bold'))
            id_lbl.place(x=9,y=10)
            id_box=Entry(jo,width=15,border=3)
            id_box.place(x=69,y=18)

            dat_lbl=Label(jo,text="Date:",bg="gold",font=('arial',10,'bold'))
            dat_lbl.place(x=8,y=35)
            dat_box=Entry(jo,width=15,border=3)
            dat_box.place(x=69,y=40)

            bal_lbl=Label(jo,text="Balance:",bg="gold",font=('arial',10,'bold'))
            bal_lbl.place(x=0,y=62)
            bal_box=Entry(jo,width=15,border=3)
            bal_box.place(x=69,y=65)

            depo_lbl=Label(jo,text="Deposit:",bg="gold",font=('arial',10,'bold'))
            depo_lbl.place(x=3,y=85)
            depo_box=Entry(jo,width=15,border=3
                           )
            depo_box.place(x=69,y=88)

            rsn_lbl=Label(jo,text="Reason:",bg="gold",font=('arial',10,'bold'))
            rsn_lbl.place(x=3,y=105)
            rsn_box=Entry(jo,width=15,border=3)
            rsn_box.place(x=69,y=110)

            with_lbl=Label(jo,text="Withdraw:",bg="gold",font=('arial',10,'bold'))
            with_lbl.place(x=0,y=128)
            with_box=Entry(jo,width=15,border=3)
            with_box.place(x=69,y=133)

            submit_btn=Button(jo,text="Submit",bg="red",foreground="black",width=15,command=lambda: t.insert_transaction(id_box.get(),dat_box.get(),rsn_box.get(),with_box.get(),depo_box.get(),bal_box.get(),'Trial',jo))
            submit_btn.place(x=85,y=175)
            jo.mainloop()

      #global wid_depo
      #wid_depo=''
      def wid_depo(self): 
            wo=Tk()
            wo.title("Account")
            wo.resizable(0,0)
            wo.geometry('650x250')
            wo.configure(bg="slateblue")
            wid_btn = Button(wo,text="Withdraw",font=('arial',25,'bold'),background="tomato",command=self.transaction)
            wid_btn.place(x=100,y=100)

            dep_btn = Button(wo,text="Deposit",font=('arial',25,'bold'),background="tomato",command=self.transaction)
            dep_btn.place(x=350,y=100)

            wo.mainloop()


      def tran_main(self):
            
            #Put the deposit and withdraw buttons on new window 
            go=Tk()
            go.geometry('650x250')
            go.title("Bank")
            go.configure(bg="slateblue")
            #go.configure(bg='')
            go.resizable(0,0)
            #go.state('zoomed')
            tran_btn = Button(go,text="Transaction",background="tomato",font=('arial',25,'bold'),command=self.wid_depo)
            tran_btn.place(x=100,y=100)
            pass_btn = Button(go,text="Passbook",background="tomato",font=('arial',25,'bold'),command=lambda: Passbook())
            pass_btn.place(x=390,y=100)
            go.mainloop()

l=Login()
l.main_account_screen()      



      #k=wid_depo()
#
#g.transaction()
