#student library management

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print("\t *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! This book has already been issued to someone else.")
            return False

    def returnBook(self, bookName):
            self.books.append(bookName)
            print("Thanks for returning this book.")
        

class Student:
    def requestBook(self):
        self.book= input("Enter the name of book you want to borrow\n")
        return self.book
    def returnBook(self):
        self.book= input("Enter the name of book you want to return\n")
        return self.book




if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Python", "PHP","Data-Structures"])
    student = Student()

    while(True):
        welcomeMsg = '''==== Welcome to Central Library ===
        Please choose an option:
        1. List all the books.
        2. Request a book.
        3. Return a book.
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter the request number:\n"))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using this library!")
            exit()
        else:
            print("Invalid Choice!")