"""
Q1a:
    Widgets are elements that make up a GUI. They can be something that the user
    sees or interacts with, or can be something more backend like containing other 
    widgets. They include Buttons, Canvas, Entry, Scrollbar and Frames.
Q1b:
    mainloop() runs the event loop, which waits for the user to do something and
    responds accordingly. It is an infinite loop; it runs until the user closes the 
    window, or presses Control-C, or does something that causes the program to quit.
Q1c:
    There are 3 of them actually: 'grid', 'pack' and 'place'.
"""
#Q2
"""
K=-0.4
When far away, dDesired-inp is negative, but fvel should be positive, hence K must
be negative :)
"""
#Q3
def compTrace(A):
    sumA=0
    for i in range(len(A)):
        sumA+=A[i][i]
    return sumA
    #return sum(A[i][i] for i in range(len(A)))
#A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
#print compTrace(A)

#Q4
def findKey(dInput,strInput):
    a=[]
    for i in dInput:
        if dInput[i]==strInput:
            a.append(i)
    a.sort()
    return a
#Q5
class Square:
    def __init__(self,x=0,y=0,sideLength=1.0):
        self.x=x
        self.y=y
        self.sideLength=sideLength
    
    def getCenter(self):
        return self.x,self.y
    def getSideLength(self):
        return self.sideLength
    def getArea(self):
        return self.sideLength**2
    def getPerimeter(self):
        return 4*self.sideLength
    def containPoint(self,px,py):
        if px<=self.x+self.sideLength/2 and px>=self.x-self.sideLength/2 and py<=self.y+self.sideLength/2 and py>=self.y-self.sideLength/2:
            return True
        return False
    def containSquare(self,inSquare):
        x,y=inSquare.getCenter()
        slength=inSquare.getSideLength()
        if x+slength/2<=self.x+self.sideLength/2 and x-slength/2>=self.x-self.sideLength/2 and y-slength/2<=self.y+self.sideLength/2 and y-slength/2>=self.y-self.sideLength/2:
            return True
        return False
#s = Square(x=1,y=1, sideLength=2.0)
#print s.getCenter()
#print s.containPoint(1,1.5)
#print s.containSquare( Square(x=1.5, y = 1, sideLength = 1))
#print s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1))

#Q6
from libdw import sm
class Elevator(sm.SM):
    def __init__(self):
        self.startState='First'
    def getNextValues(self,state,inp):
        if self.state=='First' and inp=='Up':
            nextState='Second'
        elif self.state=='Second' and inp=='Up':
            nextState='Third'
        elif self.state=='Second' and inp=='Down':
            nextState='First'
        elif self.state=='Third' and inp=='Down':
            nextState='Second'
        else:
            nextState=state
        return nextState,nextState
#e = Elevator()
#print e.transduce( ['Up', 'Up', 'Up', 'Up', 'Down', 'Down', 'Down', 'Up'])

#Q7
def countNumOpenLocker(K):
    lockerOpen=[False for i in range(K)]
    for i in range(K):
        for j in range(i,K,i+1):
            lockerOpen[j]=not lockerOpen[j]
    return sum(lockerOpen)
#print countNumOpenLocker(25)

"""
7b Answer:

The program counts the number of squares of whole numbers from 1 until K. So, if 
K=16, it will count 1,4,9,16 which gives 4. 

We will give an example to show how this works:
    For the 10th locker, if is originally closed. Then, only the numbers 1,2,5,10
    will change it's state. So, it will change from closed to open to closed to 
    open to closed. 
    So, only the number of factors of a number affect how many times it will change
    it's state, and we can only achieve an odd number of factors if the number is
    a square of another number. 
    
    So for the 25th locker, the numbers 1,5,25 can change its state, from closed to 
    open to closed to open.
"""