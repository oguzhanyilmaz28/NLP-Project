import requests
from bs4 import BeautifulSoup as bs
import csv
from nokta_silme import nokta_silme,bosluklari_kaldir
from tokenize_islem import tokenize

veri=[]
adres = 'https://www.ensonhaber.com/'
baslik = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
sayfa = requests.get(adres, headers=baslik)
soup = bs(sayfa.content, features="lxml")
haberbasiklar = soup.find_all('span',{'class':'text'})
for haber in haberbasiklar:
    veri.append([haber.text])

veri.pop()

with open('haberbaslik.csv', 'w',encoding='UTF-8', newline='') as dosya:
    writer = csv.writer(dosya)
    writer.writerows(veri)

print("'haberbaslik' adlı csv dosyası oluşturuldu.")


with open('haberbaslik.csv', 'r', encoding="utf-8") as f:
    data = f.read()

data = nokta_silme(data)
yorum = bosluklari_kaldir(data)
with open('haberbaslik.csv', 'w', encoding='utf-8') as dosya:
    dosya.write(yorum)



f = open('tokenize_basliklar.csv', 'w', encoding="utf-8")
writer = csv.writer(f)

with open("haberbaslik.csv", newline='\n', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        writer.writerow(tokenize(row[0]))

f.close()
print("'tokenize_haberbaslik' adlı csv dosyası oluşturuldu.")
