from tkinter import *
from math import *
frame=Tk()

def equals():
    val=e1.get()
    val=eval(val)
    e1.delete(0,END)
    e1.insert(END,val)
frame.title('calculator')
frame.geometry('400x400')

def back():
    val=e1.get()
    val=val[:len(val)-1]
    e1.delete(0,END)
    e1.insert(0,val)
e1=Entry(frame,font=('Times New Roman',20),width=40)
e1.place(relx=0.0,rely=0.0)

def AC():
    e1.delete(0,END)
#button
one=Button(frame,text='1',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 1))
one.place(relx=0.0,rely=0.09)

two=Button(frame,text='2',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 2))
two.place(relx=0.20,rely=0.09)

three=Button(frame,text='3',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 3))
three.place(relx=0.40,rely=0.09)

four=Button(frame,text='4',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 4))
four.place(relx=0.60,rely=0.09)

five=Button(frame,text='5',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 5))
five.place(relx=0.80,rely=0.09)

six=Button(frame,text='6',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 6))
six.place(relx=0.0,rely=0.18)

seven=Button(frame,text='7',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 7))
seven.place(relx=0.20,rely=0.18)

eight=Button(frame,text='8',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 8))
eight.place(relx=0.40,rely=0.18)

nine=Button(frame,text='9',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 9))
nine.place(relx=0.60,rely=0.18)

zero=Button(frame,text='0',width=9,fg='white',bg='black',command=lambda:e1.insert(END, 0))
zero.place(relx=0.80,rely=0.18)

plus=Button(frame,text='+',width=9,fg='white',bg='black',command=lambda:e1.insert(END,'+'))
plus.place(relx=0.00,rely=0.27)

equal=Button(frame,text='=',width=9,fg='white',bg='black',command=equals)
equal.place(relx=0.20,rely=0.27)

back=Button(frame,text='<--',width=9,fg='white',bg='black',command=back)
back.place(relx=0.40,rely=0.27)

sine=Button(frame,text='sin',width=9,fg='white',bg='black',command=lambda:e1.insert(END,'sin'))
sine.place(relx=0.80,rely=0.27)

cos=Button(frame,text='cos',width=9,fg='white',bg='black',command=lambda:e1.insert(END,'cos'))
cos.place(relx=0.60,rely=0.27)

leftbracket=Button(frame,text='(',width=9,fg='white',bg='black',command=lambda:e1.insert(END,'('))
leftbracket.place(relx=0.00,rely=0.36)

rightbracket=Button(frame,text=')',width=9,fg='white',bg='black',command=lambda:e1.insert(END,')'))
rightbracket.place(relx=0.20,rely=0.36)

allclear=Button(frame,text='AC',width=9,fg='white',bg='black',command=AC)
allclear.place(relx=0.80,rely=0.36)

divide=Button(frame,text='/',width=9,fg='white',bg='black',command=lambda:e1.insert(END,'/'))
divide.place(relx=0.40,rely=0.36)

multiply=Button(frame,text='*',width=9,fg='white',bg='black',command=lambda:e1.insert(END,'*'))
multiply.place(relx=0.60,rely=0.36)



frame.mainloop()