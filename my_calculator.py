from tkinter import *
root= Tk()
root.title("My Calci")

def write(d):
    E1.insert(16,d)
def result(r):
    E1.delete(0,END)
    E1.insert(16,r)
def delete(de):
    E1.delete(0,END)
def backspace(b):
    current=E1.get()
    E1.delete(len(current)-1,END)
    

E1=Entry(root,width=16,font="Arial 18",bd=5,justify="right")
E1.grid(row=0,column=0,columnspan=4)

Button(root,text='7',width=6,height=3,command=lambda:write('7')).grid(row=1,column=0)
Button(root,text='8',width=6,height=3,command=lambda:write('8')).grid(row=1,column=1)
Button(root,text='9',width=6,height=3,command=lambda:write('9')).grid(row=1,column=2)
Button(root,text='C',width=6,height=3,command=lambda:delete(E1)).grid(row=1,column=3)

Button(root,text='4',width=6,height=3,command=lambda:write('4')).grid(row=2,column=0)
Button(root,text='5',width=6,height=3,command=lambda:write('5')).grid(row=2,column=1)
Button(root,text='6',width=6,height=3,command=lambda:write('6')).grid(row=2,column=2)
Button(root,text='+',width=6,height=3,command=lambda:write('+')).grid(row=2,column=3)

Button(root,text='1',width=6,height=3,command=lambda:write('1')).grid(row=3,column=0)
Button(root,text='2',width=6,height=3,command=lambda:write('2')).grid(row=3,column=1)
Button(root,text='3',width=6,height=3,command=lambda:write('3')).grid(row=3,column=2)
Button(root,text='/',width=6,height=3,command=lambda:write('/')).grid(row=3,column=3)

Button(root,text='0',width=6,height=3,command=lambda:write('0')).grid(row=4,column=0)
Button(root,text='.',width=6,height=3,command=lambda:write('.')).grid(row=4,column=1)
Button(root,text='*',width=6,height=3,command=lambda:write('*')).grid(row=4,column=2)
Button(root,text='-',width=6,height=3,command=lambda:write('-')).grid(row=4,column=3)

Button(root,text='x',width=6,height=3,command=lambda:backspace(E1)).grid(row=5,column=2)
Button(root,text='=',width=6,height=3,command=lambda:result(eval(E1.get()) ) ).grid(row=5,column=3)


root.mainloop()

