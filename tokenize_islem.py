from trtokenizer.tr_tokenizer import  WordTokenizer
import re

f = open("turkce-stop-words.txt", "r", encoding="utf-8")

stop_words = f.read().split("\n")

word_tokenizer = WordTokenizer()

def tokenize(string):
    arr = word_tokenizer.tokenize(string)
    arr = [item for item in arr if not item in stop_words]
    for i in range(len(arr)):
        arr[i] = re.sub(r'#[^\s]+','', arr[i])
        arr[i] = re.sub('((www.[^\s]+)|(https?://[^\s]+))','', arr[i])
        arr[i] = re.sub(r'[^\w\s]','',arr[i])
        arr[i] = re.sub(r'(?:^| )\w(?:$| )','', arr[i])
        bfr = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)
        arr[i] = bfr.sub(f'',arr[i])
    arr = [item for item in arr if not item.isdigit()]
    arr = [item for item in arr if not item == ""]
    return arr

