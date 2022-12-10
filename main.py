# from replit import db
from formating import *
import os
import time
stock = []

def logo():
  # Put your bank name here: VVV
  print("<insert bank name here>")
  print()
  print("--------------")
  print()


def store():
  while True:
    choice = input("Sell, buy, stock, show (lists), or exit: ").lower()
    print()
    if choice == "sell":
      pass
    elif choice == "buy":
      pass
    elif choice == "stock":
      stockquest = input("Do you want to stock items or remove items (S/R): ").lower()
    
      if stockquest == "s":
        sadd = input("What are you going to add?: ").capitalize().strip()
        saddprice = round(float(input("How much should it cost?: ")), 2)
        stockadd = f"{sadd}:{saddprice:>30:}".replace(" ", ".")
        stock.append(stockadd)
        print(stock)
        continue
      elif stockquest == "r":
        pass
      else:
        print(Red)
        print("Error: unknown command!")
        print(reset)
    elif choice == "show":
      print(stock)
    elif choice == "exit":
      exit(1)
    else:
      print(Red)
      print("Error: unknown command!")
      print(reset)
logo()
store()