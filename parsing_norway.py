import json
import os
import pathlib

from bs4 import BeautifulSoup
import requests


def get_page():
    url = "https://www.norway.no/ru/belarus/-/"
    return requests.get(url)


def get_contacts():
    page = get_page()

    soup = BeautifulSoup(page.text, 'html.parser')
    main_part = soup.find('article', class_='article corearticle-page')
    s = str(main_part.find_all('p'))

    # extract adress
    adress = s[s.find("Адрес:") + 6: s.find("220050") + 6].replace('</p>, <p>', '')

    # extract phone
    phone = s[s.find("Телефон:") + 8: s.find("ца)") + 3]

    # extarct email
    email = s[s.find("Адрес электронной почты:") + 41: s.find("info.nomsq@vfshelpline.com") + 26]

    map_info = {
        "Adress": adress,
        "Phone": phone,
        "Email": email
    }

    res_map = {
        "Center": map_info
    }

    return res_map


def get_news():
    page = get_page()

    soup = BeautifulSoup(page.text, 'html.parser')
    main_part = soup.find('article', class_='article corearticle-page')
    s = str(main_part)
    headers = []
    p = soup.find_all('strong')

    for u in p:
        headers.append(u.text)

    list_news = []

    for i in range(len(headers)):
        dict_news = {}

        dict_news["header"] = headers[i]
        if i == len(headers) - 1:
            dict_news["new"] = str(BeautifulSoup(s[s.find(headers[i]):], 'html.parser')
                                   .text.replace("\n", ""))
            list_news.append(dict_news)
            break
        dict_news["new"] = str(BeautifulSoup(s[s.find(headers[i]): s.find(headers[i + 1])], 'html.parser')
                               .text.replace("\n", ""))
        list_news.append(dict_news)

        i += 1

    return list_news


def save_to_json(information, name_file):
    path = pathlib.Path("./" + name_file + ".json")
    if path.exists():
        os.remove(path)
        with open("./" + name_file + ".json", "w", encoding="utf-8") as f:
            json.dump(information, f, ensure_ascii=False, indent=4)
    else:
        with open("./" + name_file + ".json", "w", encoding="utf-8") as f:
            json.dump(information, f, ensure_ascii=False, indent=4)

    print("file saved")


def get_all_news():
    res = {"News": get_news()}
    return res


#if __name__ == "__main__":
def get_and_save_information():
    save_to_json(get_contacts(), "contacts")
    save_to_json(get_all_news(), "news")
