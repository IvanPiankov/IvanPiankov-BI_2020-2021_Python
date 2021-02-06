import random
import matplotlib.pyplot as plt

def plot(p):
    p_x = [x for (x,y) in p]
    p_y = [y for (x,y) in p]
    plt.title(f'Sierpinski carpet n = {itaration_number}')
    plt.plot(p_x,p_y, '.', color='blue')
    plt.show()

def carpet(itaration_number):
    v = [(0.0, 0.0), (0.0, 0.5), (0.0, 1), (0.5, 1), (1, 1), (1, 0.5), (1, 0.0), (0.5, 0)]
    p = []
    x,y = random.choice(v)
    for _ in range(itaration_number):
        new_x,new_y = random.choice(v)
        x = ((2*new_x) + x) / 3.0
        y = ((2*new_y) + y) / 3.0
        p.append((x,y))
    plot(p)

itaration_number = int(input())

carpet(itaration_number)
