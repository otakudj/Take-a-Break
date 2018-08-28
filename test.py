#!/usr/bin/python
# -*- coding: UTF-8 -*-

# GUI Import
import os
import numpy as np
import _tkinter
from tkinter import *
import random
import time

# Service Import
import pywin32_system32
import win32serviceutil
import win32service
import win32event
import sys

# GUI
class Wellnomics_Exercise():
    def demo(self):
        def change_to_2():
            label.configure(image = exer2)
            button.configure(text = 'Next', command = change_to_3)

        def change_to_3():
            label.configure(image = exer3)    
            button.configure(text = 'Finished', command = close)

        def close():
            top.destroy()
        
        pics = [pic for pic in os.listdir('./pic_ch/')]
        while 1:
            seq = np.random.permutation(len(pics))
            for i in range(0, len(seq), 3):
                top = Tk()
                top.title('wellnomics_exercises')
                exer1 = PhotoImage(file = './pic_ch/' + pics[i])
                exer2 = PhotoImage(file = './pic_ch/' + pics[i + 1])
                exer3 = PhotoImage(file = './pic_ch/' + pics[i + 2])
                label = Label(top, image = exer1)
                label.pack()
                button = Button(top, text = "Next", command = change_to_2)
                button.pack()
                top.mainloop()
                time.sleep(random.randint(40, 50) * 60)
                #time.sleep(5)

# Service                
# class Wellnomics_Exercises_Service(win32serviceutil.ServiceFramework):
    # _svc_name_ = "Wellnomics_Exercises_Service"
    # _svc_display_name_ = "The Everyday Wellnomics Exercises for Your Health"
    # def __init__(self, args):
        # win32serviceutil.ServiceFramework.__init__(self, args)   
        # self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
 
    # def SvcStop(self):
        # self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)   
        # win32event.SetEvent(self.hWaitStop)     
 
    # def SvcDoRun(self):
        # Wellnomics_Exercise.demo()
 
if __name__=='__main__':
    #win32serviceutil.HandleCommandLine(Wellnomics_Exercises_Service) 
    Wellnomics_Exercise().demo()