from tkinter import *
import Week9_10_Classes as CL

root = Tk()
root.configure(background="Black")
root.title("Libary item and libary book class test")

item1 = CL.LibaryItem("Bingus Explorations", "Schmungus of Bungus", "Scholastic")
item2 = CL.LibaryItem("Whearabouts of Bingus", "Flungus Munguson", "Penguin Books")
item3 = CL.LibaryItem("Bingus Sightings", "Bogur Winton", "Rubber Room Authors")

libaryItems = Label(root, text="Libary Items")
libaryItems.grid(row=0, column=0)

libaryItemNameDisplay1 = Label(root, text="Name: " + str(item1.getItemName()))
libaryItemAuthorDisplay1 = Label(root, text="Author: " + str(item1.getItemAuthor()))
libaryItemPublisherDisplay1 = Label(root, text="Publisher: " + str(item1.getItemPublisher()))

libaryItemNameDisplay1.grid(row=1, column=0)
libaryItemAuthorDisplay1.grid(row=2, column=0)
libaryItemPublisherDisplay1.grid(row=3, column=0)

libaryItemNameDisplay2 = Label(root, text="Name: " + str(item2.getItemName()))
libaryItemAuthorDisplay2 = Label(root, text="Author: " + str(item2.getItemAuthor()))
libaryItemPublisherDisplay2 = Label(root, text="Publisher: " + str(item2.getItemPublisher()))

libaryItemNameDisplay2.grid(row=1, column=1)
libaryItemAuthorDisplay2.grid(row=2, column=1)
libaryItemPublisherDisplay2.grid(row=3, column=1)

libaryItemNameDisplay3 = Label(root, text="Name: " + str(item3.getItemName()))
libaryItemAuthorDisplay3 = Label(root, text="Author: " + str(item3.getItemAuthor()))
libaryItemPublisherDisplay3 = Label(root, text="Publisher: " + str(item3.getItemPublisher()))

libaryItemNameDisplay3.grid(row=1, column=2)
libaryItemAuthorDisplay3.grid(row=2, column=2)
libaryItemPublisherDisplay3.grid(row=3, column=2)

book = CL.Book("Life of Bingus", "Wife of Bingus", "Schumgus Books", "500", False)

clearSpace = Label(root, text="                  ", background="black")
clearSpace.grid(row=3, column=3)

bookHeading = Label(root, text="Books")
bookHeading.grid(row=0, column=4)

bookName = Label(root, text="Title: " + str(book.getBookName()))
bookAuthor = Label(root, text="Author: " + str(book.getBookAuthor()))
bookPublisher = Label(root, text="Publisher: " + str(book.getBookPublisher()))
bookPages = Label(root, text="Number of Pages: " + str(book.getBookPages()))
eBookCheck = Label(root, text="Is it an eBook?" + str(book.getIf_eBook()))

bookName.grid(row=1, column=4)
bookAuthor.grid(row=2, column=4)
bookPublisher.grid(row=3, column=4)
bookPages.grid(row=4, column=4)
eBookCheck.grid(row=5, column=4)

root.mainloop()