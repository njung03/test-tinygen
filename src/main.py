import os
import sys
from colorama import Fore
import requests


def run_bash_file_from_string(s: str):
    """Runs a bash script from a string"""
    with open('temp.sh', 'w') as f:
        f.write(s)
    os.system('bash temp.sh')
    os.remove('temp.sh')

def process():
    result = "result"
    response = input(Fore.RED + '>> Do you want to run this program? [Y/n] ')
    if response == '' or response.lower() == 'y':
        print(Fore.LIGHTBLACK_EX + '\nRunning...\n')
        run_bash_file_from_string(result)
    else:
        print(Fore.LIGHTBLACK_EX + 'Aborted.')


def main():
    process()


if __name__ == '__main__':
    process()