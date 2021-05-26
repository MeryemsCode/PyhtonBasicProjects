list1 = [i for i in range(10) if i % 2==0]
print(list1)

list2 = [i for i in range(10) if i % 2==1]
print(list2)

listSon=list1+list2
print(listSon)


listEnSon=[i * 2 for i in listSon]
print(listEnSon)
