# with open("mutiefendi.txt","r+",encoding='utf-8') as file:
#     print(file.read())
# with open("mutiefendi.txt","r+",encoding='utf-8') as file:
#     file.write("deneme")

#------ sayfa sonunda güncelleme ----------
# with open("mutiefendi.txt","a",encoding='utf-8') as file:
#     file.write("\nmusa cetinkaya")

# with open("mutiefendi.txt","r",encoding='utf-8') as file:
#     print(file.read())
#------ sayfa başında güncelleme ----------
# with open("mutiefendi.txt","r+",encoding='utf-8') as file:
#     content = file.read()
#     content= "nurcan \n" + content
#     file.seek(0)
#     file.write(content)

# with open("mutiefendi.txt","r",encoding='utf-8') as file:
#     print(file.read())


#------ sayfa ortasında güncelleme ----------

with open("mutiefendi.txt","r+",encoding='utf-8') as file:
    content = file.readlines()
    content.insert(1,"Eray çetinkaya\n")
    file.seek(0)
    for i in content:
        file.write(i)
        file.writelines(content)

with open("mutiefendi.txt","r",encoding='utf-8') as file:
    print(file.read())