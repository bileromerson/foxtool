import os
import requests
from time import sleep
os.system("clear")
print("""
                      [@] choose your payload vulnerability test:
                      [1] payload test simple
                      [2] EXIT
""")

choice = input("input =>>  ")

def simple_payload_test(url):
    
    print(f"\n\033[38;5;214m[INFO] testing the {url}:\n")

    # load payloads
    with open('foxtool/tools/payloads.txt', 'r') as loadPayloads: # open payloads folder
        payloads = loadPayloads.readlines() # read
    payloads = [linha.strip() for linha in payloads]

    try: # start test
        for payload in payloads:
            params = {'search': payload}
            response = requests.get(url, params=params)

            print(f"\033[34m[INFO] Testing payload: {payload}\033[97m")
            print(f"Request status: {response.status_code}")
            
            if "error" in response.text.lower():
                print("\033[91m[INFO] Possible vulnerability detected. \033[97m \n")
            elif "unexpected" in response.text.lower():
                print("\033[0m[INFO] The site may be vulnerable. \033[97m \n")
            else:
                print("\033[32m[INFO] No vulnerability detected. \033[97m \n")

    except requests.exceptions.RequestException as e:
        print(f"\033[91m[ERRO] Request failed: {e}\033[97m \n")
        sleep(2)

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)

if choice !='2': # if nox EXIT
    url = input("Input URL: ") # Target URL

    if "http://" or "https://" not in url: # complete url
        url = "https://"+url # new url value

    if choice =='1':
        simple_payload_test(url)

elif choice =='2': # EXIT (choice 2)
    print("\nExiting ..!!!")
    sleep(2)

else:
    print("try again ...")
    sleep(1)