from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
x=0
final_list=[] #for total bill
def push(lst):
  lst.append()
def pop(lst):
  abc=lst.pop()
  return abc
lst_M=[(" 0.Item  ","Price"),("Panadol",700,80),("Neubrol",300,9),("Zetrick",200,80),("Intamizol",200,2),("Suniplast",50,4),("Bandage",80,8),("Hydrolin",100,1),("Rejix",450,1),("Surbex Z",540,8),("Cac 1000",800,9)]
lst_D=[(" 0.Item  ","Price"),("Milk",140,50),("Eggs",180,2),("Youghurt",180,5),("Cheese",550,1),("Butter",120,5),("Bread",60,8),("Condensed Milk",100,7),("Rusk",60,5),("Barn bread",50,6),("Cream",250,6)]
lst_G=[(" 0.Item  ","Price"),("Rice",200,5),("wheat",70,5),("Pulses",150,9),("Oil",300,7),("Sugar",150,6),("Salt",50,89),("red chillies",30,7),("Turmeric",50),("Ghee",90,36),("Washing powder",50,8),('Shampoo',300,7),("Hand wash",150,9),("Mask",20,8)]
lst_Bp=[(" 0.Item  ","Price"),("Facewash",190,4),("Hair oil",300,6),("Conditioner",400,8),("Fairness cream",250,7),("Hair removal cream",80,9),("Nail Polish",4000,8),("Eye liner",500,7),("Face powder",200,89),("Foundation",2100,56),("Primer",500,60),("Eye lashes",300,5),("Nail cutter",500,9),("Body_lotion",400,3),("body spray",400,6),("Perfume",4000,7)]
lst_F=[(" 0.Item  ","Price"),("Apple",200,90),("Banana",100,9),("Orange",140,5),("Coconut",50,8),("Peach",80,6),("Mango",150,8),("Grapes",200,2),("Water melon",200,2),("Lichee",400,5),("Pineapple",300,8),("Cherry",300,7),("Grape fruit",80,9)]
lst_E=[(" 0.Item  ","Price"),("Led",40000,9),("Fridge",60000,9),("Mobile",100000,7),("Washing Machine",90000,8),("Water despenser",11000,7),("Headphones",2500,9),("Laptop",80000,9),("Tablet",60000,8),("Mobile Recharge",50,9),("Torch",500,6),("Led light",200,8),("Fan",12000,5),("Earpods",50000,8)]



def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):

        for j in range(0, n-i-1):

            if arr[j][0] > arr[j + 1][0] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
bubbleSort(lst_M)
bubbleSort(lst_D)
bubbleSort(lst_G)
bubbleSort(lst_Bp)
bubbleSort(lst_F)
bubbleSort(lst_E)
la=["a","b",'c']
def avM():
  rt = Tk()

# print item from my list
  for item in lst_M:
    w = Label(rt, text=item[0:2])
    w.pack()
  rt.mainloop()
def avD():
  rt = Tk()

# print item from my list
  for item in lst_D:
    w = Label(rt, text=item[0:2])
    w.pack()
  rt.mainloop() 
def avG():
  rt = Tk()

# print item from my list
  for item in lst_G:
    w = Label(rt, text=item[0:2])
    w.pack()
  rt.mainloop()
def avE():
  rt = Tk()

# print item from my list
  for item in lst_E:
    w = Label(rt, text=item[0:2])
    w.pack()
  rt.mainloop()
def avF():
  rt = Tk()

# print item from my list
  for item in lst_F:
    w = Label(rt, text=item[0:2])
    w.pack()
  rt.mainloop()
def avBp():
  rt = Tk()

# print item from my list
  for item in lst_Bp:
    w = Label(rt, text=item[0:2])
    w.pack()
  rt.mainloop()

def avT():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in final_list:
      w = Label(rtk, text=item)
      w.pack()
    for i in final_list:
      a=int(i[1])
      total=total+a
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid][0] < x:
            low = mid + 1
 
        elif arr[mid][0] > x:
            high = mid - 1
 
        else:
            return arr[mid][1]

    return -1

