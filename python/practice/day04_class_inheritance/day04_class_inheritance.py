#Day 4 pratice
#Topic Classes and Exception handling 

#Task 1.Create LibraryItem class to manage borrowing and returning items
class LibraryItem:          #This is parent class
    def __init__(self,title):
        self.title = title
        self.is_borrowed = False
    def borrow_item(self):             #Function to track borrowing items
        if self.is_borrowed == True:
            raise Exception(f"The item {self.title} is already borrowed") 
        else:
            self.is_borrowed = True 
            print(f"The {self.title} has been borrowed now")    
    def return_item(self):             #Function to track returning items
        if self.is_borrowed ==  False:
            raise Exception(f"The item {self.title} is not  borrowed")
        else:
            self.is_borrowed = False
            print(f"The {self.title} has been returned now")
book = LibraryItem("Harry Potter")
book.borrow_item()
book.return_item()

#Task 2.Create Book class (inherits LibraryItem) with author attribute
class Book(LibraryItem): 
    """Represents a book, inherits title and is_borrowed from LibraryItem, adds author."""
    def __init__(self,title,author):
        super().__init__(title)
        self.author = author
book = Book("The Magic Of Thinking Big", "David Schwartz")
print(book.title)
print(book.author)

#Task 3.Create Journal class (inherits LibraryItem) with issue_number attribute
class Journal(LibraryItem):
    """Represents a journal, inherits title and is_borrowed from LibraryItem, adds issue_number."""
    def __init__(self,title,issue_number):
        super().__init__(title)
        self.issue_number = issue_number
journal =Journal("Nature",50)
print(f"The journal {journal.title} has number {journal.issue_number} issue")

#Task 4.Borrow the same book twice and handle the exception
try:
    book.borrow_item()
    book.borrow_item()  #It will raise an exception
except Exception as e:
    print(e)

#Task 5. Return an un-borrowed journal and handle the exception

try:
    journal.return_item()  #It will raise an exception
except Exception as e:
    print(e)
