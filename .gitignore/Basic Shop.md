# Basic shop code:
````
from replit import db
import os
import time

def Shop():
  while True:
    Money = db["Bank"]
    cmd = input("Add, take, set, see, clear, or exit? ").lower()
    if cmd == "add":
      add = int(input("How much should I add? "))
      Money += add
      print("You have", Money)
      db["Bank"] = Money
    elif cmd == "take":
      take = int(input("How much should I take? "))
      Money -= take
      print("You have", Money)
      db["Bank"] = Money
    elif cmd == "set":
      set = int(input("What should I set it to? "))
      Money = set
      print("You have", Money)
      db["Bank"] = Money
    elif cmd == "see":
      print("You have", Money)
    elif cmd == "clear":
      os.system('clear')
      logo()
    elif cmd == "exit":
      db["Bank"] = Money
      print("Saving...")
      time.sleep(1)
      print("Saved, Exiting...")
      time.sleep(1)
      print("Goodbye!")
      exit(1)
    else:
      print("\033[31m")
      print("Error unknown command!")
      print("\033[0m")


def logo():
  print("First Home Store")
  print()
  print("------------")
  print()


logo()

YrN = input("Set money? Y or N\n").lower()
if YrN == "y":
  Money = int(input("Set money: "))
  db["Bank"] = Money
elif YrN == "n":
  db["Bank"] = Money
  print("You have", Money)
os.system('clear')
logo()
Shop()```