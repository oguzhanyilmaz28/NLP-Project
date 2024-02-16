import csv
from sklearn.preprocessing import LabelBinarizer
from tokenize_islem import tokenize
from nokta_silme import nokta_silme,bosluklari_kaldir

inputFile ="yorum_veriseti.csv"


data = []
target=[]

try:
    with open(inputFile, newline='\n', encoding="utf-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for row in spamreader:
            print(row)
            data.append(row[0])
            target.append(row[1])
except:
    csvfile.close()
csvfile.close()

ds=[]
for a in data:
    b=nokta_silme(a)
    b = bosluklari_kaldir(b)
    b=tokenize(b)
    ds.append(b)

lb=LabelBinarizer()
kategori_list=lb.fit_transform(target)

with open('tokenize_yorum_veriseti.csv', 'w',encoding='UTF-8', newline='') as dosya:
    writer = csv.writer(dosya)
    writer.writerows(ds)


with open('target_yorum.csv', 'w',encoding='UTF-8', newline='') as dosya:
    writer = csv.writer(dosya)
    for a in kategori_list:
        writer.writerow(a)









