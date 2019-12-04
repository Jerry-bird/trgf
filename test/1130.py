import numpy as np

d = 0
list1 = [[0.87, 0.87, 0.87, 0.87, 0.87], [0.97, 0.97, 0.97, 0.97, 0.97],
         [0.97, 0.97, 0.97, 0.97, 0.97], [0.77, 0.77, 0.77, 0.77, 0.77], [0.68, 0.68, 0.68, 0.68, 0.68]]
for i in range(len(list1)):
    print(np.array(list1[i]))
    d = d + np.array(list1[i])
print(d)
