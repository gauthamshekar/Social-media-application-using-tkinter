import tkinter
from PIL import ImageTk, Image
from tkinter import ttk
import webbrowser

class PlaceholderEntry(ttk.Entry):
	def __init__(self, container, placeholder, *args, **kwargs):
		super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
		self.placeholder = placeholder
		self.insert("0", self.placeholder)
		self.bind("<FocusIn>", self._clear_placeholder)
		self.bind("<FocusOut>", self._add_placeholder)

	def _clear_placeholder(self, e):
		if self["style"] == "Placeholder.TEntry":
			self.delete("0", "end")
			self["style"] = "TEntry"

	def _add_placeholder(self, e):
		if not self.get():
			self.insert("0", self.placeholder)
			self["style"] = "Placeholder.TEntry"

def callback(url):
    webbrowser.open_new(url)


top = tkinter.Tk()
top.geometry('1350x700')
img = ImageTk.PhotoImage(file="logo.jpg")
rect1 = tkinter.Canvas(top, width=1350, height=700, bg='#3b5998')
rect1.pack()
rect = tkinter.Canvas(top, width=350, height=440, bg='#3b5998', highlightbackground='#3b5998')
rect.pack()
rect.create_image(170,30,image=img)
btn = tkinter.Button(top, text='Login', bg='#4267B2', width=30, highlightbackground='#4267B2', fg='white', bd=4, cursor="hand2")
btn1 = tkinter.Button(top, text='Sign Up', bg='#4267B2', width=30, highlightbackground='#4267B2', fg='white', bd=4, cursor="hand2")
rect1.create_rectangle(1,2,1365,70, fill='#3b5998', outline='#3b5998')
style = ttk.Style(top)

style.configure("Placeholder.TEntry", foreground="#808B96")

entry = PlaceholderEntry(top, "Email Address", width=30)
entry.pack()
rect.create_window(180,100, window=entry)
entry1 = PlaceholderEntry(top, placeholder="Password", width=30)
entry1.pack()
rect.create_window(180,130, window=entry1)

lbl1 = tkinter.Label(top, text='forgot password?', bg ='#3b5998', font="Roboto 9 bold", fg="white")
lbl2 = tkinter.Label(top, text='why friends?', bg ='#3b5998', font="Roboto 9 bold", fg="white", cursor="hand2")
lbl2.bind("<Button-1>", lambda e: callback("http://www.google.com"))
rect.place(x=475, y=200, anchor = 'nw')
rect.create_window(180,360, window=lbl1)
rect.create_window(180,390, window=lbl2)
rect.create_window(180,180, window=btn)
rect.create_window(180,240, window=btn1)
top.mainloop()
