import tkinter as tk
from tkinter import ttk

crypto_pairs = [
    'BTC-USD', 'ETH-USD', 'XRP-USD', 'BCH-USD', 'LTC-USD',
    'EOS-USD', 'BNB-USD', 'BSV-USD', 'USDT-USD', 'ADA-USD',
    'XLM-USD', 'TRX-USD', 'MIOTA-USD', 'DASH-USD', 'XMR-USD',
    'XTZ-USD', 'ETC-USD', 'NEO-USD', 'MKR-USD', 'ONT-USD'
]

def start_bot():#Here is coming trading bot logic.
    print("Bot started with the following parameters:")
    print(f"Crypto Pair: {pair_entry.get()}")
    print(f"Buy Treshold: {buy_threshold_entry.get()}")
    print(f"Sell Treshold: {sell_threshold_entry.get()}")

#Main Window.
root = tk.Tk()
root.title("Crypto Trading Bot")

#Window size is set up to 70% of screen size. Change as needed.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)
position_right = int(screen_width / 2 - window_width / 2)
position_down = int(screen_height / 2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

#Chart Area 40% of applications size, change as needed.
chart_width = window_width
chart_height = int(window_height * 0.4)
chart_area = tk.Canvas(root, width=chart_width, height=chart_height, bg="lightgray")
chart_area.pack(side=tk.TOP, pady=(10, 0))

#Adding Grid.
mainframe = ttk.Frame(root)
mainframe.pack(fill=tk.BOTH, expand=True)

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