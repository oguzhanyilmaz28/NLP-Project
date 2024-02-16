import re

def nokta_silme(string):
    silinecekler = ''' !()-[]{};:'"\, <>./?@#$%^&*_~ '''
    for row in string:
        if row in silinecekler:
            string = string.replace(row, ' ')
    return string

def bosluklari_kaldir(metin):
    temiz_metin = re.sub(r'\n\s*', '\n', metin)
    return temiz_metin

