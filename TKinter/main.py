from tkinter import Entry,Frame,Tk
root = Tk()
root.title('index')
root.geometry('900x700')
root.minsize(500,500)
root.configure(background='#15161d')

F = Frame(width=900).grid(row=1)
E = Entry(root,width=850).grid(row=2)


root.mainloop()