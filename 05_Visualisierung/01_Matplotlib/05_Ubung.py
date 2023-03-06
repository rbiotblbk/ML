from matplotlib import pyplot as plt 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)
import numpy  as np


def ak_curve(count=7000, delta_min= -5, delta_max=5):
    
    
    value = 0
    
    y= []
    #x = [i for i in range(count)]
    x = np.arange(0,count)
    
    for i in range(count): 
       
        delta = np.random.uniform(delta_min,delta_max, size = (1,))[0]
        value += delta
        if value < 0:
            value = 0
            
        y.append(value)
        
    return x, y
    
     
        
    
    
x,y = ak_curve()

    
    
    
# 1. Create a figure (Window)
fig = plt.figure()

# 2. Create a draw area (Subplot)
ax = fig.add_subplot(111)  # 1:row, 1: column, 1:index of the area

# 3. Draw the graph/plot in the draw area
ax.plot(x, y, color = "blue", linewidth = 1, linestyle = "-", label = "Firma GmbH")



# 4. Plot configuration
#plt.legend() # show the legend
plt.grid(False)
plt.xlabel("Day")
plt.ylabel("Price")
plt.title("Aktienkurs")

# Save the plot as an image
plt.savefig("./images/myfigure2.png")

# 6. show the plot to the user
plt.show()