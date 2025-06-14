import tkinter as tk # its a python library used to make a gui calculator
calculation=""#its a global variable and its changes are applicable for all the functions
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)#it adds the input to the variable calculation in the form of string
    text_result.delete(1.0,"end")#clears the text field from first to the last
    text_result.insert(1.0,calculation)#write the updated from first to the last
def evaluate():
    global calculation
    try:
        result=str(eval(calculation))#evaluates the calculation using eval function
        calculation=""#empties the calculation variale
        text_result.delete(1.0,"end")#clears the expression
        text_result.insert(1.0,result)#displays result
    except:
        clear_field()#calls clear_field function
        text_result.insert(1.0,"Error") #outputs error
def clear_field():
    global calculation
    calculation=""#clears the calcualtion varaible
    text_result.delete(1.0,"end")#clears the text field
box=tk.Tk()#initializing app window
box.geometry("400x325")
text_result=tk.Text(box,height=2,width=21,font=("Arial",24))#the result box design
text_result.grid(columnspan=5)#displays the widgets in gird layout and spans across the columns
#Buttons
btn_1=tk.Button(box,text="1",command=lambda:add_to_calculation(1),width=8,font=("Arial",14))#button for number 1
btn_1.grid(row=2,column=1)#placing in the layout
btn_2=tk.Button(box,text="2",command=lambda:add_to_calculation(2),width=8,font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(box,text="3",command=lambda:add_to_calculation(3),width=8,font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(box,text="4",command=lambda:add_to_calculation(4),width=8,font=("Arial",14))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(box,text="5",command=lambda:add_to_calculation(5),width=8,font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(box,text="6",command=lambda:add_to_calculation(6),width=8,font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(box,text="7",command=lambda:add_to_calculation(7),width=8,font=("Arial",14))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(box,text="8",command=lambda:add_to_calculation(8),width=8,font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(box,text="9",command=lambda:add_to_calculation(9),width=8,font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(box,text="0",command=lambda:add_to_calculation(0),width=8,font=("Arial",14))
btn_0.grid(row=5,column=2)
btn_add=tk.Button(box,text="+",command=lambda:add_to_calculation("+"),width=8,font=("Arial",14))
btn_add.grid(row=5,column=4)
btn_sub=tk.Button(box,text="-",command=lambda:add_to_calculation("-"),width=8,font=("Arial",14))
btn_sub.grid(row=4,column=4)
btn_mul=tk.Button(box,text="*",command=lambda:add_to_calculation("*"),width=8,font=("Arial",14))
btn_mul.grid(row=3,column=4)
btn_div=tk.Button(box,text="/",command=lambda:add_to_calculation("/"),width=8,font=("Arial",14))
btn_div.grid(row=2,column=4)
btn_open=tk.Button(box,text="(",command=lambda:add_to_calculation("("),width=8,font=("Arial",14))
btn_open.grid(row=5,column=1)
btn_close=tk.Button(box,text=")",command=lambda:add_to_calculation(")"),width=8,font=("Arial",14))
btn_close.grid(row=5,column=3)
btn_equal=tk.Button(box,text="=",command=evaluate,width=12,font=("Arial",14))
btn_equal.grid(row=6,column=3,columnspan=2)
btn_clear=tk.Button(box,text="c",command=clear_field,width=12,font=("Arial",14))
btn_clear.grid(row=6,column=1,columnspan=2)
box.mainloop()#listens to the input and keeps the window opened




