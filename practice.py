#Practice Problems : http://www.codeabbey.com/index/task_view/min-of-three

#Sum two numbers
X = 5
Y = 6
print (X+Y)


#Sum in a loop
list = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in list:
    sum += i 
print(sum)

#Summing from two list
listA = [1,2,3,4,5,6,7,8,9]
listB = [1,2,3,4,5,6,7,8,9]
listC = [listA[i]+listB[i] for i in range(len(listA))]
print (listC)
#zipped_list = zip(listA,listB)
#sum = [x+y for (x,y) in zipped_list]
#print(sum)

#Minimum of Two 
lista = [8,5,17,15]
listb = [1,4,70,20]
listc = []
for i in range(0,len(lista)):
    if lista[i] < listb[i]:
        listc.append(lista[i])
    else:
        listc.append(listb[i])
print(listc)

#Min of Three
list1 = [7,3,5]
list2 = [15,20,40]
list3 = [4,8,13]
list4 = []
for i in range(0,len(list1)):
    if list1[i] < list2[i]:
        if list1[i] < list3[i]:
            list4.append(list1[i])
        else:
            list4.append(list3[i])
    else:
        if list2[i] < list3[i]:
            list4.append(list2[i])
        else:
            list4.append(list3[i])
print(list4)

#Min Max of array
list5 = []
i = 1
while i <= 300:
    list5.append(i)
    i= i+1
print("Min = " + str(min(list5)))
print("Max = " + str(max(list5)))
