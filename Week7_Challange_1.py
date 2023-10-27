import tkinter
from tkinter import *

root = Tk()
root.configure(background="light grey")
root.wm_title("Word Length Counter")

inputVar1 = IntVar
inputVar2 = IntVar
global entitiyID
entitiyID = []

numberOfWords = Label(root, text="Enter Number of Words: ")
numberofWordsInput = Entry(root, textvariable=inputVar1)

numberOfWords.grid(row=0, column=0)
numberofWordsInput.grid(row=0, column=1)

def wordsDisplay():
    totalWords = int(numberofWordsInput.get())
    words = int(0)

    while words < totalWords:
        lengthOfWords = Label(root, text="Enter Word " + str(words + 1) + ":")
        wordsInput = Entry(root, textvariable=inputVar2)

        lengthOfWords.grid(row=(words+2), column=0)
        wordsInput.grid(row=(words+2), column=1)

        words += 1

        saveWords = Button(root, text="Input Words", command=insertWords)
        saveWords.grid (row=1, column=1)

def insertWords():
    totalWords = int(numberofWordsInput.get())
    words = int(0)
    listOfWords1 = []

    while words < totalWords:
        widget = root.grid_slaves(row=(words+2), column=1)
        listOfWords1.append(widget[0].get())
        words += 1


    listOfWords2 =[]
    words2 = int(0)
    while words2 < len(listOfWords1):
        listOfWords2.append(str(listOfWords1[words2])+'\n')
        words2 += 1

    with open("Word Storage.txt", "w") as file:
        file.writelines(listOfWords2)
        file.close

confirmWordsButton = Button(root, text="Confirm Words", command=wordsDisplay)
confirmWordsButton.grid(row=1, column=0)

root.mainloop()