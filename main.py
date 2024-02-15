import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplfinance as mpf
import yfinance as yf
import pandas as pd

crypto_pairs = [
    'BTC-USD', 'ETH-USD', 'XRP-USD', 'BCH-USD', 'LTC-USD',
    'EOS-USD', 'BNB-USD', 'BSV-USD', 'USDT-USD', 'ADA-USD',
    'XLM-USD', 'TRX-USD', 'MIOTA-USD', 'DASH-USD', 'XMR-USD',
    'XTZ-USD', 'ETC-USD', 'NEO-USD', 'MKR-USD', 'ONT-USD'
]

def fetch_candlestick_data(pair):
    #Convert format for yahoo finance from "XXX-YYY" to "XXXYYY=X".
    yf_pair = pair.replace('-', '') + "=X"

    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(months=6)

    #Fetching historical market data.
    df = yf.download(yf_pair, start=start_date, end=end_date)

    if not df.empty:
        df.rename(columns={"Open": "Open", "High": "High", "Low": "Low", 
                           "Close": "Adj Close", "Volume": "Volume"}, inplace=True)
        return df
    else:
        print(f"No data found {pair}")

def start_bot():#Here is coming trading bot logic.
    selected_pair_index = pair_listbox.curselection()
    selected_pair = crypto_pairs[selected_pair_index[0]] if selected_pair_index else ""
    print("Bot started with the following parameters:")
    print(f"Crypto Pair: {selected_pair}")
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

#Container for chart and listbox.
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X)

#Chart Area 40% of applications size, change as needed.
chart_width = int(window_width * 0.6)
chart_height = int(window_height * 0.4)
chart_area = tk.Canvas(top_frame, width=chart_width, height=chart_height, bg="lightgray")
chart_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#Listbox for selecting crypto pair.
pair_listbox = tk.Listbox(top_frame, exportselection=False)
for pair in crypto_pairs:
    pair_listbox.insert(tk.END, pair)
pair_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

#Adding Grid.
mainframe = ttk.Frame(root)
mainframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#Adding Widgets.
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

root.mainloop()