import time
start = time.time()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('inizio...')

x = np.linspace(0, 10, 100000)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
print(f'tempo di esecuzione: {time.time() - start} \n' )
plt.show()

input('premi invio per uscire')



