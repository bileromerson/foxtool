#!/usr/bin/env python3.13
# Version 1.2

import os
import sys
import subprocess
from time import sleep
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assets.logo import logo

header = """\033[38;5;214m
        
                     \033[34m[✔] https://github.com/bileromerson/foxtool [✔]

                     \033[34m[✔]              Version 1.2                [✔]
                     \033[30m[-]         inspired by: setoolkit          [-]
                     \033[91m[X]  Please Don't Use For illegal Activity  [X]
\033[97m"""
print(logo, header) # print the logo
if __name__ == "__main__":
        try:
                print("""
                      [@] set your vulnerability test option:
                      [1] XSS Payload Test
                      \033[91m[2] SQL Injection Test\033[97m
                      [5] EXIT
                """)

                choice = input("input =>>  ").strip()
                        
                if choice == '1':
                        subprocess.run(["python", f"{os.getcwd()}/foxtool/tools/xss_payloads.py"])
                
                else:
                        print("try again...")
                        sleep(1)

        except KeyboardInterrupt:
                print("\nExiting ...")
                sleep(2)