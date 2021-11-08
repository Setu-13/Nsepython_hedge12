# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import logging
import threading
import time as sleeptime

import pytz
from datetime import time
from nsepython import *


class Hedeg_12:
    # Verify if market is open or not
    def __init__(self):
        self.exp_list=(expiry_list("BANKNIFTY", "list"))
        print("Upcomming Exp are \n",self.exp_list)
        print("Latest one is--",self.exp_list[0])

        #self.exp_list=exp_list[0]


    def market_status():
        india_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        #india_time = datetime.now().time()

        if india_time <= time(15, 30):
            if india_time >= time(9,15):
                #market_status = running_status()
                print("Market is open")
                return "OPEN"
            else:
                print("Market close")
                return "CLOSE"
        else:
            print("Market close")
            return "CLOSE"

    # BANK-Nifty current price and round price
    def spot_price(self, symbol):

        spot_price = index_info(symbol)["last"]
        #print(symbol, spot_price)
        now = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%a--%I:%M:%p||%d-%b-%Y")
        #print(now_time)
        #now_time.strftime("%a--%I:%M:%p||%d-%b-%Y")
        return spot_price, now

    def derivative_symbol(self, symbol, exp, type, strike_point):
         try:
            #print(symbol,exp,type, strike_point)
            #derivative_price = nse_quote_ltp(str(symbol),str(exp),str(type), 40000)
            #print('"'+symbol+'"','"'+exp+'"', '"'+type+'"', 40000)
            derivative_price = nse_quote_ltp(symbol,exp, type, strike_point)
            #print(derivative_price)
            return derivative_price

         except:
            print("error")
            exit(0)

    def hedge_12_calculation(self, spot_price):
        spot_price=round(spot_price,-2)
        #print(spot_price)


        # PE = threading.Thread(traget=nse_quote_ltp("BANKNIFTY", self.exp_list[0], "PE", spot_price + 100,))
        # CE = threading.Thread(target=nse_quote_ltp("BANKNIFTY", self.exp_list[0], "CE", spot_price - 100,))
        # PE = threading.Thread(traget=self.derivative_symbol("BANKNIFTY", self.exp_list[0], "PE", spot_price + 100,))
        # CE = threading.Thread(target=self.derivative_symbol("BANKNIFTY", self.exp_list[0], "PE", spot_price - 100,))
        # PE.start()
        # CE.start()
        # print(CE.join())
        # print(PE.join())



        PE=self.derivative_symbol("BANKNIFTY",self.exp_list[0],"PE",spot_price+100)
        CE=self.derivative_symbol("BANKNIFTY",self.exp_list[0],"PE",spot_price-100)
        #print(PE,"--",CE)
        return PE, CE




def welcome(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(name)  # Press Ctrl+F8 to toggle the breakpoint.

    #from datetime import datetime

    # datetime object containing current date and time
    trade = Hedeg_12()

    banknifty = trade.spot_price("NIFTY BANK")
    #print("Bank Nifty running @",banknifty[0],"on", banknifty[-1])
    #now = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%a--%I:%M:%p||%d-%b-%Y")
    while datetime.datetime.now(pytz.timezone('Asia/Kolkata')).time() <= datetime.time(15, 30):
        price=trade.hedge_12_calculation(banknifty[0])
        #print(price)
        print("\nBank Nifty running @",banknifty[0],"DATE", banknifty[-1],"\nPE->",price[0] , " and CE->",price[1],"\t Sum is ",round(sum(price),1),"\n...")
        sleeptime.sleep(5)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    welcome('This is program to monitor HEDGE-12 from NES')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
