from tkinter import *

class CalcUI():
    def __init__(self):
        self.num = [0,0,0]
        self.len = 1
        self.whichNum = 0
        self.operand = 0
        self.isFloat = 0
        self.fractNum = 0
        self.fract = 0.1
        self.initUI()


    def initUI(self):
        self.root = Tk()
        self.numFrame = Frame(self.root)
        b0 = Button(self.numFrame, text="0")
        b1 = Button(self.numFrame, text="1")
        b2 = Button(self.numFrame, text="2")
        b3 = Button(self.numFrame, text="3")
        b4 = Button(self.numFrame, text="4")
        b5 = Button(self.numFrame, text="5")
        b6 = Button(self.numFrame, text="6")
        b7 = Button(self.numFrame, text="7")
        b8 = Button(self.numFrame, text="8")
        b9 = Button(self.numFrame, text="9")
        bplus = Button(self.numFrame, text = "+")
        bminus = Button(self.numFrame, text = "-")
        bmult = Button(self.numFrame, text = "*")
        bdiv = Button(self.numFrame, text = "/")
        bequal = Button(self.numFrame, text = "=")
        bclear = Button(self.numFrame, text="C")
        bfraction = Button(self.numFrame, text=".")
        bdellast = Button(self.numFrame, text="B")


        self.numDis = Label(self.root, width=10, height=2, text="0", anchor="e", borderwidth=2, relief="groove")

        b0.grid(row=4, column=2)
        b1.grid(row=1, column=1)
        b2.grid(row=1, column=2)
        b3.grid(row=1, column=3)
        b4.grid(row=2, column=1)
        b5.grid(row=2, column=2)
        b6.grid(row=2, column=3)
        b7.grid(row=3, column=1)
        b8.grid(row=3, column=2)
        b9.grid(row=3, column=3)
        bequal.grid(row=4, column=3)
        bplus.grid(row=1, column=4)
        bminus.grid(row=2, column=4)
        bmult.grid(row=3, column=4)
        bdiv.grid(row=4, column=4)
        bfraction.grid(row=4, column=1)
        bclear.grid(row=1, column=5)
        bdellast.grid(row=2,column=5)

        b0.bind('<Button -1>', self.numClk)
        b1.bind('<Button -1>', self.numClk)
        b2.bind('<Button -1>', self.numClk)
        b3.bind('<Button -1>', self.numClk)
        b4.bind('<Button -1>', self.numClk)
        b5.bind('<Button -1>', self.numClk)
        b6.bind('<Button -1>', self.numClk)
        b7.bind('<Button -1>', self.numClk)
        b8.bind('<Button -1>', self.numClk)
        b9.bind('<Button -1>', self.numClk)
        bplus.bind('<Button -1>', self.operationClk)
        bminus.bind('<Button -1>', self.operationClk)
        bequal.bind('<Button -1>', self.operationClk)
        bmult.bind('<Button -1>', self.operationClk)
        bdiv.bind('<Button -1>', self.operationClk)
        bfraction.bind('<Button - 1>', self.toFloat)
        bclear.bind('<Button - 1>', self.Clear)
        bdellast.bind('<Button - 1>', self.delLast)

        self.numDis.pack(side=TOP)
        self.numFrame.pack()
        self.root.mainloop()

    def numClk(self, event):

        if (self.num[self.whichNum] == 0 and self.isFloat == 1):
             pass
        elif (event.widget["text"] == 0 and self.num[self.whichNum] == 0):
            return
        elif (self.num[self.whichNum] == 0):
            self.num[self.whichNum] = int(event.widget["text"])
            self.numDis["text"] = self.num[self.whichNum]
            return


        if (self.len == 10):
            return

        if (self.isFloat != 1):
            self.num[self.whichNum] = self.num[self.whichNum] * 10 + int(event.widget["text"])
        else:
            self.fractNum += 1
            self.num[self.whichNum] = round(self.num[self.whichNum]+int(event.widget["text"])* self.fract, self.fractNum)
            self.fract *= 0.1


        if (self.num[self.whichNum] == 0 and self.isFloat == 1 and self.fractNum > 1):
            num = str(self.num[self.whichNum])
            for i in range(1, self.fractNum):
                num += '0'
            self.numDis["text"] = num
            print(num)
        else :
            self.numDis["text"] = self.num[self.whichNum]

        self.len += 1

    def operationClk(self, event):
        operand = event.widget["text"]

        if (operand != "="and self.operand == 0):
            self.operand = operand
            self.numDis["text"] = 0
            self.isFloat = 0
            self.whichNum = 1
            self.len = 0
            self.fract = 0.1
            return
        elif (operand != "=" and self.operand != 0):
            return
        elif (operand == "=" and self.operand == 0):
            return

        if (self.operand == "+"):
            self.num[2] = self.num[0] + self.num[1]
        elif (self.operand == "-"):
            self.num[2] = self.num[0] - self.num[1]
        elif (self.operand == "*"):
            self.num[2] = self.num[0] * self.num[1]
        elif (self.operand == "/"):
            self.num[2] = self.num[0] / self.num[1]

        self.fractNum = 0
        self.fract = 0.1
        self.isFloat = 0
        self.len = len(str(self.num[2]))

        if (self.len >= 10 and isinstance(self.num[2], float)):

            if (len(str(int(self.num[2]))) >= 10 ):
                self.num[0] = self.num[2] = 9999999999
            else:
                lenInt = len(str(int(self.num[2])))
                self.num[0] = self.num[2] = round(self.num[2], 10 - lenInt)
            self.len = 10
            self.isFloat = 1

        elif (isinstance(self.num[2], float)):
            self.num[0] = self.num[2]
            self.fractNum = self.len - len(str(int(self.num[2]))) - 1
            self.fract = 0.1**(self.fractNum + 1)
            self.isFloat = 1

        elif (self.len >= 10 ):
            self.len = 10
            self.num[0] = self.num[2] = 9999999999
        else:
            self.num[0] = self.num[2]

        self.num[1] = 0
        self.numDis["text"] = self.num[2]
        self.whichNum = 0
        self.operand = 0

    def toFloat(self,event):
        if (self.isFloat == 0):
            #self.numDis["text"] += "."
            self.isFloat = 1
            self.fractNum = 0

    def Clear(self, event):
         self.num[0] = 0
         self.num[1] = 0
         self.num[2] = 0
         self.len = 1
         self.operand = 0
         self.isFloat = 0
         self.fract = 0.1
         self.fractNum = 0
         self.numDis["text"] = "0"

    def delLast(self,event):

        if (self.isFloat == 0):
            self.num[self.whichNum] = int(self.num[self.whichNum]/10)
        else:
            self.fractNum -= 1
            self.num[self.whichNum] = (int(10**self.fractNum*self.num[self.whichNum]))/(10**self.fractNum)
            self.fract = self.fract*10

            if ( self.fractNum == 0):
                self.isFloat = 0
                self.num[self.whichNum] = int(self.num[self.whichNum])

        if (self.len != 1):
            self.len -= 1

        self.numDis["text"] = self.num[self.whichNum]

