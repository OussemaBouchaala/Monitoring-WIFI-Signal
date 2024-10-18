import sys
import os
import tkinter as tk
from tkinter import ttk
# Add the parent directory of question_2_4 and question_2_5 to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from question_2_4.cmd import detect_networks,connect_wifi

networks = detect_networks()

root = tk.Tk()
root.title("Access Points Infos")
#root.geometry("400x300")  # Width x Height
root.wm_minsize(400, 300)  # Minimum width of 400 pixels and minimum height of 300 pixels


label = tk.Label(root, text="Click button to show nearby acces points")
label.pack()  # Automatically place the widget



def toggle_treeview():
    global networks 
    array=detect_networks()
    networks = sorted(array, key=lambda x: int(x[1].strip('%')), reverse=True)
    global tree_exists, tree
    if tree_exists:
        tree.destroy()
    # Create a new Treeview widget
    tree = ttk.Treeview(root, columns=('SSID', 'Signal'), show='headings')

    # Define the columns and disable resizing (stretch=False)
    tree.heading('SSID', text='Access Point (SSID)', anchor='center')  # Center align the heading
    tree.heading('Signal', text='Signal Strength', anchor='center')  # Center align the heading

    # Fix column widths and prevent resizing by the user
    tree.column('SSID', width=260, minwidth=200, stretch=True)
    tree.column('Signal', width=120, minwidth=120, stretch=True)

    # Insert the updated data
    for ssid, signal in networks:
        # Insert the values
        tree.insert('', tk.END, values=(ssid, signal))

    # Pack the Treeview widget into the window
    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Set tree_exists to True to indicate that the grid is visible
    tree_exists = True
    root.after(200, toggle_treeview)
  
def show_SSID_infos():
    button.config(state=tk.DISABLED)
    button1.config(state=tk.NORMAL)
    toggle_treeview()

    

# def show_SSID_infos():
#     text.config(state=tk.NORMAL)
#     array=detect_networks()
#     sorted_networks = sorted(array, key=lambda x: int(x[1].strip('%')), reverse=True)
#     multilines_array = "\n".join([str(item) for item in sorted_networks])
#     text.insert(tk.END, f"Nearby Access Points sorted by signal rate:\n{multilines_array}\n")
#     text.insert(tk.END,"\n------------------------------\n")
#     text.config(state=tk.DISABLED)

def connect_ssid():
    global msg_exists
    if msg_exists:
        global label1
        label1.destroy()
    #print(type(sorted_networks[0][0]),type(connect_wifi(sorted_networks[0][0])))
    cnct_msg=connect_wifi(networks[0][0])
    msg= "AP Name: "+networks[0][0]+" -> "+cnct_msg
    label1 = tk.Label(root, text=msg)
    label1.pack()
    msg_exists=True

msg_exists = False

tree_exists = False
# button_frame = tk.Frame(root)
# button_frame.pack(pady=1000)
button = tk.Button(root, text="Show", command=show_SSID_infos)
button.pack()
button1 = tk.Button(root, text="Connect to the perfect one", command=connect_ssid)
button1.pack()
button1.config(state=tk.DISABLED)
# text = tk.Text(root, height=100, width=400)
# text.config(state=tk.DISABLED)
# text.pack(pady=10)
#tree = None
root.mainloop()