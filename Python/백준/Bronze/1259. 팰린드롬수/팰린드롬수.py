def pal(text):
    l = len(text) -1
    for i in range(l):
        if text[i] != text[l-i]:
            print('no')
            return
    print('yes')
    return

while(True):
    text = input()
    if text =='0':
        break
    pal(text)
    