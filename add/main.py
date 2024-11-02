import requests

def ayir(a):
    if a[0] == ' ':
        return ayir(a[1:])
    return a


with open('word.txt','r',encoding="utf8") as f:
    k = 0
    a = []
    for i in f.readlines():
        if '[ ]' in i or '[x]' in i:
            if '[ ]' in i:
                i = i.replace('[ ]','[x]')
            a.append(i[i.find('[x]  ')+5:])
            k += 1

for i in a:
    i = i.split()
    if len(i) < 3:
        i += ['-'] * len(i)
    chine = ayir(i[0])
    pinyin = ayir(i[1])
    s = i[2:]
    translate = ''
    for i in s:
        translate +=" " +  ayir(i)
    
    x = requests.get(f'http://127.0.0.1:8000/word/add/?chine={chine}&pinyin={pinyin}&translate={translate[1:]}')
    print(x.text)