import requests
import tkinter as tk



currency_symbolx=['USD', 'AED', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AZN', 'BBD', 'BDT', 'BGN', 'BHD', 'BRL', 'BSD', 'BWP', 'BYN', 'CAD', 'CHF', 'CLP', 'CNY', 'COP', 'CZK', 'DKK', 'DOP', 'DZD', 'EGP', 'ETB', 'EUR', 'FJD', 'GBP', 'GEL', 'GHS', 'GNF', 'GTQ', 'HKD', 'HNL', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KHR', 'KRW', 'KWD', 'KZT', 'LAK', 'LBP', 'LKR', 'MAD', 'MDL', 'MKD', 'MMK', 'MUR', 'MXN', 'MYR', 'NAD', 'NGN', 'NOK', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'SAR', 'SCR', 'SEK', 'SGD', 'THB', 'TJS', 'TND', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UYU', 'UZS', 'VEF', 'VND', 'XAF', 'XCD', 'XOF', 'XPF', 'ZAR', 'ZMW']


print("LIST OF CURRENCY FORMAT ")
for i in range(len(currency_symbolx)):
    print(i,currency_symbolx[i])


def calx():
    print(amounto.get(),base.get(),export.get())
    url = 'http://v3.exchangerate-api.com/bulk/3749462b0ddb36c1c43a777f/'
    print("ENTER THE AMOUNT : ")
    amount=int(amounto.get())
    print("ENTER THE BASE CURRENCY CODE: ")
    ax=str(base.get())
    url=url+ax
    response = requests.get(url)
    datax=response.json()
    print("CHOOSE THE EXCHANGE RATE CURRENCY : ")
    bx=str(export.get())
    currency_output=amount*(datax['rates'][bx])
    print("THE RATE VALUE: ")
    print(currency_output)
    currency_output=round(currency_output,2)
    tk.Label(window, text=currency_output, font="lato").grid(row=4, column=2)

window=tk.Tk()
window.geometry("400x150+95+5")
window.title("CURRENCY CONVERTOR")
tk.Label(window,text=" AMOUNT ",font="lato").grid(row=0,column=0)
amounto=tk.Entry(window)
amounto.grid(row=0,column=2)
tk.Label(window,text=" BASE CURRENCY ",font="lato").grid(row=1,column=0)
base=tk.Entry(window)
base.grid(row=1,column=2)
tk.Label(window,text=" EXPORT CURRENCY ",font="lato").grid(row=2,column=0)
export=tk.Entry(window)
export.grid(row=2,column=2)
tk.Button(window,text='  CONVERT  ',command=calx,fg = "darkgreen", bg = "white").grid(row=3,column=1)
tk.Label(window,text=" AMOUNT ",font="lato").grid(row=4,column=0)
window.mainloop()