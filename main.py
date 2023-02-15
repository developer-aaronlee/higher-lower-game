import numpy as np


num_list1 = [0, 1, 2, 3, 4, 5]
num_list2 = [3, 4, 5, 6, 7, 8]
num_test = np.array(num_list1) & np.array(num_list2)
print(num_test)