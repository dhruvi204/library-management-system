from click import edit


def Admin(edited_books):
    bookhandling= int(input("To add a new book press 1 \n"))
    while bookhandling==1:
        book=input("Enter the book name \n")
        book=book.lower()
        edited_books.append(book)
        again=int(input("To add more books press 1 /n To exit press 2 /n "))
        if again != 1:
            break
    return(edited_books)
        
        
            
        
        
        
    