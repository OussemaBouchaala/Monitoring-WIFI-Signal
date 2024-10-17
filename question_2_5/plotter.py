import sys
import os
import tkinter as tk
# Add the parent directory of question_2_4 and question_2_5 to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from question_2_4.detect_networks import detect_networks

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Function to update the bar chart
def update_chart():
    global bar_rects, ax, canvas

    # Get the latest Wi-Fi signal data
    wifi_data = detect_networks()
    cleaned_data = [(ssid, int(signal.strip('%'))) for ssid, signal in wifi_data]
    ssids = [x[0] for x in cleaned_data]
    signal_strengths = [x[1] for x in cleaned_data]

    # Clear the existing plot
    #ax.clear()

    # Create a new bar chart
    bar_rects = ax.bar(ssids, signal_strengths, color='blue')

    # Set axis labels and range
    ax.set_ylim(0, 100)  # Signal strength typically between -100 and 0 dBm
    ax.set_ylabel("Signal Strength (%)")
    ax.set_title("Real-Time Wi-Fi Signal Strength")

    # Draw the updated chart
    canvas.draw()

    # Call the function again after 5 seconds (5000 milliseconds)
    root.after(500, update_chart)

# Tkinter window setup
root = tk.Tk()
root.title("Wi-Fi Signal Strength Monitor")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(6, 4))

# Embed the Matplotlib figure in Tkinter using FigureCanvasTkAgg
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Start the real-time chart update
root.after(200, update_chart)

# Run the Tkinter main loop
root.mainloop()