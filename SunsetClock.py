#! /usr/bin/env python

# Sunset Clock for condo

# Copyleft 2014 (8/25/14 2200) Mark Fink  -- mastermwf@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Reminder: The program is free. The images you use may be copyrighted.

# Ver. 0.1.0


import ephem
import datetime
import Tkinter as tk # Tkinter for Python 2.7
# import tkinter as tk  # tkinter for Python 3.4
from Tkinter import *
# from tkinter import *

hel65B = ('Helvetica', 65, 'bold')   # substitute your favorite font here for insertion in line 64
hel80 = ('Helvetica', 80)            # defines font
san65 = ('Sans', 65)

now = datetime.datetime.now() #get current time

GOM=ephem.Observer()
GOM.horizon = 0
GOM.lat='29.1266667'   # Insert your Latitude here. Positive numbers for North
GOM.lon='-90.2166667'  # Insert your Longitude here. Negative numbers for West
GOM.elevation = 24     # meters
GOM.date = now
sun = ephem.Sun()      

def countdown(label):
  def clock():
        
    nextSet = ephem.localtime(GOM.next_setting(sun))   # This is the line that can be modified to get sunrise, moonset, meridian passage, etc
    remaining = nextSet-datetime.datetime.now()
    hours = int(remaining.seconds) // 3600
    minutes = int(remaining.seconds % 3600) // 60
    seconds = int(remaining.seconds % 60)
    displayFormat = 'Sunset in {}:{}:{}'.format(hours, format(minutes, '02d'), format(seconds, '02d'))
    label.config(text= '\n \n \n \n \n {}'.format(displayFormat))    # adjust newlines '\n' to fit your display
    label.after(1000, clock)
    
  clock()
 
 
root = tk.Tk()                # creates the working window
root.title("Sunset Clock")    # text in title bar
logo = PhotoImage(file="clock1.ppm")  # Insert path to your favorite sunset photo. Resolution of photo determines window size.
label = tk.Label(root, compound=CENTER, font=hel65B, image=logo, fg="white")   # centers text, adjusts font, inserts background photo, choice of text color
countdown(label)      # runs the counting routine
label.pack()          # displays the label with text on top of the image

root.mainloop()
