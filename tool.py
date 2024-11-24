#!/usr/bin/env python3
# Version 1.0
import os
import subprocess
from time import sleep

logo = """\033[38;5;214m
                                 ██▄              ▄██
                                 ████▄          ▄████
                                 ██████▄      ▄██████
                                ▄████████████████████▄
                              ▄████    ████████    ████▄
                              ██████████████████████████
                              ▀██████████    ██████████▀
                                ▀████████████████████▀
                                    
                     \033[34m[✔]       https://github.com/nome         [✔]
                     \033[34m[✔]            Version 1.0                [✔]
                     \033[30m[-]       inspired by: hackingtool        [-]
                     \033[91m[X] Please Don't Use For illegal Activity [X]
\033[97m """

if __name__ == "__main__":
        print(logo)
        try:
                print("""
                      [@] set your option:
                      [1] SQL VULNERABILITY
                      [2] EXIT
                """)

                choice = input("input =>>").strip()

                if choice == "1":
                        subprocess.run(["python", f"{os.getcwd()}/foxtool/tools/sql_code.py"])


                else:
                        print("try again...")
                        sleep(1)

        except KeyboardInterrupt:
                print("\nExiting ...")
                sleep(2)