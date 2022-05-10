import tkinter
from tkinter import *
from tkinter import scrolledtext 
import wikipedia
import wolframalpha
IS=Tk()
IS.title("Intelligence System")
IS.iconbitmap("tk\images\is.ico")
IS.resizable(False, False)
IS.config(background="red")
intro = Label(IS, text="Welcome to Intelligence System", font=20, bg="red")
intro.grid(row=0)
ins = Label(IS, text="Enter keywords or queries", font=10, bg="red")
ins.grid(row=1)
e = Entry(IS, width=50, bg="white")
e.grid(row=2)
res = scrolledtext.ScrolledText(IS, bg="red")
res.grid(row=5)
res.config(state=DISABLED)
def wiki():
    i = e.get().lower()
    if not i:
        return
    elif i:
        try:
            answer = wikipedia.summary(i)
            res.config(state=NORMAL)
            res.delete("1.0", END)
            res.insert(END, answer)
            res.config(state=DISABLED)
        except:
            res.config(state=NORMAL)
            res.delete("1.0", END)
            res.insert(END, "Failed find any results from Wikipedia")
            res.config(state=DISABLED)
    else:
        res.config(state=NORMAL)
        res.delete("1.0", END)
        res.insert(END, "Failed find any results from Wikipedia")
        res.config(state=DISABLED)
def wolf():
    i = e.get().lower()
    if not i:
        return
    elif i:
        try:
            app_id="8442YL-RHPH7JGJPY"
            client = wolframalpha.Client(app_id)
            result = client.query(i)
            answer = next(result.results).text
            res.config(state=NORMAL)
            res.delete("1.0", END)
            res.insert(END, answer)
            res.config(state=DISABLED)
        except:
            res.config(state=NORMAL)
            res.delete("1.0", END)
            res.insert(END, "Failed find any results from Wolfram Alpha")
            res.config(state=DISABLED)
    else:
        res.config(state=NORMAL)
        res.delete("1.0", END)
        res.insert(END, "Failed find any results from Wikipedia")
        res.config(state=DISABLED)
btn1 = Button(IS, text="Search for information from Wikipedia", command=wiki, bg="yellow")
btn1.grid(row=3)
btn2 = Button(IS, text="Search for information from Wolfram Alpha", command=wolf, bg="yellow")
btn2.grid(row=4)
IS.mainloop()


        
 
