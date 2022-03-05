import requests
try:
    response = requests.get('http://www.pudim.com.br/')
except requests.exceptions.ConnectionError:
    print('\033[31mO site Pudim nao está acessivel!\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
