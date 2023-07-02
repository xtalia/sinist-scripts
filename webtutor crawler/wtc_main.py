# Serg Sinist test helper for get answers in t2 etc
# ver 0.03
# За помощь спасибо Андрею Малахову из евки


# pip install bs4, lxml, requests, colorama
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
from certifi import contents
from colorama import Fore
from ast import While
import requests
import os
from os import path
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs
from colorama import init as kek
kek()  # для иницилизации колорамы
CCC = 0

# константы цветов, чтобы каждый раз не писать Fore...
C, G, M, R, RR = Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.RESET
__location__ = path.realpath(path.join(os.getcwd(), path.dirname(__file__)))


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def readlink(link):

    if link == "111":
        
        with open(os.path.join(__location__ +  '\debug.xml'), 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, "xml")
            qss = soup.find_all('item')
            print(R, "DEBUG")

            
    else:
        # парсинг ссылки link, где есть object_id и part_code
        parsed_url = urlparse(link)
        atl = parse_qs(parsed_url.query)['object_id'][0]
        code = parse_qs(parsed_url.query)['part_code'][0]

        # сцепление ссылки, ведущей на искомый xml файл с его выводом
        url = "https://abc.tele2.ru/qti_return.html?atl=" + atl + "&code=" + code + \
            "&charset=utf-8"
        print(M, url)
        url_link, url_link.encoding = requests.get(url), 'utf-8'
        soup = BeautifulSoup(url_link.text, "xml")
        qss = soup.find_all('item')

# цикл, который вытаскивает сначала заголовки вопросов в параметре title в теге item
    # for qs in qss:
    #     print(M + '\n' + "<?> " + RR + qs.get('title') + M + " <?>" + RR + '\n')
    #     ass = qs.find('response_lid')
    #     meme = ass.find_all("response_label", {"ws_right": "1"})
    #     for sas in meme:
    #         print(G + ">> ", RR + sas.find('mattext').text)
    counter = 0
    for qs in qss:
        counter += 1
        print(C + '\n' + " <" + str(counter) + "> " + RR + qs.get('title') + M + RR + '\n')
        ass = qs.find('response_lid')
        meme = ass.find_all("response_label", {"ws_right": "1"})
        for sas in meme:
            print(G + ">> ", RR + sas.find('mattext').text)



def start():
    # start programm

    print(G + "sergsinist webtutor answer crawler")
    start = input(C + "Вставьте ссылку теста из браузера, где есть кнопка начать\продолжить тест: " + RR)
    while start.strip():
        try:
            readlink(start)
        except Exception:
            print(R + "Возникла ошибка - попробуйте снова вставить ссылку", RR)
        start = input("Можете повторить или нажать Enter для выхода: ")
        cls()
    else:
        quit()


if __name__ == "__main__":
    start()