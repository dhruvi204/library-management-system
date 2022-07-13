import Admin
import Users
def Borrow(Books):
    print(Books)
    borrowed_books=[]
    while True:
      Book_name=input("Enter the name of the book you want to borrow \n")
      Book_name=Book_name.lower()
    
      if Book_name in Books:
        borrowed_books.append(Book_name)
        Books.remove(Book_name)
        print("The book is now yours")
        break
      else:
        print("book not available please select another book \n")
        continue