import ast
import pandas as pd
from gensim.models import Word2Vec
import csv

def word2vec_create(value):
    model = Word2Vec(sentences=value.tolist(), vector_size=100, window=5, min_count=1)
    model.save("haber.model")

def word2vec_load(value):
    model = Word2Vec.load("haber.model")

    words = [word for word in value if word in model.wv.key_to_index]

    if not words:
        print("Kelime bulunamadı")
        return None

    vektor = [model.wv[word] for word in words]
    ort_vektor = sum(vektor) / len(vektor)

    return ort_vektor.tolist()

data = []

with open("tokenize_yorumlar.csv", newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        if len(row) > 0:
            data.append(row)


df = pd.DataFrame({
    "vektor": data
})

df["vektor2"] = df["vector"].apply(lambda x: ''.join(str(x)))
word2vec_create(df["vektor2"])
df["word2vec"] = df["vektor2"].apply(word2vec_load)
df["word2vec"].to_csv("input_test_yorum.csv", sep='\t', encoding='utf-8')
df = pd.read_csv('input_test_yorum.csv', sep="\t", encoding='utf-8')

df['word2vec'] = df['word2vec'].apply(ast.literal_eval)





