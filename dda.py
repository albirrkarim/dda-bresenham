import matplotlib.pyplot as plt
import cv2

x1 = 10
y1 = 70

x2 = 70
y2 = 150


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
    

# Draw point based on above x, y axis values.
plt.scatter(x_number_list, y_number_list, s=1)

# Set chart title.
plt.title("Algoritma DDA")

# Set x, y label text.
plt.xlabel("X")
plt.ylabel("Y")
plt.show()