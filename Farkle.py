import collections
import tkinter.messagebox
import dice
from tkinter import *
import PySimpleGUI

class MyWindow:
    def __init__(self, win):
        self.label1 = Label(win, text = "Results: ")
        self.label2 = Label(win, text="Farkle", font = ("Helvetica", 20))
        self.label3 = Label(win, text= "Score: ")

        self.button1 = Button(win, text = "Roll", font=("Helvetica", 16),command=self.roll)
        self.button1.config(height=2, width=20)
        self.button1.place(x=50, y=100)

        self.label1.place(x = 50, y = 200)
        self.label2.place(x = 50, y = 25)
        self.label3.place(x = 200, y = 250)

        self.t2 = Entry()
        self.t2.place(x = 100, y = 200)

        self.scoreButton = Entry()
        self.scoreButton.place(x = 250, y = 250)

        self.total = 0
        self.lookForNumbers = [1, 5]
        self.three = None
        self.five = None
        self.one = None

    # ------------------------------------------------------------------------------------------------------------------
    def popUp(self):
        # TODO allow for multiple pick three of \\ Low priority
        score = []
        # TODO options are movable so remake this
        optionThree = f'Hold three {self.three}'
        optionTwo = f'Hold 5'
        optionOne = f'Hold 1'

        if self.three is None:
            optionThree = None
        if self.one is None:
            optionOne = None
        if self.five is None:
            optionTwo = None

        while True:
            event, values = PySimpleGUI.Window('Choose an option', [
                [PySimpleGUI.Text('What to Hold?'), PySimpleGUI.Listbox([optionOne, optionTwo, optionThree], size=(20, 3), key='LB')],
                [PySimpleGUI.Button('Ok'), PySimpleGUI.Button('Cancel')]]).read(close=True)

            if event == 'Ok':
                print(values["LB"][0])
                if values["LB"][0] != any in self.lookForNumbers:
                    self.foundThree = True
                    print(f'You chose {values["LB"][0]}')
                    score.append(values["LB"][0])
            if event == PySimpleGUI.WIN_CLOSED or event == 'Cancel':
                break
        self.score(score)

    # ------------------------------------------------------------------------------------------------------------------
    def roll(self):
        self.t2.delete(0, "end")
        self.total = list(dice.roll("6d6"))
        for i in self.total:
            self.t2.insert(END, f"{i} ")
        self.hold()

    # ------------------------------------------------------------------------------------------------------------------
    def hold(self):
        # TODO Make pop-up when these things happen so they can choose what to hold
        self.foundThree = False
        self.three = None
        self.one = None
        self.five = None

        holdable = False
        # TODO accumulate when you have numbers here then make it where options actually work in PopUp
        for i in self.total:
            if self.total.count(i) >= 3:
                self.three = i
                holdable = True
            if any(x in self.total for x in self.lookForNumbers):
                if i == 1:
                    self.one = 1
                if i == 5:
                    self.five = 5
                holdable = True

        # TODO make certain numbers holdable due to above conditions
        if holdable:
            self.popUp()

    # ------------------------------------------------------------------------------------------------------------------
    def score(self, score):
        # TODO make it to where you can pick how many to save and accumulate score accordingly
        self.scoreButton.delete(0, "end")

        one = 0
        three = 0
        five = 0

        for number in score:
            if number in score == 5:
                five = self.five * 10
            if number in score == 1:
                one = self.one * 100
            if self.foundThree == True:
                three = self.three * 100

        currentScore = one + three + five
        self.scoreButton.insert(END, currentScore)


def main():
    win = Tk()
    myWin = MyWindow(win)
    win.title("Farkle")
    win.geometry("600x450+10+10")
    win.mainloop()

if __name__ == '__main__':
    main()

