from tkinter import *

import random #random library

class Random( Frame ):
  def __init__( self ):
   Frame.__init__( self )
   self.master.title( "Random Array") #random array

   self.master.rowconfigure( 5, weight = 1 )
   self.master.columnconfigure( 5, weight = 1 )
   self.grid( sticky = W+E+N+S )


   def generator(): #Generator defined
    self.nums = []
    for x in range(0, 10):
       self.nums.append(random.randint(1, 10)) #return a random integer


       num = ''.join('%4i' % num for num in self.nums)
       self.label2 = Label( self, text=num, width=22, height=22)
       self.label2.grid(row=3, columnspan=10, sticky=W+E+N+S)

   self.button4 = Button( self,text='Generate numbers',command=generator )
   self.button4.grid( row = 2,column=1, sticky = W+E+N+S )
   
def main():
  Random().mainloop()   

if __name__ == "__main__":
  main()