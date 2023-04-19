from tkinter import Tk,Label,Entry,Button

root = Tk()
root.geometry('800x800')
root.title('generateur pass word')
label = Label(root,text='Bienvenue')
entrer = Entry(root,width=30)
bouton = Button(root,text='générer',command=root.destroy)


entrer.pack()
label.pack()
root.mainloop()