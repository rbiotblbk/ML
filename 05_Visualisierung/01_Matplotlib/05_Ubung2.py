from matplotlib import pyplot as plt 
import os 
from pathlib import Path 
import numpy  as np

os.chdir(Path(__file__).parent)

def generate_data(count:int=7000, delta_min:int= -5, delta_max:int=5) -> tuple:
    """_summary_

    Args:
        count (int, optional): _description_. Defaults to 7000.
        delta_min (int, optional): _description_. Defaults to -5.
        delta_max (int, optional): _description_. Defaults to 5.

    Returns:
        tuple: _description_
    """
    current_value = 0
    y_values= []
     
    # Generate X-Axes Values from Zero till count
    x_values = np.arange(0,count)
    
    for i in range(count): 
       
        delta = np.random.uniform(delta_min,delta_max, size = (1,))[0]
        current_value += delta
        
        # Check if negative -> put Zero
        if current_value < 0:
            current_value = 0
            
        # Add to my total list
        y_values.append(current_value)
        
    return x_values, y_values

def plot_data(x_values, y_values, file_name = "myfigure2.png"):   
    # 1. Create a figure (Window)
    fig = plt.figure()

    # 2. Create a draw area (Subplot)
    ax = fig.add_subplot(111)  # 1:row, 1: column, 1:index of the area

    # 3. Draw the graph/plot in the draw area
    ax.plot(x_values, y_values, color = "blue", linewidth = 1, linestyle = "-", label = "Firma GmbH")



    # 4. Plot configuration
    #plt.legend() # show the legend
    plt.grid(False)
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.title("Aktienkurs")

    # Save the plot as an image
    plt.savefig("./images/" + file_name)

    # 6. show the plot to the user
    plt.show()


def main():      

    # Generate Data
    x_values, y_values = generate_data()

    # Visualize
    plot_data(x_values, y_values, "mohamed.png")   
        
        
   

if __name__ == "__main__":
    main()