#hello 

list1 = [1,2,4,5]
list2 = [4,8,9,12,34,78]


minimum_length = len(list1) if len(list1) < len(list2) else len(list2)

print (minimum_length)

index_list1 = 0
index_list2 = 0

list3 = []

while True:
    if list1[index_list1] == list2[index_list2]:
        list3.append(list1[index_list1])
        list3.append(list2[index_list2])
        index_list1 += 1
        index_list2 += 1
    elif list1[index_list1] < list2[index_list2]:
        list3.append(list1[index_list1])
        index_list1 += 1
    elif list2[index_list2] < list1[index_list1]:
        list3.append(list2[index_list2])
        index_list2 += 1

    if index_list2 > (minimum_length-1) or index_list1 > (minimum_length-1):
        break

print (index_list2, index_list1)

#conditionals

print ([*list3,*list2[index_list2:]])

'''

length_of_array1: int = len(list1)
length_of_array2: int = len(list2)

list3: list = []

for i in range(length_of_array1):
    for j in range(length_of_array2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            list3.append(list2[j])
        elif list1[i] == list2[j]:
            list3.append(list1[i])
            list3.append(list2[j])
        else:
            list3.append(list2[j])
            list3.append(list1[i])
print (list3)

'''

