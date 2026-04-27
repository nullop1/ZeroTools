import sys,os
from colorama import Fore

print(Fore.BLACK+"""
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
                                                                
       """)


print(Fore.RED + 'recoded and recreated by @imtheisobhan on Telgram')


def display_menu():
    print(Fore.GREEN + """
    1: StableBypasser (DDos)
    2: CheckHost (Check Sites And Resolve Sites)
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Scripts/stablebypasser.py"' if os.name == 'nt' else 'python Scripts/stablebypasser.py')
    if command == '2':
        os.system('cmd /k "python Scripts/checkhost.py"' if os.name == 'nt' else 'python Scripts/checkhost.py')
        display_menu()
    else:
        print('invailed CMD !!! ')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
