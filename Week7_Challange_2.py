import tkinter
from tkinter import *
import statistics

root = Tk()
root.configure(background="Light Grey")
root.wm_title("Average, longest and amount of words")

wordList = []
numberOfWords = 0

with open("Word Storage.txt", "r") as words:
    line = words.readline()
    for line in words:
        line.replace("\n" , "")
        wordList.append(line)

x = []
for i in wordList:
    x.append(len(i))
res = (statistics.mean(x) / len(wordList))

numberOfWords += len(wordList) + 1

ress = max(wordList, key=len)



print("There are " + str(numberOfWords) + " Words in the file")
print("The Longest Word Is " + str(ress) + " and it is " + str(len(ress) - 1) + " Letters Long")
print("The average letters per word is: " + str(res))

numWords = Label(root, text="There are " + str(numberOfWords) + " Words in the file")
longestWord = Label(root, text="The Longest Word Is " + str(ress) + " and it is " + str(len(ress) - 1) + " Letters Long")
averageLetters = Label(root, text="The average letters per word is: " + str(res))

numWords.pack()
longestWord.pack()
averageLetters.pack()

root.mainloop()