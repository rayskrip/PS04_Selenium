from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
search_text = input('введите запрос: ')
search_box.send_keys(search_text)
search_box.send_keys(Keys.ENTER)

browser.find_element(By.CLASS_NAME, "searchmatch").click()

action = int(input('введите 1, если хотите листать параграфы текущей статьи, '
                   'введите 2, если хотите перейти на одну из связанных страниц, '
                   'введите 3, если хотите выйти из программы '))

if action == 1:
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

elif action == 2:
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "mw-content-ltr mw-parser-output":
             hatnotes.append(element)

    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    time.sleep(10)
elif action == 3:
    browser.close()

action = int(input('введите 1, если хотите листать параграфы текущей статьи, '
                   'введите 2, если хотите перейти на одну из связанных страниц'))

if action == 1:
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

elif action == 2:
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "mw-content-ltr mw-parser-output":
             hatnotes.append(element)

    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    time.sleep(10)



