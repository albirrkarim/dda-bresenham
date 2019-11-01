import matplotlib.pyplot as plt
import cv2


import time
start_time = time.time()

# Titik Awal
x1 = 1
y1 = 7

# Titik Akhir
x2 = 7
y2 = 15

# Perhitungan
dy = y2-y1
dx = x2-x1

#  Hitung Median 
m = dy / dx

dy=abs(dy)
dx=abs(dx)

duaDX=2*dx
duaDY=2*dy

selisihDua=duaDY-duaDX

p = duaDY-dx

len=x2+y2

x=x1
y=y1

if(m>=1):
    selisihDua=duaDX-duaDY
    p=duaDX-dy


# x axis value list.
x_number_list = []

x_number_list.append(x1)

# y axis value list.
y_number_list = []

y_number_list.append(y1)

for i in range(1,len):
    
    #  Incremental 
    if(0 < m < 1):
        #  0 < m < 1
        if(p > 0):
            x = x + 1
            y = y + 1

            p = p + selisihDua
        else:
            x = x + 1
            y = y

            p = p + duaDY

    elif( m < 0 ):
        # m < 0 
        if(p > 0):
            x = x + 1
            y = y - 1

            p = p + selisihDua
        else:
            x = x + 1
            y = y

            p = p + duaDY

    else:
        #  1 < m 
        if(p > 0):
            x = x + 1
            y = y + 1

            p = p + selisihDua
        else:
            x = x 
            y = y +1

            p = p + duaDX

    x_number_list.append(x)
    y_number_list.append(y)

    if((x>=x2) and (y>=y2) ):
        break

end_time = time.time()
delta_time = end_time-start_time
print("Execution Time : ",delta_time," ms")

from guppy import hpy

h = hpy()

print (h.heap())

# Draw point based on above x, y axis values.
plt.scatter(x_number_list, y_number_list, s=10)

# Set chart title.
plt.title("Algoritma Bresenham")

# Set x, y label text.
plt.xlabel("X")
plt.ylabel("Y")
plt.show()