percent_list_new_all = [[1.0, 2.0, 3.0, 4.0, 5.0], [6.0, 7.0, 8.0, 9.0, 10.0],
         [11.0, 12.0, 13.0, 14.0, 15.0], [16.0, 17.0, 18.0, 19.0, 20.0], [21.0, 22.0, 23.0, 24.0, 25.0],
         [21.0, 22.0, 23.0, 24.0, 25.0]]

# 5层级
# list1 = [5.0, 9.0, 13.0, 15.0]
# 4个商品
real_price_list = [2, 4, 6, 8, 10, 12]
# ls = []
# ls2 = []
# for s in range(len(lists)):
#     for a in range(len(percent_lists_new)):
#         for i in range(len(percent_lists_new[a])):
#             ss = percent_lists_new[s][i] * lists[s]
#             ls.append(ss)
# print(ls)

# 第一个列表的第N个元素 乘以第二个列表对应的第N个元素
list2 = []
for i in range(len(percent_list_new_all)):
    for s in range(len(percent_list_new_all[i])):
        ss = percent_list_new_all[i][s] * real_price_list[i]
        list2.append(ss)
list3 = []
for i in range(0, len(list2), len(percent_list_new_all[1])):
    list3.append(list2[i:i + len(percent_list_new_all[1])])
print(list3)
