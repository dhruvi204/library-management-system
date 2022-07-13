import Users
import Admin
def book():
   while True:
    
      book_list=['harry Potter','percy Jackson','selection','hunger games']
      uinp= int(input("Press 1 for Admin /n Press 2 for User \n"))
    
      if uinp == 2:
       Users.Users(edited_book_list)
      
      if uinp==1:
       edited_book_list=Admin.Admin(book_list)
       print(edited_book_list)
    
book()
 
     
  
 
     
    
