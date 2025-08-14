# XSS Payload Test Tool
# Version 1.2
import os
import sys
from urllib import response
import requests
import platform
import requests
from time import sleep
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assets.logo import logo    

caminho_driver = './chromedriver'

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

print(logo, """\033[38;5;214m
                      [@] choose your payload vulnerability test:
                      \033[34m[1] payload test simple
                      \033[91m[2] payload test advanced
                      \033[97m[3] EXIT
\033[97m""")
def payload_test(url, file):
    print(f"\n\033[38;5;214m[INFO] testing the {url}:\033[97m\n")
    print(f"\033[38;5;214m[INFO] using payloads from: {file}\033[97m\n")

    # load payloads
    with open(file, 'r') as loadPayloads: # open payloads folder
        payloads = loadPayloads.readlines() # read
        payloads = [linha.strip() for linha in payloads]

    try: # start test
        line = []
        for payload in payloads:
            response = requests.get(url, params={'search': payload})
            startScript = payload.find("<script>") # example payload
            endScript = payload.find("</script>")
            anotherForms = "javascript:alert('XSS')" # another example payload ATENTION: the payload neads to alert('XSS')
            script = payload[startScript:endScript + len('</script>')] # extract the script part from the payload

            print(f"\033[34m[INFO] Testing payload: {payload}\033[97m")
            print(response.url)
            print(f"Request status: {response.status_code}")
            print(f"Response length: {len(response.text)} characters\n")
            if script.lower() in response.text.lower(): # check if the payload is in the response text (I need to repair the javascript:alert part for acept all payloads)
                print(script)
                print("\033[91m[INFO] Possible vulnerability detected. \033[97m\n")
                line.append(f"\033[91m{payload}\033[97m")
            else:
                print("\033[32m[INFO] nothing here... \033[91m")
                print(f"\033[38;5;214m[INFO] Payload {payload} not found in response.\033[97m\n")
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
        url = input("Input URL: ").strip() # Target URL
        file = "foxtool/txts/xss_payloads.txt" # file path
        if "http://" not in url and "https://" not in url: # complete url
            url = "http://"+url # new url value
        payload_test(url, file)

    elif choice =='2':
        url = input("Input URL: ").strip() # Target URL
        file = input("what is the file path:  ") # file path

        if "http://" not in url and "https://" not in url: # complete url
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


# this is verry hard for me, thank you for the test. :3