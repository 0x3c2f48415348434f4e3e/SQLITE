#1 library can have multipel books
from books import Books
import datetime
class Library(Books):
    def __init__(self, Name:str, Author:str, Rating:int,date:datetime) -> None:
        super().__init__(Name, Author, Rating)
        self.date = date