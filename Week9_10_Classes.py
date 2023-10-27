class LibaryItem:
    def __init__(self, name, author, publisher):
        self.__name = name
        self.__author = author
        self.__publisher = publisher

    def setItemName(self, name):
        self.__name = name

    def setItemAuthor(self, author):
        self.__author = author

    def setItemPublisher(self, publisher):
        self.__publisher = publisher

    def getItemName(self):
        return self.__name

    def getItemAuthor(self):
        return self.__author

    def getItemPublisher(self):
        return self.__publisher

class Book:
    def __init__(self, title, author, publisher, pages, ebook):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__pages = pages
        self.__ebook = ebook

    def setBookName(self, title):
        self.__title = title

    def setBookAuthor(self, author):
        self.__author = author

    def setBookPublisher(self, publisher):
        self.__publisher = publisher

    def setBookPages(self, pages):
        self.__pages = pages

    def setIf_eBook(self, ebook):
        self.__ebook = ebook

    def getBookName(self):
        return self.__title

    def getBookAuthor(self):
        return self.__author

    def getBookPublisher(self):
        return self.__publisher

    def getBookPages(self):
        return self.__pages

    def getIf_eBook(self):
        return self.__ebook
