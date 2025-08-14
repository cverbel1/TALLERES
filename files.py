f= open('note.txt',mode='r',)
try:
    primero = f.readline()
    segundo= f.readline()
    resto = f.readlines()
    # print(resto)
finally:
    f.close()

    with open('note.txt',mode='r') as e:
        todo = e.readlines()
        for a in todo:
            print(a.strip())