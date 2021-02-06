import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time

# First function for sorting list with using merge sort
def merge(a,b):
    c = []
    indexA, indexB = 0,0
    while indexA < len(a) and indexB <len(b):
        if a[indexA] < b[indexB]:
            c.append(a[indexA])
            indexA +=1
        else:
            c.append(b[indexB])
            indexB+=1
    return c + a[indexA:] + b[indexB:]
def my_sort(a):
    if len(a) <= 1:
        return a
    else:
        l = len(a) // 2
        left = a[0:l]
        right = a[l::]
        left  = my_sort(left)
        right = my_sort(right)
        return merge(left, right)
def is_sorted_monkey(data):
    return all(data[i] <= data[i+1] for i in range(len(data)-1))
def monkey_sort(data):
    while not is_sorted_monkey(data):
        random.shuffle(data)
    return data
def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):
            return True
    return False
def rand_listed(len):
    list_random = (random.sample(range(1000000), len))
    while is_sorted(list_random) is False:
        list_random = (random.sample(range(1000000), len))
    return list_random


len_list = int(input())
number = []
timer = []
type_sort =[]
for i in range(2, len_list+1):
    rand_list = rand_listed(i)
    for j in range(5):
        list_for_test = rand_list.copy()
        start_my_sort_time = time.perf_counter()
        my_sort(list_for_test)
        end_my_sort_time = time.perf_counter()
        my_sort_time = end_my_sort_time - start_my_sort_time
        number.append(i)
        timer.append(my_sort_time)
        type_sort.append("my_sort")
        start_monkey_time = time.perf_counter()
        monkey_sort(list_for_test)
        end_monkey_time = time.perf_counter()
        monkey_sort_time = end_monkey_time - start_monkey_time
        number.append(i)
        timer.append(monkey_sort_time)
        type_sort.append("monkey_sort")
index = [i for i in range(len(timer))]
df = pd.DataFrame({'Length_list,(elem)': number,
                   'Time,(s)': timer,
                   "Sort_type": type_sort}, index=index)

sns.barplot(x='Length_list,(elem)', y='Time,(s)', hue='Sort_type', data=df,
            palette='Blues', edgecolor='w').set_title(f"Changing the sorting time at the maximum length of the list = {len_list}")

plt.show()


