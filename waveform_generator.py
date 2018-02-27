import numpy as np
import matplotlib.pyplot as plt

dr = int(1e9)
fs = int(10e9)

data = "10101010101100110011001110111011101110"
bits = len(data)
data_v = ""
for i in range(len(data)):
    data_v = data_v + data[i]*(int(fs/dr))

data_v = (i for i in data_v)

data_t = bits*int(fs/dr)
data_t = (i*(1/fs) for i in range(data_t))

plt.plot(list(data_t), list(data_v))
plt.show()
