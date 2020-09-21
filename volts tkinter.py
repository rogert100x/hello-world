#create layouts below

from tkinter import *

#set window as the object name for tkinter
window=Tk()

def volts(i,r):
    v=i*r
    return v

def amp(v,r):
    i=v/r
    return i

def res(v,i):
    r=v/i
    return r



def click_calc():
      Vin=V.get()
      Iin=I.get()
      Rin=R.get()

      if Vin and Iin and Rin:
          Label(window,width=35,text='Only 2 to be populated - Press CLEAR to continue',bg='light green').grid(row=6,columnspan=3,sticky=EW) #message
          exit
      
      if not Vin:
             V.insert(END,str(volts(float(Iin),float(Rin)))) #insert string result into blank screen entry box
      if not Iin:
            I.insert(END,str(amp(float(Vin),float(Rin)))) #insert string result into blank screen entry box
      if not Rin: #try different method
            tempR=round(res(float(Vin),float(Iin)),3)
            R.insert(END,tempR)#insert float number blank into entry box
            #or - R.insert(END,str(res(float(Vin),float(Iin)))) #insert result into screen entry box
            
def click_clear(): #clear all entry boxes
      V.delete(0,END)
      I.delete(0,END)
      R.delete(0,END)
      Label(window,width=25,text='',bg='light green').grid(row=6,columnspan=3,sticky=EW) #clear message
                
    
def close_window():
    window.destroy()
    #exit() this will close IDLE as well


#window stuff
window.geometry("400x500")
window.title('Ohms Law calculator')
window.configure(background='light green')

#label Stuff
Label(window,width=22,text='\nOhms Law.\n\n',bg='light green',font=('bold',20,'underline')).grid(row=1,columnspan=3,sticky=EW)
Label(window,width=22,text='\nPopulate 2 boxes to calculate the third.\n\n',bg='light green',font=('bold',15,'underline')).grid(row=2,columnspan=3,sticky=EW)
Label(window,width=10,text='Volts',bg='red', font=('bold',15)).grid(row=3,column=0,sticky=W)
Label (window,width=10,text='Amps',bg='light blue',font=('bold',15)).grid(row=3,column=1,sticky=W)
Label (window,width=10,text='Ohms',bg='green',font=('bold',15)).grid(row=3,column=2,sticky=W)

#entry boxes
V=Entry(window,width=11,bg='light grey',relief='sunken',font=('bold',15),justify=CENTER)
V.grid(row=5,column=0,sticky=EW)

I=Entry(window,width=11,bg='light grey',relief='sunken',font=('bold',15),justify=CENTER)
I.grid(row=5,column=1,sticky=EW)

R=Entry(window,width=11,bg='light grey',relief='sunken',font=('bold',15),justify=CENTER)
R.grid(row=5,column=2,sticky=EW)


#create submit & quit & clear buttons
Label (window,width=25,text='',bg='light green').grid(row=6,columnspan=2,sticky=EW) #blank line
Button(window, text="Submit",bg="grey",  width=6, command=click_calc).grid(row=7,column=0,sticky=EW)
Button(window, text="Clear", bg="white", width=6, command=click_clear).grid(row=7,column=1,sticky=EW)
Button(window, text="Exit", bg="white", width=6, command=close_window).grid(row=7,column=2,sticky=EW)



#KEEP THE WINDOW ALIVE WITH THIS LOOP
window.mainloop()
