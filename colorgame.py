import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple']
# list of all colours
score = 0
timeLeft = 30

# function for starting the game


def startGame(event):
    if timeLeft == 30:
        countdown()

    nextColor()

# unction to choose and display the next colour


def nextColor():
    global score
    global timeLeft

    if timeLeft > 0:
        e.focus_set()
        # if the color typed is equal to the coloe of text
        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg=str(colours[1]), text=str(colours[0]))

        scoreLabel.config(text="Score: "+str(score))

# countdown timer function


def countdown():
    global timeLeft

    # if game is in play
    if timeLeft > 0:
        # decrement the timer
        timeLeft -= 1

        # update the time left label
        timeLabel.config(text="Time left:"+str(timeLeft))
        timeLabel.after(1000, countdown)


# Driver code
root = tkinter.Tk()

root.title("ColorGame")

# setting the size of GUI
root.geometry("400x300")
# add an insruction label
instructions = tkinter.Label(
    root, text="Type in the color of the words and not the word text!", font=('Helvetica', 12))

instructions.pack()
# add a score label
scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +
                          str(timeLeft), font=('Helvetica', 12))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# add a text entry box for tping colors
e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()


e.focus_set()

# starting the GUI
root.mainloop()
