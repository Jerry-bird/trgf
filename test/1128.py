list1 = [[1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 4.0, 5.0]]
list4 = []
for i in range(len(list1)):
    list3 = list1[i][0:1]
    for s in range(len(list1[i]) - 1):
        a = list1[i][s + 1] - list1[i][s]
        list3.append(a)
    list4.append(list3)
print(list4)


# list2 = [1.0, 2.0, 3.0, 4.0, 5.0]
# list3 = list2[0:1]
# for i in range(len(list2)-1):
#     a = list2[i+1]-list2[i]
#     list3.append(a)
# print(list3)