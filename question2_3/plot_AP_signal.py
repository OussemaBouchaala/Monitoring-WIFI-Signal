import subprocess
import re
import time
from datetime import datetime
import keyboard
import platform
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
import numpy as np
def read_data_from_cmd():
    p = subprocess. Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode('unicode_escape').strip()
    #print(out)
    if platform.system() == 'Linux':
        m = re.findall('(wlan [0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
    elif platform.system() == 'Windows':
        m = re.findall('Name.*?:.*? ([A-z0-9-]*).*?Signal.*?:.*?([0-9]*%)', out, re. DOTALL)
    else:
        raise Exception('reached else of if statement')
    p.communicate()
    print(m)
    return m

def display_signal_strength_continuously():
    """
    This function continuously fetches and displays the Wi-Fi signal strength.
    """
    try:
        while True:
            read_data_from_cmd()
            time.sleep(0.2)  # Refresh every 5 seconds
            if keyboard.is_pressed('q'):  # This waits for any key press
                print("Key pressed. Stopping signal strength monitoring.")
                break
    except KeyboardInterrupt:
        print("\nStopping the continuous signal strength monitoring.")

# Run the function to continuously display signal strength
#display_signal_strength_continuously()

#plot signals
def get_signal(arr):
    signal=arr[0][1]
    signal=signal[:-1]
    signal=int(signal)
    return signal

yLimit=int(input("donner la limite des points à afficher: "))
x_data, y_data = [], []
figure =plt.figure()
line,= plt.plot(x_data, y_data, color='red', linestyle='-', marker='o', markersize=5, label='Signal Strength')

def update (frame):
    
    x_data.append(datetime.now()) 
    y_data.append(get_signal(read_data_from_cmd()))
    #y_data.append(randrange(1,5))

    if len(y_data)>yLimit :
        y_data.pop(0)
        x_data.pop(0)

    line.set_data(x_data, y_data)
    figure.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    figure.gca().relim()
    figure.gca().autoscale_view()

    # Set date formatting for x-axis
    
    
    plt.gcf().autofmt_xdate()

    # Set the limits for y-axis
    plt.ylim(0, 100)

    return line,
try:
    animation =FuncAnimation (figure, update, interval=200, cache_frame_data=False)
    plt.xlabel('Real Time')
    plt.ylabel('Signal Strength (%)')
    plt.title('Real Time Signal Strength')
    plt.legend()
    plt.show()
except KeyboardInterrupt:
    print("\nStopping the continuous signal strength monitoring.")



