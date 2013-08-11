class Book:
    def __init__(self, isbn=-1, title="", author=""):
        self.Isbn = isbn
        self.Title = title
        self.Author = author

    def __repr__(self):
        return "< isbn:%s, title:%s, author:%s >" % (self.Isbn, self.Title, self.Author)