import tkinter as tk
from tkinter import ttk

def start_bot():#Here is coming trading bot logic.
    print("Bot started with the following parameters:")
    print(f"Crypto Pair: {pair_entry.get()}")
    print(f"Buy Treshold: {buy_threshold_entry.get()}")
    print(f"Sell Treshold: {sell_threshold_entry.get()}")

#Main Window.
root = tk.Tk()
root.title("Crypto Trading Bot")

#Adding Grid.
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Adding Widgets.
pair_label = ttk.Label(mainframe, text="Crypto Pair (adding pairs later):")
pair_label.grid(column=0, row=0, sticky=tk.W)
pair_entry = ttk.Entry(mainframe)
pair_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

buy_threshold_label = ttk.Label(mainframe, text="Buy Treshold:")
buy_threshold_label.grid(column=0, row=2, sticky=tk.W)
buy_threshold_entry = ttk.Entry(mainframe)
buy_threshold_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

sell_threshold_label = ttk.Label(mainframe, text="Sell Threshold:")
sell_threshold_label.grid(column=0, row=2, sticky=tk.W)
sell_threshold_entry = ttk.Entry(mainframe)
sell_threshold_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

start_button = ttk.Button(mainframe, text="Start Bot", command=start_bot)
start_button.grid(column=1, row=3, sticky=tk.W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

pair_entry.focus()

root.mainloop()