import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

―――――――――――――――――――――――――――――――――――――
 _______  _______  _______  _______        
/ ___   )(  ____ \(  ____ )(  ___  )
\/   )  || (    \/| (    )|| (   ) |
    /   )| (__    | (____)|| |   | |
   /   / |  __)   |     __)| |   | |
  /   /  | (      | (\ (   | |   | |
 /   (_/\| (____/\| ) \ \__| (___) |
(_______/(_______/|/   \__/(_______)
                                                                                                                   
―――――――――――――――――――――――――――――――――――――
                                                                 
By: @imtheisobhan on telgram 
""")

def display_menu():
    print(Fore.BLUE + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. ddos 1             
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Scripts/ddos4.1.py"')
    else:
        print(Fore.RED + 'Invalid option! Please choose the correct one.')


while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
