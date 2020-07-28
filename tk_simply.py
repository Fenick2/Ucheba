from tkinter import *

root = Tk()
e = Entry(root, bg='yellow', width=30)
b = Button(root, text='Test text')
l = Label(root, bg='purple', fg='yellow', width=30)

def compose(event):
    x = int(e.get())
    y = 2
    a = 0
    while y < x:
        if x % y == 0:
            a = 1
            break
        y += 1
    if a:
        l['text'] = 'Составное'
    else:
        l['text'] = 'Простое'
    
    
b.bind('<Button-1>', compose)

e.pack()
b.pack()
l.pack()
root.mainloop()

