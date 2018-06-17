from sys import argv
from Tkinter import *
script, rot = argv
root = Tk()
root.title("ROT Solver")
root.geometry("720x250+0+0")

textArea = Text(root,height=10,width=80)
textArea.pack()
text = StringVar()


def show():
	global text,solved 
	text = textArea.get("1.0","end-1c")
	solved = ''
	for i in text:
		if ord(i) == 32:
			solved += ' '
			continue
		if ord(i) <=122 and ord(i)>=97: #logic for small alphabets
			a = ord(i)
			n = a + int(rot)
			if n > 122:
				diff = n - 122
				n = 96 + diff
			else:
				pass
			solved += chr(n)
		if ord(i) <= 90 and ord(i) >= 65:
			a = ord(i)
			n = a + int(rot)
			if n > 90:
				diff = n - 90
				n = 64 + diff
			else:
				pass
			solved += chr(n)
	print str(solved)
	
work = Button(root,text="Solve",command=lambda:show()).pack()
root.mainloop()
