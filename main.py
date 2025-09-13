#!/usr/bin/env python3.13
# Version 1.3

import os
import sys
import platform
import subprocess
from time import sleep
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assets.logo import logo
from core.color import correct,notgood,thing,reset,red,orange,gray

header = f"""\033[38;5;214m

                     {correct}             You're welcome               {correct+reset}

                     {thing}               Version 1.3                {thing+reset}
                     {notgood}  Please Don't Use For illegal Activity   {notgood+reset}
\033[97m"""
print(logo, header) # print the logo
if __name__ == "__main__":
        try:
                print(f"""
                      {orange}[@] set your vulnerability test option:
                      {gray}[1] XSS Payload Test
                      {red}[2] SQL Injection Test
                      {gray}[5] EXIT
                """)

                choice = input("input =>>  ").strip()

                if platform.system() == 'Windows':
                        os.system("cls")
                elif platform.system() == 'Linux':
                        os.system("clear")

                if choice == '1':

                        subprocess.run(["python", f"{os.getcwd()}/foxtool/tools/XssScan/xss_payloads.py"])
                
                else:
                        print("try again...")
                        sleep(1)

        except KeyboardInterrupt:
                print("\nExiting ...")
                sleep(2)