# Importing all the neccessary libraries/module
from colorama import *
import phonenumbers
from phonenumbers import carrier,geocoder,timezone
import time
import subprocess

print(Fore.GREEN+"   This tool is still under development,               \nsome functions might not work properly...")
time.sleep(3)
subprocess.call('clear', shell=True)
time.sleep(3)
print(Fore.YELLOW+"   Type start to start the tool")
command=input(Fore.GREEN+"           Enter option >>: ")
time.sleep(3)
def tool():
	print("           This tool is for educational purposes only....")
	time.sleep(3)
subprocess.call('clear',shell=True)
# Next line contains an error so i comment it out and make it a default scan.
'''        Feel free to tweak the code however you want'''
#	num=input(Fore.GREEN+"       Enter the target number with country code.    \nenter here >>: ")
num=("+2348035884831")
#my father's phone above'
phonenumbers.parse(num)
print(f'  Phone_Nubmer: {num}')
#name=timezone.time_zones_for_number(num)
#print(name)
if command:
	tool()	
# To be continued...
