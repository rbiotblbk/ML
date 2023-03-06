from trend import Trend

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)



def main():   
    # Create Instances   
    trend1 = Trend(1000)
         
    # Plot Data
    trend1.plot_data()
  

if __name__ == "__main__":
    main()