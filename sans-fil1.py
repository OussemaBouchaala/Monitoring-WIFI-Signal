import subprocess
import re
import time
import platform
import matplotlib.pyplot as plt
import numpy as np
import keyboard
import matplotlib.dates as mdates


import matplotlib.pyplot as plt

from datetime import datetime,timedelta
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange

from datetime import datetime, timedelta


current_time = datetime.now()


time_minus_200ms = current_time - timedelta(milliseconds=200)
time_minus_400ms = current_time - timedelta(milliseconds=400)









def read_data_from_cmd():
    p = subprocess. Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode("unicode_escape").strip()
    #print(out)
    if(platform.system()=='Linux'):
        m= re.findall('(wlan[0-9]+).?Signal level=(-[0-9]+) dBm',out,re.DOTALL)
    elif platform.system() == 'Windows':
        m = re.findall('Signal.*?ÿ:.*?([0-9]*)%', out, re. DOTALL)
    else:
        raise Exception('reached else of if statement')
    p.communicate()
    #print(m)
    
    return m
# while(1):
#     m=read_data_from_cmd()
#     signal=m[0]
#     print(signal)
#     time.sleep(0.2)
#     if(keyboard.is_pressed('q')):
#         break

max_data=int(input("please enter the maximum number of points in the gragh= "))
def update(frame):
    
    
    m=read_data_from_cmd()
    signal=int(m[0])
    
    x_data.append(datetime.now())
    if(len(x_data)>max_data):
        x_data.pop(0)
    
    y_data.append(signal)
    if(len(y_data)>max_data):
        y_data.pop(0)
  
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,


x_data, y_data = [], []

figure = pyplot.figure()
pyplot.ylim(0, 100)
line, = pyplot.plot(x_data, y_data,linestyle='-',marker='o',label="hello")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H-%M-%S')) 
pyplot.title("hi")
plt.xlabel("time")
plt.ylabel("signal strenth")
plt.legend()
plt.gcf().autofmt_xdate()

animation = FuncAnimation(figure, update, interval=200,cache_frame_data=False)

pyplot.show()


