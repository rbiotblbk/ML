from matplotlib import pyplot as plt 
import numpy  as np

class Trend:

    def __init__(self, count) -> None:
        self.x_values = []
        self.y_values = []
        self.count = count 

        self.generate_data()


    def generate_data(self,delta_min:int= -5, delta_max:int=5) :
        """_summary_

        Args:
            count (int, optional): _description_. Defaults to 7000.
            delta_min (int, optional): _description_. Defaults to -5.
            delta_max (int, optional): _description_. Defaults to 5.

        Returns:
            tuple: _description_
        """
        current_value = 0
       
        
        # Generate X-Axes Values from Zero till count
        self.x_values = np.arange(0,self.count)
        
        # Generate Y-Axes values 
        for i in range(self.count): 
        
            delta = np.random.uniform(delta_min,delta_max, size = (1,))[0]
            current_value += delta
            
            # Check if negative -> put Zero
            if current_value < 0:
                current_value = 0
                
            # Add to my total list
            self.y_values.append(current_value)
            
         

    def plot_data(self, file_name = "myfigure2.png"):   
        # 1. Create a figure (Window)
        fig = plt.figure()

        # 2. Create a draw area (Subplot)
        ax = fig.add_subplot(111)  # 1:row, 1: column, 1:index of the area

        # 3. Draw the graph/plot in the draw area
        ax.plot(self.x_values, self.y_values, color = "blue", linewidth = 1, linestyle = "-", label = "Firma GmbH")



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
