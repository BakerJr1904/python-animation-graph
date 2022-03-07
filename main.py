import pandas as pd
import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()  # Clears axis
    plt.plot(x, y1, label='Sensor 1')
    plt.plot(x, y2, label='Sensor 2')
    plt.plot(x_vals, y_vals)

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)  # gcf - get current figure; interval=1000 = 1 second

plt.title('Practice Data')
plt.tight_layout()
# plt.savefig('data/pie.png')
plt.show()