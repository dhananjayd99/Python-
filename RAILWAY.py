# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 15:28:05 2018

@author: DHANANJAY"""

class railway:
    def General(self,generalamt):
        gen=500
        print("AMOUNT OF A SINGLE TICKET:  ",gen)
        print("AMOUNT FOR ADULT IS 500")
        print("AMOUNT FOR BELOW 12 IS 300")
        print("TICKET FOR CHILD BELOW 3 IS FREE")
        self.generalamt=generalamt
        r=0
        t=0
        y=0
        for i in range(generalamt):
            w=input("NAME OF PASSENGER:")
            z=input("GENDER:")
            x=int(input("AGE:"))
            print("NAME OF THE PASSENGER:",w)
            print("GENDER OF THE PASSENGER:",z)
            print("AGE OF THE PASSENGER:",x)
            if(x<=3):
                y+=gen-500
            elif(3<x<=12):
                r+=gen-200
            elif(x>12):
                t+=gen+0
        total=y+r+t
       
        print("total amount need to be paid:",total)
        print("total number of tickets:",self.generalamt)
    def Sleeper_class(self,generalamt):
        gen=800
        print("AMOUNT OF A SINGLE TICKET:  ",gen)
        print("AMOUNT FOR ADULT IS 800")
        print("AMOUNT FOR BELOW 12 IS 500")
        print("TICKET FOR CHILD BELOW 3 IS FREE")
        self.generalamt=generalamt
        t=0
        y=0
        r=0
        for i in range(generalamt):
            w=input("NAME OF PASSENGER:")
            z=input("GENDER:")
            x=int(input("AGE:"))
            print("NAME OF THE PASSENGER:",w)
            print("GENDER OF THE PASSENGER:",z)
            print("AGE OF THE PASSENGER:",x)
            if(x<=3):
                y+=gen-500
            elif(3<x<=12):
                r+=gen-200
            elif(x>12):
                t+=gen+0
        total=y+r+t
        
        print("total amount need to be paid:",total)
        print("total number of tickets:",generalamt)
        print("**YOU WILL BE PROVIDED WITH A BEDSHEET AND A PILLOW")
    def Third_AC_class(self,generalamt):
        gen=1200
        print("AMOUNT OF A SINGLE TICKET:  ",gen)
        print("AMOUNT FOR ADULT IS 1200")
        print("AMOUNT FOR BELOW 12 IS 1000")
        print("TICKET FOR CHILD BELOW 3 IS FREE")
        self.generalamt=generalamt
        y=0
        r=0
        t=0
        for i in range(generalamt):
            w=input("NAME OF PASSENGER:")
            z=input("GENDER:")
            x=int(input("AGE:"))
            print("NAME OF THE PASSENGER:",w)
            print("GENDER OF THE PASSENGER:",z)
            print("AGE OF THE PASSENGER:",x)
            if(x<=3):
                y+=gen-500
            elif(3<x<=12):
                r+=gen-200
            elif(x>12):
                t+=gen+0
        total=y+r+t
        
        print("total amount need to be paid:",total)
        print("total number of tickets:",generalamt)
    def Second_AC_class(self,generalamt):               
        gen=1500
        print("AMOUNT OF A SINGLE TICKET:  ",gen)
        print("AMOUNT FOR ADULT IS 1500")
        print("AMOUNT FOR BELOW 12 IS 1200")
        print("TICKET FOR CHILD BELOW 3 IS FREE")
        self.generalamt=generalamt
        y=0
        r=0
        t=0
        for i in range(generalamt):
            w=input("NAME OF PASSENGER:")
            z=input("GENDER:")
            x=int(input("AGE:"))
            print("NAME OF THE PASSENGER:",w)
            print("GENDER OF THE PASSENGER:",z)
            print("AGE OF THE PASSENGER:",x)
            if(x<=3):
                y+=gen-500
            elif(3<x<=12):
                r+=gen-200
            elif(x>12):
                t+=gen+0
        total=y+r+t
        
        print("total amount need to be paid:",total)
        print("total number of tickets:",generalamt)
    def First_AC_class(self,generalamt):
        gen=2000
        print("AMOUNT OF A SINGLE TICKET:  ",gen)
        print("AMOUNT FOR ADULT IS 2000")
        print("AMOUNT FOR BELOW 12 IS 1800")
        print("TICKET FOR CHILD BELOW 3 IS FREE")
        self.generalamt=generalamt
        y=0
        r=0
        t=0
        for i in range(generalamt):
            w=input("NAME OF PASSENGER:")
            z=input("GENDER:")
            x=int(input("AGE:"))
            print("NAME OF THE PASSENGER:",w)
            print("GENDER OF THE PASSENGER:",z)
            print("AGE OF THE PASSENGER:",x)
            if(x<=3):
                y+=gen-500
            elif(3<x<=12):
                r+=gen-200
            elif(x>12):
                t+=gen+0
        total=y+r+t
        print("total amount need to be paid:",total)
        print("total number of tickets:",generalamt)
a=railway()
print("WELCOME TO INDIA RAILWAYS")
print("Trains available are: \n DELHI TO MUMBAI \n MUMBAI TO GOA \n BANGALORE tO KERELA \n KERElA TO TAMIL NADU")
q=int(input("press 1 for DELHI TO MUMBAI\n press 2 for MUMBAI TO GOA \n press 3 for BANGLORE TO KERELA \n press 4 for KERELA TO TAMIL NADU"))
if(q==1 or q==2 or q==3 or q==4):
    k=int(input("Select 1 for booking seats and 2 for HOME SCREEN"))
    if(k==1):
        st=int(input("PRESS 1 FOR General,2 FOR Sleeper class,3 FOR Third AC class, 4 FOR Second AC class,5 FOR First AC class"))
        if(st==1):
            generalamt=int(input("ENTER NUMBER OF PASSENGERS"))
            a.General(generalamt)
        if(st==2):
            generalamt=int(input("ENTER NUMBER OF PASSENGERS"))
            a.Sleeper_class(generalamt)
        if(st==3):
            generalamt=int(input("ENTER NUMBER OF PASSENGERS"))
            a.Third_AC_class(generalamt)
        if(st==4):
            generalamt=int(input("ENTER NUMBER OF PASSENGERS"))
            a.Second_AC_class(generalamt)
        if(st==5):
            generalamt=int(input("ENTER NUMBER OF PASSENGERS"))
            a.First_AC_class(generalamt)
    else:
        print("YOU HAVE BEEN SAFELY LOGGED OUT")
if(q==1):
    print("Travelling to MUMBAI \n From DELHI")
elif(q==2):
    print("Travelling to GOA \n From MUMBAI ")
elif(q==3):
    print("Travelling to KERELA \n From BANGALORE ")
elif(q==4):
    print("Travelling to TAMIL NADU \n From KERELA")
    
    
    