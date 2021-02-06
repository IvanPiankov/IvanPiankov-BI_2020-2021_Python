import random
import matplotlib.pyplot as plt
import numpy as np

n = int(input())
x = np.zeros(n)
y = np.zeros(n)
direct = ["up", "down", "right", "left"]
for i in range(1,n):
    path = random.choice(direct)
    if path == "up":
        x[i] = x[i-1]
        y[i] = y[i-1]+1
    elif path == "down":
        x[i] = x[i-1]
        y[i] = y[i-1]-1
    elif path == "right":
        x[i] = x[i-1]+1
        y[i] =y[i-1]
    else:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
plt.title(f'Random walk n = {n}')
plt.plot(x,y, color='blue')
plt.show()