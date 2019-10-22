import matplotlib.pyplot as plt
import cv2

import time
start_time = time.time()

# Titik awal
x1 = 1
y1 = 7

# Titik Akhir
x2 = 7
y2 = 15


dy = y2-y1
dx = x2-x1

step = dx  if dx > dy  else dy

xInc = dx / step
yInc = dy / step

x=x1
y=y1

len=y2+x2


# x axis value list.
x_number_list = []

x_number_list.append(x1)

# y axis value list.
y_number_list = []

y_number_list.append(y1)


for i in range(1,len):
    
    x = x + xInc 
    y = y + yInc

    xBulat=int(x)
    yBulat=int(y)
    
    x_number_list.append(xBulat)
    y_number_list.append(yBulat)

    if(x>=x2 and y>=y2):
        break
    

end_time = time.time()
delta_time = end_time-start_time
print("Execution Time : ",delta_time," ms")

# Draw point based on above x, y axis values.
plt.scatter(x_number_list, y_number_list, s=10)

# Set chart title.
plt.title("Algoritma DDA")

# Set x, y label text.
plt.xlabel("X")
plt.ylabel("Y")
plt.show()