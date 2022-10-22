name = input("Введите название файла: ")
file = open(name+".txt","a")
while(True):
        strok = input("Введите строку: ")
        if(len(strok) < 3 or strok.isalpha()==False):
            print("Введите только строку")
            continue
        else:
            file.write("\n" + strk)
            break
