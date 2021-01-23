from tkinter import *
import pandas
import random

languageFile = pandas.read_csv("ViWords/Vietnamese_Words - Sheet1.csv")
vietnamese_words = languageFile.to_dict(orient="records")
print(vietnamese_words)

def newWord():
    canvas.itemconfig(cardPosition, image=cardFront)
    global chosenWord
    chosenWord = random.choice(vietnamese_words)
    canvas.itemconfig(languageText, text="Vietnamese")
    canvas.itemconfig(printedWord, text= chosenWord["Vietnamese"])
    root.after(3000, changeCard)

def changeCard():
    canvas.itemconfig(cardPosition, image=cardBack)
    canvas.itemconfig(languageText, text="English")
    canvas.itemconfig(printedWord, text=chosenWord["English"])

root = Tk()
root.title("Vietnamese Flash Cards")
root.config(padx=30, pady=30, bg="white")

canvas = Canvas(width=800, height=530)
canvas.config(bg="white", highlightthickness=0)
cardFront = PhotoImage(file="Images/Frontside.png")
cardBack = PhotoImage(file="Images/backside.png")
cardPosition = canvas.create_image(400, 265, image=cardFront)
languageText = canvas.create_text(400, 150, text="Title", font=("Georgia", 55))
printedWord = canvas.create_text(400,250, text="chosenWord", font=("Georgia", 75, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrongImg = PhotoImage(file="Images/wrongbtnpng.png")
wrongButton = Button(image=wrongImg, highlightthickness=0, bg="white", command=newWord)
wrongButton.grid(row=1, column=0)

rightImg = PhotoImage(file="Images/checkmarkbtn.png")
rightButton = Button(image=rightImg, bg="white", highlightthickness=0, command=newWord)
rightButton.grid(row=1, column=1)

newWord()
root.after(3000, changeCard)
root.mainloop()
