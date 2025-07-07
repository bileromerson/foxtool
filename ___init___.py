#!/usr/bin/env python3.13
# Version 1.2

import os

import subprocess
from time import sleep

header = """\033[38;5;214m
                                 ██▄              ▄██   
                                 ████▄          ▄████   
                                 ██████▄      ▄██████   
                                ▄████████████████████▄  
                              ▄████    ████████    ████▄
                              ██████████████████████████
                              ▀██████████    ██████████▀
                                ▀████████████████████▀  
        
                     \033[34m[✔] https://github.com/bileromerson/foxtool [✔]

                     \033[34m[✔]              Version 1.2                [✔]
                     \033[30m[-]         inspired by: setoolkit          [-]
                     \033[91m[X]  Please Don't Use For illegal Activity  [X]
\033[97m"""

if __name__ == "__main__":
        print(header)
        try:
                print("""
                      [@] set your vulnerability test option:
                      [1] XSS Payload Test
                      \033[91m[2] SQL Injection Test\033[97m
                      [5] EXIT
                """)

                choice = input("input =>>  ").strip()

                while choice =='2':
                        print('''
                        \033[91m This function does not exist at the moment.
                        \033[34m please try again.\033[97m
                        ''')
                        choice = input("input =>>  ").strip()
                while choice == '3':
                        print('''
                        \033[91m This function does not exist at the moment.
                        \033[34m please try again.\033[97m
                        ''')
                        choice = input("input =>>  ").strip()
                while choice == '4':
                        print('''
                        \033[91m This function does not exist at the moment.
                        \033[34m please try again.\033[97m
                        ''')
                        choice = input("input =>>  ").strip()
                        
                if choice == '1':
                        subprocess.run(["python", f"{os.getcwd()}/foxtool/tools/xss_payloads.py"])
                
                else:
                        print("try again...")
                        sleep(1)

        except KeyboardInterrupt:
                print("\nExiting ...")
                sleep(2)