from matplotlib import pyplot as plt 


x = [1,2,3,4,5,6,7]
y = [10,29,30,43,51,65,71]
z = [11,32,41, 1, 2, 17,24]


# Subplot (row_count, column_count, ID of the axes)
plt.subplot(2, 2 , 1)
plt.plot(x, y, color = "blue")


plt.subplot(2, 2 , 2)
plt.plot(x, y, color = "green")


plt.subplot(2, 2 , 3)
plt.plot(x, y, color = "red")


plt.subplot(2, 2 , 4)
plt.plot(x, y, color = "black")

# Show window
plt.show()