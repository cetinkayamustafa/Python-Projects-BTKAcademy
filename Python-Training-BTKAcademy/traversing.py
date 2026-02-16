with open("newfile.txt","r",encoding='utf-8') as file:

    content = file.read()
    print(file.tell())
    file.seek(10)
    print(content)
