import datetime
class Book:
    def __init__(self,name, author):
        self.name   = name
        self.author = author
        
    def getInfo(self):
        print('Book Name :',self.name)
        print('Author Name :',self.author)

class Publisher(Book):
    publication = 'MacMillan'
    def publishDate(self):
        print('Published Date :',datetime.date.today())

publish = Publisher('Harry Porter','J.K. Rowling')
publish.getInfo()
publish.publishDate()
print('Book Publication :',publish.publication)
