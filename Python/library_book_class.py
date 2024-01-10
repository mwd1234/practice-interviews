# Design a Python class representing a library book. Include attributes like title, author, 
# and publication year. Implement methods to display book details and to check 
# if the book is overdue based on a specified return date.

from datetime import date, timedelta

class LibraryBook:
    
    def __init__(self, title, author, pub_year, return_date): 
        self.title = title
        self.author = author
        self.pub_year = pub_year
        self.return_date = return_date
        self.overdue_book = False
        

    def get_book_title(self):
        return f"The name of your book is {self.title}."
    
    
    def get_book_author(self):
        return f"The author of your book is {self.author}."
    
    
    def get_pub_year(self):
        return f"The publication year of your book is {self.pub_year}."
    
    
    def set_return_data(self, return_date):
        self.return_date = return_date


    def overdue_checker(self):
        return self.return_date < date.today()      


lb = LibraryBook("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, date(2024, 1, 15))

print(lb.overdue_checker())

lb.set_return_data(date.today() - timedelta(days=1))

print(lb.overdue_checker())
