import time as t
from tkinter import *
from datetime import datetime as dt

def Clock(deltaTime=t.time()):
    return deltaTime - t.time()

class LabelFriendlyName(Label):
    def __init__(self, root, text="", friendlyName=None, lambdaF=None):
        super().__init__(root, text=text)
        self.FriendlyName = friendlyName
        self.Lambda = lambdaF

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.labels = {}
        self.CreateLabels()
        self.CalcTime()

    def AddNewLabel(self,labelName, labelText = "", friendlyName = None, packDir=None, lambdaF=None):
        if friendlyName is not None: # how can this be improved?
            self.labels.update({labelName:LabelFriendlyName(self.master, labelText, friendlyName, lambdaF=lambdaF)})
        else:
            self.labels.update({labelName:LabelFriendlyName(self.master, labelText, labelName, lambdaF=lambdaF)})
        if packDir != None:
            if packDir == "pack":
                self.labels[labelName].pack(fill=BOTH, expand=TRUE)

    def ConfigureLabel(self, key=None, value=None, label=None, format=None):
        if key is not None:
            self.labels[key].configure(text=f"{self.labels[key].FriendlyName}: {f'{format}'.format(self.labels[key].Lambda(value))}")
        else: #not tested
            label.configure().configure(text=f"{label.FriendlyName}: {f'{format}'.format(label.Lambda(value))}")

    def CreateLabels(self):#improve these lambda function calcs
        self.AddNewLabel(labelName="Milliseconds", packDir="pack", lambdaF=lambda x: x*1000)
        self.AddNewLabel(labelName="Seconds", packDir="pack", lambdaF=lambda x: x)
        self.AddNewLabel(labelName="Minutes", packDir="pack", lambdaF=lambda x: x/60)
        self.AddNewLabel(labelName="Hours", packDir="pack", lambdaF= lambda x: x/60/60)
        self.AddNewLabel(labelName="Days", packDir="pack", lambdaF=lambda x: x/60/60/24)
        self.AddNewLabel(labelName="tenthsRemaining", friendlyName="Tenths of a Seconds Remaining", packDir="pack",lambdaF=lambda x: 60 * x % 1)
        self.AddNewLabel(labelName="SecondsRemaining", friendlyName="Seconds Remaining", packDir="pack",lambdaF=lambda x: (((((x/86400 % 1) * 24) % 1) * 60) % 1) * 60)
        self.AddNewLabel(labelName="MinutesRemaining", friendlyName="Minutes Remaining", packDir="pack",lambdaF=lambda x: (((x/86400 % 1) * 24) % 1) * 60 )
        self.AddNewLabel(labelName="HoursRemaining", friendlyName="Hours Remaining", packDir="pack",lambdaF=lambda x: (x/86400 % 1) *24 )
        self.AddNewLabel(labelName="DayRemaining", friendlyName="Day Remaining", packDir="pack",lambdaF=lambda x: x/86400 % 1  )
 
    def CalcTime(self):
        for label in self.labels:
            self.ConfigureLabel(key=label, value=Clock(1676498400), format='{0:.3f}')
        self.after(16, self.CalcTime)

root = Tk()
app = Window(root)

root.wm_title("Countdown")
root.mainloop()