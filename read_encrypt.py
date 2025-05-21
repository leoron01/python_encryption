
import random
import numpy as np



 
with open('test_script.exe', "rb") as f:
    data = f.read()
 
# Converte ogni byte in una stringa di 8 bit
binary_data = ' '.join(format(byte, '08b') for byte in data)
print(binary_data[0:1000])
random.seed(23)
keys = random.randint(0, len(data), 100)

for k in keys:

    if data[k] == 0:
       data[k] = 1
    else:
        data[k] = 0   




f.write(bin)
f.close()




