# Serg Sinist test helper for solve memes in Tele2 or test like
# ver 0.03
# За помощь спасибо Андрею Малахову из евки


# pip install bs4, lxml, requests
from ast import While
import requests
import os
from bs4 import BeautifulSoup
# import lxml
from urllib.parse import urlparse
from urllib.parse import parse_qs


def test_roulette(link):

    # парсинг ссылки link, где есть object_id и part_code
    parsed_url = urlparse(link)
    atl = parse_qs(parsed_url.query)['object_id'][0]
    code = parse_qs(parsed_url.query)['part_code'][0]

    # сцепление ссылки, ведущей на искомый xml файл с его выводом
    url = "https://abc.tele2.ru/qti_return.html?atl=" + atl + "&code=" + code + "&charset=utf-8"  # если у вас web tutor, то данную переменную можете изменить
    print(url)
    url_link = requests.get(url)
    url_link.encoding = 'utf-8'

    soup = BeautifulSoup(url_link.text, "xml")
    qss = soup.find_all('item')

# цикл, который вытаскивает сначала заголовки вопросов в параметре title в теге item
    for qs in qss:
        print("********************************")
        print("<?> " + qs.get('title') + " <?>")
        print("********************************")
        ass = qs.find('render_choice')
        for sas in ass:
            # поиск всех ответов с выводом значения верного\неверного ответа (1\0)
            # print(">> "+ str(sas.find('material').text) + ' ' + str(sas.get('ws_right')))
            # вывод правильного ответа
            if sas.get('ws_right') == "1":
                print(">> " + sas.find('material').text)
            else:
                print("---")


def start():
    # start programm

    print("***")
    print("***")
    print("sergsinist webtutor answer crawler")
    print("***")
    print("***")
    start = input("Вставьте ссылку теста из браузера, где есть кнопка начать\продолжить тест: ")
    while start.strip():
        try:
            test_roulette(start)
        except Exception:
            print("Возникла ошибка - попробуйте снова вставить ссылку")
        start = input("Можете повторить или нажать Enter для выхода: ")
        os.system('CLS')
    else:
        quit()


if __name__ == "__main__":
    start()