import os
import time
import random

# ANSI color escape codes
COLORS = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
    '\033[97m'   # White
]

RESET_COLOR = '\033[0m'  # Reset color to default
CYAN = '\033[96m'

def crack_wifi():
    os.system("sudo python cracker.py -i wlan0 --iface-down -K")

def main_menu():
    banner = f"""
{random.choice(COLORS)}
  ██████  ██▓ ▄▄▄       ███▄ ▄███▓    █     █░ ██▓  █████▒██▓
▒██    ▒ ▓██▒▒████▄    ▓██▒▀█▀ ██▒   ▓█░ █ ░█░▓██▒▓██   ▒▓██▒
░ ▓██▄   ▒██▒▒██  ▀█▄  ▓██    ▓██░   ▒█░ █ ░█ ▒██▒▒████ ░▒██▒
  ▒   ██▒░██░░██▄▄▄▄██ ▒██    ▒██    ░█░ █ ░█ ░██░░▓█▒  ░░██░
▒██████▒▒░██░ ▓█   ▓██▒▒██▒   ░██▒   ░░██▒██▓ ░██░░▒█░   ░██░
▒ ▒▓▒ ▒ ░░▓   ▒▒   ▓▒█░░ ▒░   ░  ░   ░ ▓░▒ ▒  ░▓   ▒ ░   ░▓  
░ ░▒  ░ ░ ▒ ░  ▒   ▒▒ ░░  ░      ░     ▒ ░ ░   ▒ ░ ░      ▒ ░
░  ░  ░   ▒ ░  ░   ▒   ░      ░        ░   ░   ▒ ░ ░ ░    ▒ ░
      ░   ░        ░  ░       ░          ░     ░          ░  
                                                             
{RESET_COLOR}
"""
    while True:
        print(banner)
        print("\nPlease select an option:")
        print(f"{CYAN}[1]{RESET_COLOR} {CYAN}Crack WiFi{RESET_COLOR}")
        print(f"{CYAN}[2]{RESET_COLOR} {CYAN}Exit{RESET_COLOR}")
        choice = input(f"{CYAN}Enter your choice: {RESET_COLOR}")

        if choice == '1':
            os.system('clear') 
            time.sleep(1)
            crack_wifi()
        elif choice == '2':
            print("Byeee...")
            break
        else:
            for _ in range(1):
                time.sleep(0.5)
            time.sleep(0.5)
            os.system('clear') 

if __name__ == "__main__":
    main_menu()
