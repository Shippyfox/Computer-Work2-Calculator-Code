import tkinter as tk

def press(n):
  global expression
  global labellText
  expression = expression+n
  labellText.set(expression)

m=tk.Tk()
m.title('Main window')

expression=''
labellText=tk.StringVar()
labellText.set(expression)

labell=tk.Label(m, borderwidth=2, relief="ridge",textvariable=labellText, width=32)
labell.grid(row=0, columnspan=10)

button1=tk.Button(m, text='1', width=6, command=lambda : press('1'))
button1.grid(row=1, column=0)
button2=tk.Button(m, text='2', width=6, command=lambda : press('2'))
button2.grid(row=1, column=1)
button3=tk.Button(m, text='3', width=6, command=lambda : press('3'))
button3.grid(row=1, column=2)
button4=tk.Button(m, text='4', width=6, command=lambda : press('4'))
button4.grid(row=2, column=0)
button5=tk.Button(m, text='5', width=6, command=lambda : press('5'))
button5.grid(row=2, column=1)
button6=tk.Button(m, text='6', width=6, command=lambda : press('6'))
button6.grid(row=2, column=2)
button7=tk.Button(m, text='7', width=6, command=lambda : press('7'))
button7.grid(row=3, column=0)
button8=tk.Button(m, text='8', width=6, command=lambda : press('8'))
button8.grid(row=3, column=1)
button9=tk.Button(m, text='9', width=6, command=lambda : press('9'))
button9.grid(row=3, column=2)
button0=tk.Button(m, text='0', width=6, command=lambda : press('0'))
button0.grid(row=4, column=1)
buttonP=tk.Button(m, text='+', width=4, command=lambda : press('+'))
buttonP.grid(row=1, column=4)
buttonM=tk.Button(m, text='-', width=4, command=lambda : press('-'))
buttonM.grid(row=2, column=4)
buttonT=tk.Button(m, text='x', width=4, command=lambda : press('*'))
buttonT.grid(row=3, column=4)
buttonD=tk.Button(m, text='/', width=4, command=lambda : press('/'))
buttonD.grid(row=4, column=4)

buttonC=tk.Button(m, text='CLEAR', width=6, command=lambda : clear(''))
buttonC.grid(row=4, column=0)

def clear(n):
  global expression
  global labellText
  expression = ''
  labellText.set(expression)

buttonEqual=tk.Button(m, text='=', width=6,
command=lambda : equal())
buttonEqual.grid(row=4, column=2)
def equal():
    try:
       global expression
       global labellText
       result=str(eval(expression))
       expression = result
    except:
        result='ERROR'
        expression=' '
    labellText.set(result)

button=tk.Button(m, text='stop', width=32,
command=lambda : m.destroy())
button.grid(row=5, columnspan=10)
m.mainloop()