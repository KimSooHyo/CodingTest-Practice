def special(month, day):
    if month < 2:
        print("Before")
        return
    elif month > 2:
        print("After")
        return
    else:
        if day < 18:
            print("Before")
            return
        elif day > 18:
            print('After')
        else:
            print('Special')
            return

month = int(input())
day = int(input())

special(month, day)