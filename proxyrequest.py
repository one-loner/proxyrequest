import requests
import socks
import socket

def main():
    print('Данная программа производит Get запросы до https://ifconfig.me/ip через SOCKS-прокси на 127.0.0.1 ')
    pi=input('Введите порт, на котором поднят прокси [9050]: ')
    if pi == '':
       p=9050
       print('Выбран порт по умолчанию (9050)')
    else:
       p=int(pi)

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", p)
    socket.socket = socks.socksocket


    url = 'https://ifconfig.me/ip'
    response = requests.get(url)
    print(response.text)

if __name__ == "__main__":
    main()
