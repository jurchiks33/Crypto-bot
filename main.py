import tkinter as tk
from tkinter import ttk

def start_bot():
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

