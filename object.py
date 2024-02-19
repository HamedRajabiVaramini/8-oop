'''
simple_programming_

This code defines Book class and 
makes an object 
'''
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

# Example usage:
my_book = Book(
    title="The Great Gatsby", 
    author="F. Scott Fitzgerald", 
    genre="Classic Fiction")
print(f"Title: {my_book.title}")
print(f"Author: {my_book.author}")
print(f"Genre: {my_book.genre}")

