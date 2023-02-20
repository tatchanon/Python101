from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox
from PIL import ImageTk, Image




#สร้างหน้าจอหลักของโปรแกรม
GUI=Tk()
GUI.title('โปรแกรมSMART FARM')#นี่คือชื่อโปรแกรม
GUI.geometry('500x500')#นี่คือขนาดของโปรแกรม
GUI.iconbitmap('C:/Users/Leowpard/Desktop/Serminar/Python/Day02/LP.ico')




#Create function
def click1():
    text='โปรดระบุสถานะการทำงานที่่ 1 :'+ e1.get()
    messagebox.showinfo('สถานะ',text)

def click2():
    text='โปรดระบุสถานะการทำงานที่่ 2'
    messagebox.showinfo('สถานะ',text)
    
def click3():
    text='โปรดระบุสถานะการทำงานที่่ 3'
    messagebox.showinfo('สถานะ',text)
    

#สร้าง Tabs
notebook = ttk.Notebook(GUI)

#สร้่าง Tabs แรก
tab1 = Frame(notebook)
tab1.pack(fill='both', expand=True)
notebook.add(tab1, text="Input")
#สร้่าง Tabs ที่สอง
tab2 = Frame(notebook)
tab2.pack(fill='both', expand=True)
notebook.add(tab2, text="เครื่องคิดเลข")

###################################
#Tab1-โปรแกรมบันทึกสถานะอุปกรณ์
###################################

my_img = ImageTk.PhotoImage(Image.open("IOTSmartFarm300x300.png"))
my_label = Label(tab1,image=my_img)
my_label.grid(row=5,column=0,columnspan=3)



#สร้าง Label
label1=Label(tab1, text='สถานะ1',font=('Angsana New',14),fg='green')
label1.grid(row=0,column=0)

label2=Label(tab1, text='สถานะ2',font=('Angsana New',14),fg='green')
label2.grid(row=1,column=0)

label3=Label(tab1, text='สถานะ3',font=('Angsana New',14),fg='green')
label3.grid(row=2,column=0)

#สร้าง Button
B1=Button(tab1, text='Input 1',fg='red',bg='white',command=click1)
B1.grid(row=0,column=2)

B2=Button(tab1, text='Input 2',fg='red',bg='white',command=click2)
B2.grid(row=1,column=2)

B3=Button(tab1, text='Input 3',fg='red',bg='white',command=click3)
B3.grid(row=2,column=2)

#สร้าง Entry
e1=Entry(tab1,width=20)
e1.insert(0,"Enter the Status")
e1.grid(row=0, column=1)

e12=Entry(tab1,width=20)
e12.insert(0,"Enter the Status")
e12.grid(row=1, column=1)

e13=Entry(tab1,width=20)
e13.insert(0,"Enter the Status")
e13.grid(row=2, column=1)


#button_quite = Button(tab1, text="Exit Program", command=GUI.quit)
#button_quite.grid(row=3,column=0, columnspan=3)


####################################
#Tab2-โปรแกรมเครื่องคิดเลข
####################################

#สร้าง Entry
e2=Entry(tab2,width=35,borderwidth=5)
e2.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#สร้าง Def
def button_click(number):
    current = e2.get()
    e2.delete(0,END)
    e2.insert(0,str(current)+ str(number))

def button_clear():
    e2.delete(0,END)

def button_add():
    first_number = e2.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e2.delete(0,END)

def button_equal():
    second_number = e2.get()
    e2.delete(0,END)
    
    if math =='addition':
        e2.insert(0,f_num + int(second_number))
    
    if math =='subtraction':  
        e2.insert(0,f_num - int(second_number))
    
    if math =='multiplication':    
        e2.insert(0,f_num * int(second_number))
    
    if math =='division':    
        e2.insert(0,f_num / int(second_number))




    

def button_subtract():
    first_number = e2.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e2.delete(0,END)


def button_multiply():
    first_number = e2.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e2.delete(0,END)

def button_divide():
    first_number = e2.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e2.delete(0,END)
    
#define Button
button_1=Button(tab2, text='1',padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(tab2, text='2',padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(tab2, text='3',padx=40,pady=20,command=lambda:button_click(3))

button_4=Button(tab2, text='4',padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(tab2, text='5',padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(tab2, text='6',padx=40,pady=20,command=lambda:button_click(6))

button_7=Button(tab2, text='7',padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(tab2, text='8',padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(tab2, text='9',padx=40,pady=20,command=lambda:button_click(9))

button_0=Button(tab2, text='0',padx=40,pady=20,command=lambda:button_click(0))
button_add=Button(tab2, text='+',padx=39,pady=20,command=button_add)
button_equal=Button(tab2, text='=',padx=86,pady=20,command=button_equal)
button_clear=Button(tab2, text='Clear',padx=77,pady=20,command=button_clear)
button_subtract=Button(tab2, text='-',padx=40,pady=20,command=button_subtract)
button_multiply=Button(tab2, text='*',padx=40,pady=20,command=button_multiply)
button_divide=Button(tab2, text='/',padx=40,pady=20,command=button_divide)


#Showing Button on Screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)
button_subtract.grid(row=10,column=0)
button_multiply.grid(row=10,column=1)
button_divide.grid(row=10,column=2)

###################################
# Show the tabs
notebook.pack(fill='both', expand=True)
# Start the event loop
GUI.mainloop()






