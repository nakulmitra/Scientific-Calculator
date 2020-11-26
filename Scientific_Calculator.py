import tkinter as tk
import math as m

def close():
    root.destroy()
    
def all_clear():
    ans.delete(0,"end")

def clear():
    text=ans.get()
    text=text[:-1]
    ans.delete(0,"end")
    ans.insert(0,text)
    
def sci(event):
    e=event.widget
    text=e["text"]

    eq=ans.get()

    try:
        res=""
        if("sin" in text):
            res+=str(m.sin(float(eq)))
        elif("cos" in text):
            res+=str(m.cos(float(eq)))
        elif("tan" in text):
            res+=str(m.tan(float(eq)))
        elif("sinh" in text):
            res+=str(m.sinh(float(eq)))
        elif("cosh" in text):
            res+=str(m.cosh(float(eq)))
        elif("tanh" in text):
            res+=str(m.tanh(float(eq)))
        elif("perm" in text):
            ind=eq.find(",")
            a=int(eq[:ind])
            b=int(eq[ind+1])
            res+=str(m.perm(a,b))
        elif("comb" in text):
            ind=eq.find(",")
            a=int(eq[:ind])
            b=int(eq[ind+1])
            res+=str(m.comb(a,b))
        elif("log 10" in text):
            res+=str(m.log10(float(eq)))
        elif("log 2" in text):
            res+=str(m.log2(float(eq)))
        elif("floor" in text):
            res+=str(m.floor(float(eq)))
        elif("ceil" in text):
            res+=str(m.ceil(float(eq)))
        elif("degrees" in text):
            res+=str(m.degrees(float(eq)))
        elif("radians" in text):
            res+=str(m.radians(float(eq)))
        elif("pow" in text):
            ind=eq.find(",")
            a=int(eq[:ind])
            b=int(eq[ind+1])
            res+=str(m.pow(a,b))
        elif("factorial" in text):
            res+=str(m.factorial(int(eq)))
        elif("round" in text):
            ind=eq.find(",")
            a=float(eq[:ind])
            b=int(eq[ind+1])
            res+=str(round(a,b))
        
        ans.delete(0,"end")
        ans.insert(0,res)
    
    except:
        pass
    
    
    
def op(event):
    e=event.widget
    text=e["text"]
    en=ans.get()
    try:
        if(text=="="):
            res=eval(str(en))
            
        elif(text=="sqrt"):
            res=float(en)**0.5
        
        ans.delete(0,"end")
        ans.insert(0,res)
        
    except:
        pass

def write(event):
    
    e=event.widget
    text=str(e['text'])

    if("pi" in text):
        ans.insert("end",m.pi)
    else:
        ans.insert("end",text)
    
root=tk.Tk()
root.title("Calculator")
root.config(bg="#ffff00")

ans=tk.Entry(root,justify="center")
ans.pack(side="top",padx=10,pady=10,fill="x")

f=tk.Frame()
f.pack(side="top",padx=10,fill="x")

sqrt=tk.Button(f,text="sqrt",relief="raise",width=7)
sqrt.grid(row=0,column=0)
sqrt.bind("<Button-1>",op)

mod=tk.Button(f,text="sin",relief="raise",width=7)
mod.grid(row=0,column=1)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="cos",relief="raise",width=7)
sqrt.grid(row=0,column=2)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="tan",relief="raise",width=7)
mod.grid(row=0,column=3)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="%",relief="raise",width=7)
sqrt.grid(row=1,column=0)
sqrt.bind("<Button-1>",write)

mod=tk.Button(f,text="sinh",relief="raise",width=7)
mod.grid(row=1,column=1)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="cosh",relief="raise",width=7)
sqrt.grid(row=1,column=2)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="tanh",relief="raise",width=7)
mod.grid(row=1,column=3)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="perm",relief="raise",width=7)
sqrt.grid(row=2,column=0)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="comb",relief="raise",width=7)
mod.grid(row=2,column=1)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="log 10",relief="raise",width=7)
sqrt.grid(row=2,column=2)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="log 2",relief="raise",width=7)
mod.grid(row=2,column=3)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="floor",relief="raise",width=7)
sqrt.grid(row=3,column=0)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="ceil",relief="raise",width=7)
mod.grid(row=3,column=1)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="round",relief="raise",width=7)
sqrt.grid(row=3,column=2)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="radians",relief="raise",width=7)
mod.grid(row=3,column=3)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="pi",relief="raise",width=7)
sqrt.grid(row=4,column=0)
sqrt.bind("<Button-1>",write)

mod=tk.Button(f,text="pow",relief="raise",width=7)
mod.grid(row=4,column=1)
mod.bind("<Button-1>",sci)

sqrt=tk.Button(f,text="factorial",relief="raise",width=7)
sqrt.grid(row=4,column=2)
sqrt.bind("<Button-1>",sci)

mod=tk.Button(f,text="degrees",relief="raise",width=7)
mod.grid(row=4,column=3)
mod.bind("<Button-1>",sci)

btn_frame=tk.Frame(root)
btn_frame.pack(side="top",padx=10,pady=10,fill="x")

lst=[7,4,1]

for i in range(3):
    val=lst[i]
    for j in range(3):
        bt=tk.Button(btn_frame,text=val,relief="raise",width=5)
        bt.grid(row=i,column=j)
        bt.bind("<Button-1>",write)
        val+=1


div=tk.Button(btn_frame,text="/",relief="raise",width=6)
div.grid(row=0,column=3)
div.bind("<Button-1>",write)

mul=tk.Button(btn_frame,text="*",relief="raise",width=6)
mul.grid(row=0,column=4)
mul.bind("<Button-1>",write)

add=tk.Button(btn_frame,text="+",relief="raise",width=6)
add.grid(row=1,column=3)
add.bind("<Button-1>",write)

sub=tk.Button(btn_frame,text="-",relief="raise",width=6)
sub.grid(row=1,column=4)
sub.bind("<Button-1>",write)

dot=tk.Button(btn_frame,text=".",relief="raise",width=6)
dot.grid(row=2,column=3)
dot.bind("<Button-1>",write)

equal=tk.Button(btn_frame,text="=",relief="raise",width=6)
equal.grid(row=2,column=4)
equal.bind("<Button-1>",op)

comma=tk.Button(btn_frame,text=",",relief="raise",width=5)
comma.grid(row=3,column=0)
comma.bind("<Button-1>",write)

zero=tk.Button(btn_frame,text="0",relief="raise",width=5)
zero.grid(row=3,column=1)
zero.bind("<Button-1>",write)

clear=tk.Button(btn_frame,text="Clear",relief="raise",width=5,command=clear)
clear.grid(row=3,column=2)

a_clr=tk.Button(btn_frame,text="All Clear",relief="raise",width=6,command=all_clear)
a_clr.grid(row=3,column=3)

close=tk.Button(btn_frame,text="Close",relief="raise",width=6,command=close)
close.grid(row=3,column=4)

root.mainloop()

