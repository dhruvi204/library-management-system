import Users
def Return(Books):
    
    while True:
        User_Return= input("Enter the Book you want to return")
        User_Return= User_Return.lower()
        
        if User_Return in Books:
            print("The book has been returned, Thankyou")
            break
        else:
            print("Book is not listed as borrowed, please try again")
            continue
    return(User_Return)
    
        
    