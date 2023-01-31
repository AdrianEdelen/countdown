import time as t
from tkinter import *
from datetime import datetime as dt

def CheckDateTimeIsBetween(begin_time, end_time, check_time = None):
        check_time = check_time or dt.utcnow().hour
        if begin_time < end_time:
            return check_time >= begin_time and check_time < end_time
        else: # crosses midnight
            return check_time >= begin_time or check_time < end_time
        
def CalcRemainingWorkHours(days_remaining):
    return days_remaining * 9

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        
        self.secondsL = Label(self, text="")
        self.minutesL = Label(self, text="")
        self.HoursL = Label(self, text="")
        self.DaysL = Label(self, text="")
        self.WorkDaysL = Label(self, text="")
        
        self.secondsL.pack(pady=5)
        self.minutesL.pack(pady=5)
        self.HoursL.pack(pady=5)
        self.DaysL.pack(pady=5)
        self.WorkDaysL.pack(pady=5)
        self.CalcTime()

    


    def CalcTime(self):
        
        timeLeft = 1676498400 - t.time()
        
        time = {
            'Seconds' : '{:.2f}'.format(round(timeLeft,2)),
            'Minutes' : '{:.3f}'.format(round(timeLeft / 60, 3)),
            'Hours'   : '{:.4f}'.format(round(timeLeft / 60 / 60, 4)),
            'Days'    : '{:.5f}'.format(round(timeLeft / 60/ 60 / 24,5))
        }
        self.secondsL.configure(text=f"Seconds: {time['Seconds']}")
        self.minutesL.configure(text=f"Minutes: {time['Minutes']}")
        self.HoursL.configure(text=f"Hours: {time['Hours']}")
        self.DaysL.configure(text=f"Days: {time['Days']}")
        if (CheckDateTimeIsBetween(13,24)):
            self.WorkDaysL.configure(text=f"Work Time Remaining: {'{:.5f}'.format(round(CalcRemainingWorkHours(float(time['Days'])),5))}")
             
        #if CheckDateTimeIsBetween(8, 17):
            
        self.after(16, self.CalcTime)


    

root = Tk()
app = Window(root)

root.wm_title("Countdown")
root.geometry("400x200")

root.mainloop()