# from replit import db
from formating import *
import os, time, random
stock = {}
def WIP():
  wipmess = random.randint(1,3)
  print(Red)
  if wipmess == 1:
    print("This is a work in progress feature!")
  elif wipmess == 2:
    print("This feature is not available yet!")
  elif wipmess == 3:
    print("This feature is coming soon!")
  else:
    pass
  print(reset)
  time.sleep(1.5)
  os.system('clear')
  logo()
  store()
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
      WIP()
    elif choice == "buy":
      WIP()
    elif choice == "stock":
      stockquest = input("Do you want to stock items or remove items (S/R): ").lower()
    
      if stockquest == "s":
        sadd = input("What are you going to add?: ").title().strip()
        saddprice = round(float(input("How much should it cost?: ")), 2)
        saddprice_text = f"{saddprice}"
        stockadd = f"{sadd}:{'.'*(40 - len(sadd) - len(saddprice_text))}${saddprice_text}"
        stock[sadd] = stockadd
        print(stockadd)
      elif stockquest == "r":
        srm = input("What do you want to remove?: ").title().strip()
        if srm in stock:
          del stock[srm]
        else:
          print(Red)
          print(f"Error: No such item, {srm} in stock.")
          print(reset)
        # I can't remove stuff from the stock list ⬆⬆⬆⬆⬆.
      else:
        print(Red)
        print("Error: unknown command!")
        print(reset)
    elif choice == "show":
      for item, label in stock.items():
        print(label)
    elif choice == "exit":
      exit(1)
    elif choice == "wip test":
      WIP()
    else:
      print(Red)
      print("Error: unknown command!")
      print(reset)
logo()
store()