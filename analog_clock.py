
import tkinter as tk
import math
import time
import frames as f


# clock outline
f.analog_canvas.create_oval(250, 250, 750, 750, 
                            outline = "grey", 
                            width = 10, 
                            )

start = 240 # point near edge of clock
end = 220 # end point for line
# creates lines for minutes
for i in range(60):
  f.analog_canvas.create_line(500 + start * math.cos(2 * math.pi * i / 60), 
                              500 + start * math.sin(2 * math.pi * i / 60), 
                              500 + (end + 10) * math.cos(2 * math.pi * i / 60), 
                              500 + (end + 10) *math.sin(2 * math.pi * i / 60), 
                              fill = "white", 
                              width = 2, 
                              )
# creates lines for hours
for i in range(12):
  f.analog_canvas.create_line(500 + start * math.cos(2 * math.pi * i / 12), 
                              500 + start * math.sin(2 * math.pi * i / 12), 
                              500 + end * math.cos(2 * math.pi * i / 12), 
                              500 + end *math.sin(2 * math.pi * i / 12), 
                              fill = "red", 
                              width = 5, 
                              )


def get_time():
  '''
  Gets current time.
  '''
  hr = time.localtime()[3]
  mn = time.localtime()[4]
  sc = time.localtime()[5]
  
  return hr, mn, sc


def convert_time():
  '''
  Converts current time to display on clock
  '''
  hr, mn, sc = get_time()
  
  minute = mn + sc / 60
  hour = hr % 12 + minute / 60
  
  return hour, minute, sc


class AnalogClock():
  '''
  Updates and draws hands onto canvas.
  '''
  def __init__(self):
    self.line = f.analog_canvas.create_line(500, 500, 500, 500, 
                                            fill = "white", 
                                            width = 5, 
                                            )
    # sec_line uses diff colour and is specific to the seconds hand
    self.sec_line = f.analog_canvas.create_line(500, 500, 500, 500, 
                                                fill = "red", 
                                                width = 2, 
                                                )  
    
  def update_hands(self, angle, length):
    x = 500 + length * math.cos(angle)
    y = 500 + length * math.sin(angle)
    # used length of seconds hand to plot specific line for seconds
    # else it uses the defualt line (white colour)
    if (length == 230):
      f.analog_canvas.coords(self.sec_line, 500, 500, x, y)
    else:
      f.analog_canvas.coords(self.line, 500, 500, x, y)
    
  def draw_hands(self):
    hour, minute, second = convert_time()
    
    # hour hand 
    hour_hand.update_hands(2 * math.pi * hour / 12 - math.pi / 2, 
                           130,  
                           )
    # minute hand 
    minute_hand.update_hands(2 * math.pi * minute / 60 - math.pi / 2, 
                             180, 
                             )
    # second hand
    second_hand.update_hands(2 * math.pi * second / 60 - math.pi / 2, 
                             230, 
                             )
    # refreshes/draws hands again after 1000 ms
    f.analog_canvas.after(1000, self.draw_hands) 

# hands for clock
hour_hand = AnalogClock()
minute_hand = AnalogClock()
second_hand = AnalogClock()
