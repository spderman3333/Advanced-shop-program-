from replit import db
import os
import time

print("Welcome to Stefan's Bank")

def login():
  pass

def register():
  pass

def Error():
  print("\033[31m")
  print("Error, Command not found!")
  print("\033[0m")

while True:
  print("Please choose one of these options:")
  print("1) login into existing account")
  print("2) register new account")
  option = int(input("Choose option: "))
  if option == 1:
    login()
    break
  elif option == 2:
    register()
    break
  else:
    Error()
    
# db["Bank"] = Money