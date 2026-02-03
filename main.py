from library import Admin, admin_books, membership, library_system

def main():
    print("-----Welcome to the Library Management System-----")
    user_type = input("Are you an Admin or Member? (A/M): ").upper()

    if user_type == 'A':
        username = input("Username: ")
        password = eval(input("Password: "))
        admin = Admin()
        
        login_result = admin.login(username, password)
        if login_result == "successfully logged in":
            print("Admin logged in successfully.")
            choice = input("YOU WANT TO MANAGE MEMBERS OR MANAGE BOOKS: ").upper()
            if choice == "BOOKS":
                book_manager = admin_books()
                
                choice = input("Enter your choice (add/view/update/delete/exit): ").lower()
                if choice == "add":
                        book_manager.add_books() 
                elif choice == "view":
                        book_manager.view_books()
                elif choice == "update":
                        book_manager.update_books()
                elif choice == "delete":
                        book_manager.delete_books()
                elif choice == "exit":
                        print("Exiting admin menu.")
                        
                else:
                        print("Invalid choice!")

            elif choice == "MEMBERS":
                member = membership()
                
                print("\n--- USER MENU ---")
                print("1. Add User")
                print("2. View Users")
                print("3. Search User")
                print("4. Update User")
                print("5. Delete User")
                print("6. Back")
                m_choice = input("  ENTER YOUR CHOICE: ").lower()
            
                if m_choice == "register":
                    member.add_users()
                elif m_choice == "view":
                    member.view_users()
                elif m_choice == "search user":
                    member.search_user()
                elif m_choice == "update":
                    member.update_users()
                elif m_choice == "delete":
                    member.delete_users() 
                elif m_choice == "exit":
                    print("Exiting member menu.")
                    
            else:
                print("Invalid choice!")
        else:
            print("Login failed. Please check your credentials.")

    elif user_type == 'M':
        library = library_system()
        print("\n--- LIBRARY MENU ---")
        print("1. Issue Book")
        print("2. Return Book") 
        l_choice = input("Choose 1 or 2 : ")
        if l_choice == "1":
            library.issue_books()
        elif l_choice == "2":
            library.return_books()
    else:
        print("Invalid user type! Please enter 'A' for Admin or 'M' for Member.")

main()          