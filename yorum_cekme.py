from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from nokta_silme import nokta_silme,bosluklari_kaldir
from tokenize_islem import tokenize


url = "https://www.ensonhaber.com/ekonomi/tcmb-acikladi-yeni-200-liralik-banknotlarda-imzalar-degisti"

options = webdriver.ChromeOptions();
options.add_experimental_option('excludeSwitches', ['enable-logging']);

def scrape_comments(url):
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get(url)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    bs = BeautifulSoup(browser.page_source, "html.parser")

    yorum= bs.find("div", class_="comments-list")

    p = yorum.find_all("p")
    print(p)
    f = open('yorum.csv', 'w', encoding="utf-8")
    baslik = ["yorum"]
    writer = csv.writer(f)
    writer.writerow(baslik)
    for item in p:
        row = [str(item.get_text())]
        writer.writerow(row)
    f.close()


with open('yorum.csv', 'r', encoding="utf-8") as f:
    data = f.read()

data = nokta_silme(data)
yorum = bosluklari_kaldir(data)

with open('yorum.csv', 'w', encoding='utf-8') as dosya:
    dosya.write(yorum)


print("'yorum' adlı csv dosyası oluşturuldu.")

f = open('tokenize_yorumlar.csv', 'w', encoding="utf-8")
writer = csv.writer(f)

with open("yorum.csv", newline='\n', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        writer.writerow(tokenize(row[0]))

f.close()

print("'tokenize_yorumlar' adlı csv dosyası oluşturuldu.")