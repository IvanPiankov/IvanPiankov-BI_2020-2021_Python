import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time
#Num_and_random
number = int(input())
number_iter = []
timer = []
type_package =[]
for i in range(0, number, 1000):
    for j in range(3):
        start_time_num = time.perf_counter()
        num = np.random.uniform(size=i)
        end_time_num = time.perf_counter()
        num_time = end_time_num - start_time_num
        number_iter.append(i)
        timer.append(num_time)
        type_package.append("numpy_time")
        start_time_rand = time.perf_counter()
        rand = [random.random() for k in range(i)]
        end_time_rand = time.perf_counter()
        random_time = end_time_rand - start_time_rand
        number_iter.append(i)
        timer.append(random_time)
        type_package.append("random_time")
index = [i for i in range(len(timer))]

df = pd.DataFrame({'Amount of elements,(elem)': number_iter,
                   'Time,(s)': timer,
                   "Name package": type_package}, index=index)

sns.pointplot(x='Amount of elements,(elem)', y='Time,(s)', hue="Name package", data=df,
            palette='Blues', edgecolor='w').set_title(f"Execution speed with number of elements = {number}")

plt.show()