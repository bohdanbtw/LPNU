print("Hello world!")
import numpy as pd
import matplotlib.pyplot as plt

array = pd.random.rand(100)

plt.plot(array)
plt.xlabel("Індекс")
plt.ylabel("Значення")
plt.show()