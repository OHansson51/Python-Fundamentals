import numpy as np
import matplotlib.pyplot as plt
import math
import pathlib

my_path = pathlib.Path(__file__).parent.resolve()
filename = f"{my_path}/in_data.txt"

with open(filename) as f_data:
    lines = f_data.readline().split(sep=',')
    y_vals = list(map(float, lines))
    np.array(y_vals)

x_vals = np.linspace(0, 10, len(y_vals))
#print(x_vals)

plt.plot(x_vals,y_vals)
plt.show()