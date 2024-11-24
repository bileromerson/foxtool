#!/usr/bin/env python3
# Version 1.0
import subprocess
from time import sleep
from platform import system

logo = """\033[33m
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
                      [@] set your attack option:
                      [1] Manual
                      [2] Default
                """)

                choice = input("input =>>").strip()

                if choice == "1":
                        subprocess.run(["python", "foxtool/tools/h.py"])

                else:
                        print("try again...")
                        sleep(1)

        except KeyboardInterrupt:
                print("\nExiting ...")
                sleep(2)