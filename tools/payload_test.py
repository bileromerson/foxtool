import os
import sys
# Add the base path to sys.path
import requests
import platform
from time import sleep

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

print("""\033[38;5;214m
                                 ██▄              ▄██   
                                 ████▄          ▄████   
                                 ██████▄      ▄██████   
                                ▄████████████████████▄  
                              ▄████    ████████    ████▄
                              ██████████████████████████
                              ▀██████████    ██████████▀
                                ▀████████████████████▀  
                      [@] choose your payload vulnerability test:
                      \033[34m[1] payload test simple
                      \033[91m[2] payload test advanced
                      \033[97m[3] EXIT
\033[97m""")
def payload_test(url, file):
    print(f"\n\033[38;5;214m[INFO] testing the {url}:\033[97m\n")

    # load payloads
    with open(file, 'r') as loadPayloads: # open payloads folder
        payloads = loadPayloads.readlines() # read
    payloads = [linha.strip() for linha in payloads]

    try: # start test
        line = []
        for payload in payloads:
            params = {'search': payload}
            response = requests.get(url, params=params)

            print(f"\033[34m[INFO] Testing payload: {payload}\033[97m")
            print(f"Request status: {response.status_code}")
            
            if "error" in response.text.lower():

                print("\033[91m[INFO] Possible vulnerability detected. \033[97m \n")
                line = line + [f"\033[91m{payload}\033[97m"]
                               
            elif "unexpected" in response.text.lower():

                print("\033[0m[INFO] The site may be vulnerable. \033[97m \n")
                line = line + [f"\033[0m{payload}\033[97m"]

            else:
                print("\033[32m[INFO] No vulnerability detected. \033[97m\n")
    
        else: # when the process is over
            print("\n\033[32m<<--------------------------------------->>\033[97m\n")

            for captured_tests in line:
                 print(f"{captured_tests}\n") # print the payload tests

    except requests.exceptions.RequestException as erro:
        print(f"\033[91m[ERRO] Request failed: {erro}\033[97m \n")
        print(erro)
        sleep(2)

    except KeyboardInterrupt:
        pass
        

try:
    choice = input("input =>>  ")

    if choice =='1':
        url = input("Input URL: ") # Target URL
        file = "foxtool/tools/payloads.txt"
        
        if "http://" not in url: # complete url
            if "https://" not in url:
                url = "http://"+url # new url value

        payload_test(url, file)

    elif choice =='2':
        url = input("Input URL: ") # Target URL
        file = input("what is the file path:  ") # file path

        if "http://" or "https://" not in url: # complete url
            url = "https://"+url # new url value

        while os.path.isdir(file) or not os.path.exists(file): # if the file or arquive does not exist
            print("try again")
            file = input("what is the file path:  ")

        else:
            payload_test(url,file)

    else:
        print("try again ...")
        sleep(1)

except KeyboardInterrupt:
    pass