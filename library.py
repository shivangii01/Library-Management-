import mysql.connector
import datetime


                                    # ---------------- Database connection ----------------
def get_connection():
    try:
        con = mysql.connector.connect(
        host="localhost",
        user="****",# replace with your db username
        password="****", # replace with your db password
        database="library_db"

        )
        cursor=con.cursor()
        return con, cursor
    except mysql.connector.Error as e:
        print("Error connecting to database:", e)
        return None, None
    
                                        # ---------------- Admin class ----------------
                                 # Admin class for library management system for security purpose
class Admin:
    def __init__(self):
        self.con,self.cursor= get_connection()
    def login (self,username,password):
        try:
            self.cursor.execute("SELECT * FROM admin WHERE username=%s AND password=%s",(username,password))
            result=self.cursor.fetchone()
            if result :
                
                return "successfully logged in"
            else:
                return False 
        except Exception as e:
              print("Error during login:", e)
            #   return False


                                    # ---------------- Book management class ----------------
                                # Book class for managing books in the library with CRUD operations
class admin_books:
    def __init__(self):
        self.con, self.cursor = get_connection()
    
        
        
    def add_books(self):

        try:
            self.title = input("Title: ")
            self.author = input("Author: ")
            self.quantity = int(input("Quantity: "))
            
            self.cursor.execute("INSERT INTO books ( title, author, quantity) VALUES (%s, %s, %s)", 
                        ( self.title, self.author, self.quantity))
            self.con.commit()
            print("Book added successfully.")    
        except Exception as e:
            print("Error adding book:", e)
        

    def view_books(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            row = self.cursor.fetchall()
            now=datetime.datetime.now()
            with open("book_list.txt","w") as file :
                file.write(f"book list till:{now}\n")
            
            
            
                for rows in row:
                        book_id, title, author, quantity = rows
                        file.write(f"Book ID : {book_id}\n")
                        file.write(f"Title    : {title}\n")
                        file.write(f"Author  : {author}\n")
                        file.write(f"Quantity   : {quantity}\n")
                        file.write("-" * 30 + "\n") 
            
        except Exception as e:
            print("Error viewing books:", e)

    def update_books(self):
        try:
            self.book_id = input("Book ID to update: ")
            self.quantity = int(input("New Quantity: "))
            self.cursor.execute("UPDATE books SET quantity=%s WHERE book_id=%s", (self.quantity, self.book_id))
            self.con.commit()
            print("Book updated successfully.")
        except Exception as e:
            print("Error updating book:", e)
    def delete_books(self):
        try:
            self.book_id = input("Book ID to DELETE: ")
            self.cursor.execute("DELETE FROM books WHERE book_id=%s", (self.book_id,))
            self.con.commit()
            print("Book deleted successfully.")
        except Exception as e:
            print("Error deleting book:", e)


                                     # ---------------- Membership class ----------------
class membership():
    def __init__(self):
        self.con, self.cursor = get_connection()
    def add_users(self):
        try:
            self.name = input("Name: ")
            self.course= input("Course: ")
            self.phone = input("Phone: ")
            self.email = input("Email: ")
        
            self.cursor.execute("INSERT INTO users ( name,course, email, phone) VALUES (%s, %s, %s,%s)", 
                        ( self.name, self.course, self.phone, self.email,))
            self.con.commit()
            print("Member added successfully.")
        except Exception as e:
            print("Error adding member:", e)

    def view_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            row = self.cursor.fetchall()
           
            now=datetime.datetime.now()
            with open("members_list.txt","w") as file :
                file.write(f"Members List as of {now}\n")
            
            
            
                for rows in row:
                        user_id, name, course, phone, email = rows
                        file.write(f"User ID : {user_id}\n")
                        file.write(f"Name    : {name}\n")
                        file.write(f"Course  : {course}\n")
                        file.write(f"Phone   : {phone}\n")
                        file.write(f"Email   : {email}\n")
                        file.write("-" * 30 + "\n") 
           
        except Exception as e:
            print("Error viewing members:", e)
    
    def search_user(self):
        try:
            user_id =int(input("ENTER USER ID TO SEARCH: "))
            self.cursor.execute("select * from users where user_id is %s"),(user_id)
            columns= self.cursor.fetchall()
            print(columns)
        except Exception as e:
            print("Error searching member:", e)

    def update_users(self):
        try:
            self.user_id = input("User ID to update: ")
            self.phone = input("New Phone: ")
            self.email = input("New Email: ")
            self.cursor.execute("UPDATE users SET phone=%s,email=%s WHERE user_id=%s", (self.phone,self.email, self.user_id))
            self.con.commit()
            print("Member updated successfully.")
        except Exception as e:
            print("Error updating member:", e)
    def delete_users(self):
        try:
            self.user_id = input("User ID to DELETE: ")
            self.cursor.execute("DELETE FROM users WHERE user_id=%s", (self.user_id,))
            self.con.commit()
            print("Member deleted successfully.")
        except Exception as e:
            print("Error deleting member:", e)
        


                               # ---------------- Library system class ----------------
class library_system:
    def __init__(self):
        self.con, self.cursor = get_connection()
    def issue_books(self):
        try:
            self.user_id = int(input("ENTER User ID: "))
            self.book_id = int(input("ENTER Book ID: "))   
            self.cursor.execute(f"select quantity from books where book_id={self.book_id}")
            result= self.cursor.fetchone()  
            if result and result[0]>0:
                self.cursor.execute("INSERT INTO issued_books ( user_id, book_id) VALUES (%s, %s)", 
                ( self.user_id, self.book_id))
                self.con.commit()
                
                self.cursor.execute(f"update books set quantity=quantity-1 where book_id ={self.book_id}")
                self.con.commit()
                name=self.cursor.execute("select name from users where user_id=%s", (self.user_id,))
                name= self.cursor.fetchone()  
                self.cursor.execute("update issued_books set issue_date= NOW() where user_id=%s and book_id=%s", (self.user_id, self.book_id))
                self.con.commit()
                print(f"Book issued successfully to NAME: {name} USER ID: {self.user_id}.")
            else:
                print("Book not available or invalid book id! \n")
        except Exception as e:
            print("Error issuing book:", e)

    def return_books(self):
        try:
            self.user_id = int(input("ENTER User ID: "))
            self.book_id = int(input("ENTER Book ID: "))   
            # check if book is issued to user
            self.cursor.execute("select book_id from issued_books  where user_id=%s and book_id=%s", (self.user_id, self.book_id))
            result= self.cursor.fetchall()  
            if not result:
                print("Invalid Book ID!")
                return
            else:
                self.cursor.execute("select issue_date from issued_books  where user_id=%s and book_id=%s", (self.user_id, self.book_id))
                issue_date= self.cursor.fetchone() [0]
                return_date=datetime.date.today()
                days_passed = (return_date - issue_date).days
                fine=0
                
                if days_passed>7:
                    fine=(days_passed-7)*10
                    print(f"your fine is {fine} ")
                    
                self.cursor.execute("update issued_books set return_date= NOW(),due_date= %s,fine = %s where user_id=%s and book_id=%s" ,(return_date,fine,self.user_id, self.book_id))
                self.cursor.execute(f"update books set quantity=quantity+1 where book_id ={self.book_id}")
                self.con.commit()
                print("Book returned successfully.")
        except Exception as e:
            print("Error returning book:", e)
            




      





