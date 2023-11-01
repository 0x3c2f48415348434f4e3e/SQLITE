#Allow users to Enter Name of Book, Author, Rating
class Books:
    def __init__(self,Name:str, Author: str, Rating:int) -> None:
        self.Name = Name
        self.Author = Author
        self.Rating = Rating
