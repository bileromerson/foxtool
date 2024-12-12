#!/usr/bin/env python3.13
# Version 1.1

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
        
                     \033[34m[✔]       https://github.com/nome         [✔]
                     \033[34m[✔]            Version 1.1                [✔]
                     \033[30m[-]       inspired by: hackingtool        [-]
                     \033[91m[X] Please Don't Use For illegal Activity [X]
\033[97m"""

if __name__ == "__main__":
        print(header)
        try:
                print("""
                      [@] set your vulnerability test option:
                      [1] Payload Test
                      \033[91m[2] SQL injection\033[97m
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
                        subprocess.run(["python", f"{os.getcwd()}/foxtool/tools/payload_test.py"])
                
                else:
                        print("try again...")
                        sleep(1)

        except KeyboardInterrupt:
                print("\nExiting ...")
                sleep(2)