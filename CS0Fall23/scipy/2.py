import numpy as np
import matplotlib.pyplot as plt
import math


x_vals = np.linspace(0, 2*math.pi, 100)
print(x_vals)

y_vals = np.sin(x_vals)

print(y_vals)

plt.plot(x_vals,y_vals, color="green")
plt.plot(x_vals,y_vals+x_vals, color="red")
plt.title("My first Python Plot!")
plt.show()