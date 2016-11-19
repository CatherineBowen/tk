from tkinter import *
from Board2048 import *


def makegrid(parent, dimension=4):
    table = [[Label(parent,text="_",bg="lightgray") for _ in range(dimension)] for _ in range(dimension)]
    for r in range(len(table)):
        for c in range(len(table)):
            table[r][c].grid(row=r+1, column=c+1)
            table[r][c].config(padx=5, pady=5, width=4, height=4) 
    return table


def updategrid(board, t):
    for r in range(len(t)):
        for c in range(len(t)):
            val = board.getPos((r,c))
            if val == 0:
                t[r][c]['bg'] = "lightgray"
            elif val == 2:
                t[r][c]['bg'] = "lightblue"
            elif val == 4:
                t[r][c]['bg'] = "lightgreen"
            elif val == 8:
                t[r][c]['bg'] = "lightyellow"
            elif val == 16:
                t[r][c]['bg'] = "yellow"
            elif val == 32:
                t[r][c]['bg'] = "orange"
            elif val == 64:
                t[r][c]['bg'] = "pink"
            else:
                t[r][c]['bg'] = "red"
            t[r][c]['text'] = val

def move(board, direction):
    if direction == "left" or direction == "right":
        board.moveX(direction)
    else:
        board.moveY(direction)
    updategrid(board,table)




root = Tk()

frame1 = Frame(root)
frame1.pack()
table = makegrid(frame1)

b = Board()
b.newGame()
updategrid(b, table)

frame2 = Frame(root)
frame2.pack()

left_button = Button(frame2, text="<", command=(lambda: move(b, "left")))
up_button = Button(frame2, text="^", command=(lambda: move(b, "up")))
right_button = Button(frame2, text=">", command=(lambda: move(b, "right")))
down_button = Button(frame2, text="v", command=(lambda: move(b, "down")))

left_button.pack(side=LEFT)
up_button.pack(side=TOP)
down_button.pack(side=BOTTOM)
right_button.pack(side=RIGHT)




left = Button()

root.mainloop()
