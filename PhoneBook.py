from tkinter import *

rt = Tk()
category_menu = Menu(rt, ) # category menu what you see on top
rt.config(menu = category_menu) # here we will config menu bar
rt.configure(bg="black") 

# function to create frame for friends contacts

def friends():
	hide()
	friends_frame.pack(fill="both",expand=1)
	friends_label = Label(friends_frame,text="Friends Contacts ", font = ("Arial",12,"bold")).grid(row = 0, column=1, pady = 20, padx=50)
	friends_contacts = [	("name1","number1"),
											("name2","number2"),
											("name3","number3"),	]
	button_placement = len(friends_contacts)
	contact = StringVar()
	contact.set("tap here")
	for name, number in friends_contacts:
		Radiobutton(friends_frame, text=name, variable=contact, value=number).grid()
	# number function is used for getting the number output
	def number(value):
		mylabel = Label(friends_frame, text=value).grid(row=(button_placement)+2,column=1)
		
	mylabel = Label(friends_frame, text="select name above").grid()
	
	myButton = Button(friends_frame, text= "tap to see number",command=lambda: number(contact.get())).grid()

# function to create frame for family contacts
		
def family():
	hide()
	family_frame.pack(fill="both",expand=1) 
	family_label = Label(family_frame,text="Family Contacts ",font = ("Arial",12,"bold")).grid(row = 0, column=1, pady= 20, padx = 50)			
	family_contacts = [	("name1","number1"),
											("name2","number2"),
											("name3","number3"),	]
	button_placement = len(family_contacts)
	contact = StringVar()
	contact.set("tap here")
	for name, number in family_contacts:
		Radiobutton(family_frame, text=name, variable=contact, value=number).grid()
	def number(value):
		mylabel = Label(family_frame, text=value).grid(row=(button_placement)+2,column=1)
		
	
	mylabel = Label(family_frame, text="select name above").grid()
	
	myButton = Button(family_frame, text= "tap to see number",command=lambda: number(contact.get())).grid()
	
# function to create frame for other contacts 
def others():
	hide()
	others_frame.pack(fill="both",expand=1)
	others_label = Label(others_frame,text="other Contacts ", font = ("Arial",12,"bold")).grid(row = 0, column=1, pady = 20, padx=50)
	others_contacts = [	("name1","number1"),
											("name2","number2"),
											("name3","number3"),	]
	button_placement = len(others_contacts)
	contact = StringVar()
	contact.set("tap here")
	for name, number in others_contacts:
		Radiobutton(others_frame, text=name, variable=contact, value=number).grid()
	
	def number(value):
		mylabel = Label(others_frame, text=value).grid(row=(button_placement)+2,column=1)
		
	mylabel = Label(others_frame, text="select name above").grid()
	
	myButton = Button(others_frame, text= "tap to see number",command=lambda: number(contact.get())).grid()


# --> normally  when you shift between two frame 
# --> you will get them one by one without clearing previous screen
# --> so hide function is created to clear that previous screen 
def hide():
	friends_frame.pack_forget()
	family_frame.pack_forget()	
	others_frame.pack_forget()

# commands for menu are given below	
# command functions are defined above with their names	

friends_menu = Menu(category_menu)
category_menu.add_cascade(label="friends",menu=friends_menu)
friends_menu.add_command(label="select",command=friends)


family_menu = Menu(category_menu)
category_menu.add_cascade(label='family', menu =family_menu)
family_menu.add_command(label="select",command=family)

others_menu = Menu(category_menu)
category_menu.add_cascade(label="others",menu=others_menu)
others_menu.add_command(label="select",command=others)

exit_menu = Menu(category_menu)
category_menu.add_command(label="exit",command=rt.quit)

# home label is what you see at the start of the programm
home = Label(rt,text=" by @thatsmokshanirugutti",font=("Arial",10,"bold"),bg="black", fg="white").pack()

# frames are configured here

friends_frame = Frame(rt)
family_frame =  Frame(rt)
others_frame = Frame(rt)

rt.mainloop()