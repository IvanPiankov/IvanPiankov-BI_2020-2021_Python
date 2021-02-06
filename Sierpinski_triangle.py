import random
import matplotlib.pyplot as plt

def plot(p):
    p_x = [x for (x,y) in p]
    p_y = [y for (x,y) in p]
    plt.title(f'Sierpinski triangle n = {itaration_number}')
    plt.plot(p_x,p_y, '.', color='blue')
    plt.show()

def triangle(itaration_number):
    v = [(0.0, 0.0), (0.5, 1.0), (1, 0.0)]
    p = []
    x,y = random.choice(v)
    for _ in range(itaration_number):
        new_x,new_y = random.choice(v)
        x = (new_x + x) / 2.0
        y = (new_y + y) / 2.0
        p.append((x,y))
    plot(p)

itaration_number = int(input())
triangle(itaration_number)

