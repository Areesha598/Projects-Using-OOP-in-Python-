class Library:
    @staticmethod
    def library():
        print("Hy I am a Library.All Books are store in mine")

class Book:
    def __init__(self):
        self.lst = ["The Art of Being Alone","The Art of not Overthinking","The Secret","Stop Overthinking","Don't believe Everything you Think","Dreams never come True"]
        
    @staticmethod
    def Mebook():
        print("Hy I am a Book live in Library")
        print("Who Knows the pain that flower bears in mine")

   

    def isAvailable(self,book):
        self.book = book
        print("Total Books are:",self.lst)

    
        if book in self.lst:
            print(f"Book '{book}' is available in Library")
        else:
            print(f"Sorry! Book '{book}' is not Available in Library")
    def borrow(self,book):
        self.book = book
        if book in self.lst:
           print(f"'{self.book}' is available in Library.You can borrow")
           self.lst.remove(book) 
           print("New Updated Books List is:",self.lst)
        else:
            print(f"Sorry! '{self.book}' is not available in Library")


class Fund:
    def __init__(self,fine,time):
        self.fine = fine
        self.time = time
    def Fine(self):
       if self.time > 3:
          print(f"You have to pay a fine of {self.fine}")
       else:
           print("No Fine have to be paid")
        

class LibraryMember(Book):
    def __init__(self,name):
        super().__init__()
        self.name = name 
        self.book =None
    def display(self):
        if self.book:
            print(f"{self.name} borrows {self.book}.")
        else:
            print(f"{self.name} still borrows no book")

class StudentMember(LibraryMember):
    def __init__(self, name):
        super().__init__(name)
    def discount(self,percent,price):
        self.percent = percent
        self.price = price
        dis = self.price * (self.percent/100)
        finalPrice = self.price - dis
        print(f"Student {self.name} get Discount of {self.percent}% Now U have to pay {finalPrice} Rupees.")

class TeacherMember(LibraryMember):
    def __init__(self,name):
        super().__init__(name)
    def discount(self,percent,price):
       
        self.percent = percent
        self.price = price
        dis = self.price * (self.percent/100)
        finalPrice = self.price - dis
        print(f"Teacher {self.name} get discount of {self.percent}%.Total amount is {finalPrice} Rupees.")






#------------------TEST----------------#
fnd = Fund(600,8)
fnd = Fund(600,1)
fnd.Fine()

tm = TeacherMember("ABCD")
tm.borrow("hy")
tm.isAvailable("The Secret")
tm.discount(5,1000)



bok = Book()
bok.borrow("The Secret")
bok.isAvailable("The Secret")
bok.Mebook()



st = StudentMember("XYZ")
st.borrow("Dreams never come True")
st.display()
st.discount(2,1000)


lm = LibraryMember("LMN")
lm.display()

lb = Library()
lb.library()