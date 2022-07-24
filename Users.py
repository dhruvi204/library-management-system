import Borrow
import Return
def Users(book_display):
 User_info={}
 while True:
    Customer=int(input("Press 1 for login, Press 2 for new sign up \n"))
 
    if Customer==2:
        Cust_Name=input("Enter your name \n")
        Cust_pin=int(input("Create a new pin password \n"))
        User_info[Cust_Name]=Cust_pin
        print("ID created. Login now \n")
    if Customer==1:
        print("Welcome back \n")
        temp_name=input("enter name \n")
        temp_pwd=int(input("enter pin \n"))
        if (temp_name,temp_pwd) in User_info.items():
            Borrow_Or_Return = int(input("Press 1 to borrow books \n Press 2 to return books \n"))
            if Borrow_Or_Return==1:
                Missing_Books=Borrow.Borrow(book_display)
            if Borrow_Or_Return==2:
                book_display.append(Return.Return(Missing_Books))
                
        else:
           print("Invalid, ID does not match password")

     
        
    
    
    
      