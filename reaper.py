# Imports
import sys
import os
import argparse
from colorama import Fore
import src.modules.github as github
import src.modules.phone as phone
import src.modules.shodan as shodan

# Configuration
sys.tracebacklimit = 0

print_failed = (f"{Fore.WHITE}[{Fore.LIGHTRED_EX}FAILED{Fore.WHITE}]")
print_prompt = (f"{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]")
print_notice = (f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]")

parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('-github', help='Gets information based on Github.', action="store_true")
ap.add_argument('-phone', help='Gets information about a phone number, globally.', action="store_true")
ap.add_argument('-shodan', help='Gets ISP, location, etc from Shodan even open-ports!', action="store_true")
ap.add_argument('-ip', help='Gets ISP, location, etc from Shodan even open-ports!', action="store_true")
args = vars(parser.parse_args())

# Handle command-line arguments
if args['github']:
    while True:
        try:
            github.github(); os._exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Github module failed to run here!\n"); os._exit(0)

if args['phone']:
    while True:
        try:
            phone.phone(); os._exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Phone module failed to run here!\n"); os._exit(0)

if args['shodan'] or args['ip']:
    while True:
        try:
            shodan.run_shodan(); os._exit(0)
        except:
            print(f"{print_prompt} {print_failed}: Shodan module failed to run here!\n"); os._exit(0)

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