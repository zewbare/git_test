from tkinter import *
from tkinter import messagebox
class Calculator():
	def __init__(self):
		self.window=Tk()
		self.window.title("Calculator")
		self.NF=Frame(self.window)
		self.NF.grid(row=0,column=0,columnspan=5,padx=3,pady=3)
		self.L1=Label(self.NF,text="1st Number :")
		self.L1.grid(row=0,column=1,sticky=E)	
		self.L2=Label(self.NF,text="2nd Number :")
		self.L2.grid(row=1,column=1,sticky=E)
		self.L3=Label(self.NF,text="Answer :")
		self.L3.grid(row=2,column=1,sticky=E)
		self.E1=Entry(self.NF)
		self.E1.grid(row=0,column=2)	
		self.E2=Entry(self.NF)
		self.E2.grid(row=1,column=2)	
		self.E3=Entry(self.NF)
		self.E3.grid(row=2,column=2)
		self.BF=Frame(self.window)
		self.BF.grid(row=4,column=0,columnspan=5,padx=3,pady=3)
		self.B1=Button(self.BF,text="ADD",pady=2,padx=5,bg="lightblue",command=self.addition)
		self.B1.grid(row=0,column=0,pady=2,padx=5)
		self.B2=Button(self.BF,text="SUB",pady=2,padx=5,bg="lightblue",command=self.subtraction)
		self.B2.grid(row=0,column=1,pady=2,padx=5)
		self.B3=Button(self.BF,text="MUL",pady=2,padx=5,bg="lightblue",command=self.multiplication)
		self.B3.grid(row=0,column=2,pady=2,padx=5)
		self.B4=Button(self.BF,text="DIV",pady=2,padx=5,bg="lightblue",command=self.division)
		self.B4.grid(row=0,column=3,pady=2,padx=5)
		self.B5=Button(self.BF,text="CLR",pady=2,padx=5,bg="lightblue",command=self.clear)
		self.B5.grid(row=0,column=4,pady=2,padx=5)
		self.window.mainloop()
	def addition(self):
		if(self.E1.get()=="" or self.E2.get==""):
			messagebox.showinfo('Warning!','Please enter values')
			return
		r=round(float(self.E1.get())+float(self.E2.get()),2)
		self.E3.delete(0,len(self.E3.get())-1)
		self.E3.insert(0,str(r))
	def subtraction(self):
		if(self.E1.get()=="" or self.E2.get==""):
			messagebox.showinfo('Warning!','Please enter values')
			return
		r=round(float(self.E1.get())-float(self.E2.get()),2)
		self.E3.delete(0,len(self.E3.get())-1)
		self.E3.insert(0,str(r))
	def multiplication(self):
		if(self.E1.get()=="" or self.E2.get==""):
			messagebox.showinfo('Warning!','Please enter values')
			return
		r=round(float(self.E1.get())*float(self.E2.get()),2)
		self.E3.delete(0,len(self.E3.get())-1)
		self.E3.insert(0,str(r))
	def division(self):
		if(self.E1.get()=="" or self.E2.get==""):
			messagebox.showinfo('Warning!','Please enter values')
			return
		r=round(float(self.E1.get())/float(self.E2.get()),2)
		self.E3.delete(0,len(self.E3.get())-1)
		self.E3.insert(0,str(r))
	def clear(self):
		if messagebox.askquestion('Clear','Are you sure?'):
			self.E1.delete(0,len(self.E1.get()))
			self.E2.delete(0,len(self.E2.get()))
			self.E3.delete(0,len(self.E3.get()))
if __name__=="__main__":
	Calculator()
