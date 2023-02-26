from tkinter import*


window = Tk()
window.geometry("600x600")
window.maxsize(800,800)
window.minsize(200,200)
window.title('Profile downloadar')
#label
Label = Label(window,text= ' Hello Maryam',fg='blue',bg='black')
Label.pack()

#button

def hello():
    Label.config(text=input.get())
    
   
Button = Button(window ,text='Click here',fg='red',bg='yellow', command=hello)
Button.pack()

#input
input = Entry(window)
input.pack()


window.mainloop()