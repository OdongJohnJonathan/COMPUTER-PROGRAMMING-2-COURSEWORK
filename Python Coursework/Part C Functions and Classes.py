#Part C: functions and classes

class Book:
    def __init__(self, title, author, year_published ):#We created 3 parameters to hold the information(arguments)
        self.title = title
        self.author = author
        self.year_published = year_published
        
    def BookValue(self):
        return f"Book Title: {self.title}, Book Author: {self.author}, Year Published: {self.year_published}"
    
book1 = Book("rebels", "Jonathan", 1998)
book2 = Book("originals", "Velma", 2002)
book3 = Book("angels","Rhina", 2010)

print("Printed list of created book instances")
print(book1.BookValue())
print(book2.BookValue())
print(book3.BookValue())
print(" ") #this is a space to just let the work look organized when you run the code


#The next function returns a list of books sorted in the year published
print("Printed list of books sorted by year published")
def books_sorted(books): # 'books' in this case is a parameter
    if not books:
        print("There is nothing in the list")
        return []
    return sorted(books, key=lambda book: book.year_published)

books=[book1, book2, book3]
call_function=  books_sorted(books)
for book in call_function:
    print(book.BookValue())
    
        ###############                  Part B: Iteration Techniques                    ###############   
print(" ")

#this is the for loop

print("This is the for Loop")
for book in call_function:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year Published: {book.year_published}")

print("End of the for loop")
#End of the For loop
print(" ")

# # this is the while loop
print("This is the while Loop") 
index =0 #the purpose of the index is to act as a cursor where it should start counting items from in a list
while index < len(books):
    book = books[index] # Get the book object
    print(book.BookValue())  # this call BookValue to print details
    index += 1
        
print("End of the While loop")
    
# Search for a book by title
while True:
    search_book_name = input("Enter the book (Type 'done' when Finished searching): ")
    if search_book_name == "done":
    #the purpose of done is to break the infinite while loop when you have finished searching for a book
        break
    book_found = False # We create a variable called 'book_found to check whether the book has been found'
    for book in books:
        if book.title.lower() == search_book_name.lower():
        #here we convert both the book name entered earlier and the input from the user so that they match when searching
            print(book.BookValue()) #It prints the book name if found
            book_found = True # then here it indicates that the book has been found
            break #this breaks the loop if the condition has been satisfied
    if not book_found: #this prints book not found if no match has been found
        print("Book not found.")