'''
def binary_search(arr,s2):


  low=0
  high=len(arr)-1
  while low<=high:
      mid=(low+high)//2
      if arr[mid][0]==s2:
          if arr[mid][2]>0:
              arr[mid]=(arr[mid][0],arr[mid][1],arr[mid][2]-1)
              return arr[mid][1]
          else:
              return "Out of stock!"
      elif arr[mid][0]>s2:
          high=mid-1
      elif arr[mid][0]<s2:
          low=mid+1
  return "Search not found!"
    
  
def cl_M():
  l=[]
  l2=[]
  def operation():
    total=0
    p=''
    lav=Label(r,text="bill")
    print(e.get())
    x=binary_search(lst_M,str(e.get()))
    print(x)
    
    if x=="Search not found!" or x=="Out of stock!":
      p=(str(e.get())+"  "+x)
      l.append(0)
    
    else:
      p=(e.get()+" has been added to your cart your new balance is ")
      l.append(x)
      l2.append(e.get()+" "+str(x))
      final_list.append((e.get(),x))
    
    for i in l:
      total=total+i
      
    lav2=Label(r,text=p +" total amount "+ str(total))
    print (l)
    print(l2)
    lav.pack()
    lav2.pack()
  def bill_F():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in l2:
      w = Label(rtk, text=item)
      w.pack()
    for i in l:
      total=total+i
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
  r=Tk()
  r.title("hello")
  e=Entry(r)
  e.pack()
  
  
  myb=Button(r,text="Enter",command=operation)
  mya=Button(r,text="Available items",command=avM)
  myc=Button(r,text="Total Bill",command=bill_F)
  myb.pack()
  mya.pack()
  myc.pack()
  

  r.mainloop()
def cl_E():
  l=[]
  l2=[]
  def operation():
    total=0
    p=''
    lav=Label(r,text="bill")
    print(e.get())
    x=binary_search(lst_E,str(e.get()))
    print(x)
    
    if x=="Search not found!" or x=="Out of stock!":
      p=(str(e.get())+" "+x)
      l.append(0)
    else:
      p=(e.get()+" has been added to your cart your new balance is ")
      l.append(x)
      l2.append(e.get()+" "+str(x))
      final_list.append((e.get(),x))
    for i in l:
      total=total+i
      
    lav2=Label(r,text=p +" total amount "+ str(total))
    print (l)
    lav.pack()
    lav2.pack()
  def bill_F():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in l2:
      w = Label(rtk, text=item)
      w.pack()
    for i in l:
      total=total+i
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
  r=Tk()
  r.title("hello")
  e=Entry(r)
  e.pack()
  
  
  myb=Button(r,text="Enter",command=operation)
  mya=Button(r,text="Available items",command=avE)
  myc=Button(r,text="Total bill", command=bill_F)
  myb.pack()
  mya.pack()
  myc.pack()
  

  r.mainloop()
  
def cl_D():
  l=[]
  l2=[]
  def operation():
    total=0
    p=''
    lav=Label(r,text="bill")
    print(e.get())
    x=binary_search(lst_D,str(e.get()))
    print(x)
    
    if x=="Search not found!" or x=="Out of stock!":
      p=(str(e.get())+" "+x)
      l.append(0)
    else:
      p=(e.get()+" has been added to your cart your new balance is ")
      l.append(x)
      l2.append(e.get()+" "+str(x))
      final_list.append((e.get(),x))
    for i in l:
      total=total+i
      
    lav2=Label(r,text=p +"total amount "+ str(total))
    print (l)
    lav.pack()
    lav2.pack()
  def bill_F():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in l2:
      w = Label(rtk, text=item)
      w.pack()
    for i in l:
      total=total+i
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
  r=Tk()
  
  r.title("hello")
  e=Entry(r)
  e.pack()
  
  
  myb=Button(r,text="Enter",command=operation)
  mya=Button(r,text="Available items",command=avD)
  myc=Button(r,text="Total bill", command=bill_F)
  myb.pack()
  mya.pack()
  myc.pack()
  

  r.mainloop()
def cl_G():
  l=[]
  l2=[]
  def operation():
    total=0
    p=''
    lav=Label(r,text="bill")
    print(e.get())
    x=binary_search(lst_G,str(e.get()))
    print(x)
    
    if x=="Search not found!" or x=="Out of stock!":
      p=(str(e.get())+" "+x)
      l.append(0)
    else:
      p=(e.get()+" has been added to your cart your new balance is ")
      l.append(x)
      l2.append(e.get()+" "+str(x))
      final_list.append((e.get(),x))
    
    for i in l:
      total=total+i
      
    lav2=Label(r,text=p +"total amount "+ str(total))
    print (l)
    lav.pack()
    lav2.pack()
  def bill_F():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in l2:
      w = Label(rtk, text=item)
      w.pack()
    for i in l:
      total=total+i
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
  r=Tk()
  r.title("hello")
  e=Entry(r)
  e.pack()
  
  
  myb=Button(r,text="Enter",command=operation)
  mya=Button(r,text="Available items",command=avG)
  myc=Button(r,text="Total bill", command=bill_F)
  myb.pack()
  mya.pack()
  myc.pack()
  

  r.mainloop()
def cl_Bp():
  l=[]
  l2=[]
  def operation():
    total=0
    p=''
    lav=Label(r,text="bill")
    print(e.get())
    x=binary_search(lst_Bp,str(e.get()))
    print(x)
    
    if x=="Search not found!" or x=="Out of stock!":
      p=(str(e.get())+" "+x)
      l.append(0)
    else:
      p=(e.get()+" has been added to your cart your new balance is ")
      l.append(x)
      l2.append(e.get()+" "+str(x))
      final_list.append((e.get(),x))

    
    for i in l:
      total=total+i
      
    lav2=Label(r,text=p +"total amount "+ str(total))
    print (l)
    lav.pack()
    lav2.pack()
  def bill_F():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in l2:
      w = Label(rtk, text=item)
      w.pack()
    for i in l:
      total=total+i
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
  r=Tk()
  r.title("hello")
  e=Entry(r)
  e.pack()
  
  
  myb=Button(r,text="Enter",command=operation)
  mya=Button(r,text="Available items",command=avBp)
  myc=Button(r,text="Total bill", command=bill_F)
  myb.pack()
  mya.pack()
  myc.pack()

  r.mainloop()
def cl_F():
  l=[]
  l2=[]
  
  def operation():
    total=0
    p=''
    lav=Label(r,text="bill")
    print(e.get())
    x=binary_search(lst_F,str(e.get()))
    print(x)
    
    if x=="Search not found!" or x=="Out of stock!":
      p=(str(e.get())+" "+x)
      l.append(0)
    else:
      p=(e.get()+" has been added to your cart your new balance is ")
      l.append(x)
      l2.append(e.get()+" "+str(x))
      final_list.append((e.get(),x))
    for i in l:
      total=total+i
    
    lav2=Label(r,text=p +"total amount "+ str(total))
    print (l)
    print(l2)
    lav.pack()
    lav2.pack()
  def bill_F():
    total=0
    rtk = Tk()
    rtk.title("Total bill ")

# print item from my list
    for item in l2:
      w = Label(rtk, text=item)
      w.pack()
    for i in l:
      total=total+i
    xa=Label(rtk,text="Total amount is "+str(total))
    xa.pack()
    rtk.mainloop()
    
    
  r=Tk()
  r.title("hello")
  e=Entry(r)
  e.pack()
  
  
  myb=Button(r,text="Enter",command=operation)
  mya=Button(r,text="Available items",command=avF)
  myc=Button(r,text="Total bill", command=bill_F)
  myb.pack()
  mya.pack()
  myc.pack()

  
  r.mainloop()
  
root=Tk()
root.title("My Sweet Mart")


img = ImageTk.PhotoImage(Image.open("jt_1_400x400.png"))
panel = Label(root, image = img)
panel.place(x=0,y=0)
#mylabel = Label(root, text="Hello world")
#mylabel1 = Label(root, text="kyu world")
meds=Button(root, text="Medicine",command=cl_M)
fruits=Button(root, text=" fresh fruits",command=cl_F)
dairy=Button(root, text="dairy products",command=cl_D)
grocery=Button(root, text='grocery',command=cl_G)
Electronics=Button(root, text='Electronic products',command=cl_E)
beauty=Button(root, text="beauty products",command=cl_Bp)
Bill=Button(root, text=" Genrate bill ",command=avT)
fruits.grid(row=1,column=0)
dairy.grid(row=0,column=0)
grocery.grid(row=0,column=1)
meds.grid(row=3,column=1)
Electronics.grid(row=4,column=1)
beauty.grid(row=4,column=0)
Bill.grid(row=2,column=0)

root.mainloop()
#print(cl_F)
