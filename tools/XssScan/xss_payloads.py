# XSS Payload Test Tool
# Version 1.3
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from selenium import webdriver
from urllib import response
from core import configs
import requests
import base64
from time import sleep
from assets.logo import logo
from core.color import info,reset, good,blue,red,reset,what,orange
print(logo)
try:
    url = input('url =>> ')

    # Timeout e delay
    timeout = configs.timeout
    delay = configs.delay
    #======= for ======
    n ='1'
    for num in range(len(configs.blindParams)):# range(len(configs.blindParams))
        # params 
        params = configs.blindParams[num]
        
        for num2 in range(len(configs.payloads)):#range(len(configs.payloads))
            #payloads
            payload = configs.payloads[num2]
            if configs.toBase == True:
                    payload = base64.b64encode(payload.encode()).decode()
            # print(payload)
            print(payload)
            data = {params: payload}
            json_data = {"input": payload}
            # Headers
            headers = configs.headers.copy()
            if headers.get("User-Agent") == "$":
                headers["User-Agent"] = "Foxtool-Test"
            # Proxies
            proxies = configs.proxies

            # ===== GET =====
            try:
                resp_get = requests.get(url, params=params, headers=headers, timeout=timeout, proxies=proxies, verify=False)
                # print("GET status:", resp_get.status_code)
                # print(requests.post(url,json=params))
                sleep(delay)
                # ===== POST form-data =====
                resp_post = requests.post(url, data=data, headers=headers, timeout=timeout, proxies=proxies, verify=False)
                # print("POST status:", resp_post.status_code)
                sleep(delay)

                # ===== POST JSON =====
                resp_json = requests.post(url, json=json_data, headers=headers, timeout=timeout, proxies=proxies, verify=False)
                # print("POST JSON status:", resp_json.status_code)
                # print(data, json_data)
                
                # ==== print =====
                if payload in resp_get.text:
                    print(f"{good}Reflexo detectado na GET!{reset}")
                if payload in resp_post.text:
                    print(f"{good}Reflexo detectado na POST!{reset}")
                if payload in resp_json.text:
                    print(f"{good}Reflexo detectado no POST JSON!{reset}")

            except requests.ConnectionError:
                print(f"{what}Erro: fall on connect whith website{reset}")
                sys.exit()
            except requests.Timeout:
                print(f"{what}Erro: A conexão demorou muito!{reset}")
                sys.exit()
            except requests.RequestException as e:
                print(f"{what} general Error: {e}{reset}")
                sys.exit()
except KeyboardInterrupt:
        print("\nExiting ...")
        sleep(2)