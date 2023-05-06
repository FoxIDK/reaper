# Imports.
import sys # System stuff.
import os # Operating System functions.
import argparse # For adding arguments.
from colorama import Fore # For text colour.

# Modules.
import src.modules.github as github
import src.modules.phone as phone
import src.modules.shodan as shodan

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# Config (Prints).
print_text = (f"{Fore.WHITE}") # Change the colour of text output in the client side prints.
print_dividers = (f"{Fore.LIGHTRED_EX}") # Changes the [], | and : in the client side prints.
print_success = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESS{Fore.WHITE}]") # Success output.
print_successfully = (f"{Fore.WHITE}[{Fore.GREEN}SUCCESSFULLY{Fore.WHITE}]") # Successfully output.
print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]") # Failed output.
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]") # Prompt output.
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]") # Notice output.
print_question =  (f"{Fore.WHITE}[{Fore.YELLOW}?{Fore.WHITE}]") # Alert output.
print_alert =  (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}!{Fore.WHITE}]") # Alert output.
print_exited = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}EXITED{Fore.WHITE}]") # Execited output.
print_disconnected = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}DISCONNECTED{Fore.WHITE}]") # Disconnected output.
print_command = (f"\n[{Fore.YELLOW}>_{Fore.WHITE}]: ") # Always asks for a command on a new line.

# Arg parser.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-github',     help='Gets information based on Github.',                    action="store_true")
ap.add_argument('-shodan',     help='Gets ISP, location, etc from Shodan even open-ports!', action="store_true")
ap.add_argument('-phone',      help='Gets information about a phone number, globally.',     action="store_true")
args = vars(parser.parse_args())

if args['github']: # Runs the keygen program.
    while True:
        try:
            github.github()
            os._exit(0) 
        except:
            print(f"{print_prompt} {print_failed}: Github module failed to run here!\n")
            os._exit(0) 

if args['phone']: # Runs the keygen program.
    while True:
        try:
            phone.phone()
            os._exit(0) 
        except:
            print(f"{print_prompt} {print_failed}: Phone module failed to run here!\n")
            os._exit(0) 

if args['shodan']: # Runs the keygen program.
    while True:
        try:
            shodan.run_shodan()
            os._exit(0) 
        except:
            print(f"{print_prompt} {print_failed}: Shodan module failed to run here!\n")
            os._exit(0) 

# Program.
if __name__ == '__main__':
    try:
        print("Did you use the argument correctly?")
    except KeyboardInterrupt:
        print(f"\n{print_exited} {print_notice} {print_successfully}\n")
        print(f'{print_notice} You interrupted the program.\n')
        try:
            sys.exit(0) 
        except SystemExit:
            os._exit(0) 
    except FileNotFoundError as not_found:
        print("This file is missing:" + not_found.filename)