# -*- coding: utf-8 -*-
"""
@author: Shubham and Siddharth
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame
import time
pygame.init()    #initalise all imported module
root=Tk()
from statemachine import StateMachine, State                                                                                                                                                                                                                                                        

class Refrigerator(StateMachine):
    
    ir=State('no light',initial=True)
    reset=State('Red')
    detect=State("Red")
    temp=State("high or low")
    more=State("high")
    less=State("low")
    buzzer=State("beep")
    door_open=State("open")
    door_lock=State("lock")

    detect1=ir.to(detect)
    reset1=ir.to(reset)
    reset2=reset.to(ir)

    temp1=detect.to(temp)
    more1=temp.to(more)
    buzzer1=more.to(buzzer)
    door_lock1=buzzer.to(door_lock)
    reset3=door_lock.to(ir)

    less1=temp.to(less)
    door_open1=less.to(door_open)
    reset4=door_open.to(ir)



re=Refrigerator()
    
def button_action():            # make user defined code
    if re.is_ir:
        re.detect1()
        messagebox.showinfo("Motion Detected","Now checking temperature...")  # To display the message when we click the button
        root.configure(background='snow2')     #After pressing button, window background colour change
        root.geometry('250x200')        #Set dimension of window
        lbl_title.pack()

def button1_action():    
    if re.is_detect:
        re.temp1()
        messagebox.showinfo("Temperature","Temperature Checking")   # To display the message when we click the button 
        root.configure(background='snow2')     #After pressing button, window background colour change
        root.geometry('250x200')        #Set dimension of window
        # lbl_title = tk.Label(root,text="Red Led Glows", bg ='black',fg='snow2')
        lbl_title.pack()

def button2_action():
    if re.is_temp:
        re.less1()
        messagebox.showinfo("Temperature is normal","Door remains open")
        root.configure(background='snow2')
        root.geometry('250x200')
        re.door_open1()
        re.reset4()
        messagebox.showinfo("Resetting the state","Pointer comes to initial state")
        lbl_title.pack()

def button3_action():    
    if re.is_temp:
        re.more1()
        messagebox.showinfo("Temperature is high", "Alarm start")   # To display the message when we click the button      
        root.configure(background='snow2')
        root.geometry('250x200')
        re.buzzer1()
        messagebox.showinfo("Buzzer","Alarm ON")
        pygame.mixer.music.load(r"C:\Users\Shubham\Desktop\click_one.mp3") # Destination of alarm file and need to change it according to your system
        pygame.mixer.music.play()   # To Play the alarm
        re.door_lock1()
        messagebox.showinfo("Door locked","Door is locked")   # To display the message when we click the button      
        root.configure(background='snow2')
        root.geometry('250x200')
        lbl_title.pack()
        
        time.sleep(5) #Delay the time
        re.reset3()
        messagebox.showinfo("Reseting the state","State resetted")   # To display the message when we click the button
        root.configure(background='snow2')      
        pygame.mixer.music.stop()    # When button1 clicks then it stops the alarm

def button5_action():
    if re.is_ir:
        re.reset1()
        re.reset2()
        messagebox.showinfo("Motion not detected","Motion not Detected \n reseting the states")  # To display the message when we click the button
        root.configure(background='SkyBlue2')     #After pressing button, window background colour change
        root.geometry('250x200')        #Set dimension of window
        lbl_title.pack()



root.configure(background='white')       # Background colour of window
root.geometry('250x200')

lbl_title = tk.Label(root,text="Implement burglar alarm", bg = 'blue',fg='snow2')
lbl_title.pack()

root.maxsize(250,200)           # Set Maximum size of a window
root.minsize(250,200)           # Set Minimum size of a window

# Add button to gui window to change background colour and text colour and adds a command to button
button=Button(root, text ='Motion Detected',command = button_action, fg="snow2",bg="medium blue")
button1=Button(root, text ='Temperature Checking',command = button1_action, fg="snow2",bg="medium blue")
button2=Button(root, text='Temperature is normal',command = button2_action, fg="snow2",bg="medium blue")
button3=Button(root, text='Temperature is high',command = button3_action, fg="snow2",bg="medium blue")
button5=Button(root, text='Motion not detected',command = button5_action, fg="snow2",bg="medium blue")

button.place(x=75,y=40)             # To set the coordinates of button
button1.place(x=59,y=70)           # To set the coordinates of button
button2.place(x=59,y=100)           # To set the coordinates of button
button3.place(x=65,y=130) 
button5.place(x=63,y=160) 

mainloop()
    
    