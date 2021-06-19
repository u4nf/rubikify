import tkinter as tk
import tkinter.messagebox as box


window = tk.Tk()
window.title('Scalp Calc')
window.geometry('250x300')


def calculate():
	output_label = tk.Label(window, text='Profit %').place(x=15, y=80)

	buy_price = float(buy_price_input.get())
	target_price = float(target_price_input.get())
	fee = 0.002

	try:
		profit_percent_bf = ((target_price - buy_price) / buy_price) * 100
		profit_percent_af = round(profit_percent_bf - fee, 4)
	except ZeroDivisionError:
		output_data_label = tk.Label(window, text='Zero').place(x=100, y=80)
		return 0


	output_data_label = tk.Label(window, text=str(profit_percent_af)).place(x=100, y=80)

def profit_above():
	output_label = tk.Label(window, text='Profit above').place(x=15, y=100)

	buy_price = float(buy_price_input.get())
	fee = 0.002

	profit_above = round(buy_price + (buy_price * fee), 7)
	#profit_above = buy_price + (buy_price * fee)

	output_data_label = tk.Label(window, text=str(profit_above)).place(x=100, y=100)



buy_price_label = tk.Label(window, text='Buy Price').place(x=15, y=20)

buy_price_input = tk.Entry(window, width=15)
buy_price_input.insert(tk.END, '0')
buy_price_input.place(x=100, y=20)
buy_price_input.focus()

target_price_label = tk.Label(window, text='Target Price').place(x=15, y=50)

target_price_input = tk.Entry(window, width=15)
target_price_input.insert(tk.END, '0')
target_price_input.place(x=100, y=50)
target_price_input.focus()

go_button = tk.Button(window, text='CALC PERCENT PROFIT', command=calculate, borderwidth=5)
go_button.place(x=35, y=170)

profit_above_button = tk.Button(window, text='PROFIT ABOVE', command=profit_above, borderwidth=5)
profit_above_button.place(x=60, y=220)

output_label = tk.Label(window).place(x=15, y=80)
output_data_label = tk.Label(window).place(x=100, y=80)

window.mainloop()