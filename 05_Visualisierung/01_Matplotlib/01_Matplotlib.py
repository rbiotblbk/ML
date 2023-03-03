# pip install matplotlib

from matplotlib import pyplot as plt 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


x = [1,2,3,4,5,6,7]
y = [10,29,30,43,51,65,71]
z = [11,32,41,1,2,17,24]

# 1. Create a figure (Window)
fig = plt.figure()

# 2. Create a draw area (Subplot)
ax = fig.add_subplot(111)  # 1:row, 1: column, 1:index of the area

# 3. Draw the graph/plot in the draw area
ax.plot(x, y, color = "green", linewidth = 5, linestyle = "--", label = "Market Dev")
ax.plot(x, z, color = "blue", linewidth = 5, linestyle = ":", label = "Revenue")


# 4. Plot configuration
plt.legend() # show the legend
plt.grid(True)
plt.xlabel("Check Point")
plt.ylabel("Price")
plt.title("My first Diagram")

# Save the plot as an image
plt.savefig("./images/myfigure1.png")

# 6. show the plot to the user
plt.show()