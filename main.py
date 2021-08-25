from matplotlib import pyplot as plt
import random
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation
import csv



usd_tryvalue = []
zaman = []

index = count()

def realtime(i):
    zaman.append(next(index))
    usd_tryvalue.append(random.randint(1, 5000))
    plt.cla()
    plt.plot(zaman, usd_tryvalue)

gunc = FuncAnimation(plt.gcf(), realtime, interval=1000)








plt.show()
