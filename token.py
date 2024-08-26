import os 
import time 

os.system("clear")
print()
token = input("\033[32m\033[1m [\033[36m$\033[32m]\033[33m Enter Your Token : \033[36m")
file=open("token.txt", "w")
file.write(token)
file.close()

file = open("token.txt", "r")
data = file.read()
file.close()

time.sleep(2)
print()

print("\033[32m\033[1mThanks! Your Token have Been saved as token.txt.")
print()
restart=input(" \033[32m[\033[36m→\033[32m] \033[33mPress Enter to Restart the Program")
os.system("python main.py")
