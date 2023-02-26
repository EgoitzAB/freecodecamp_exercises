import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = line.slope*x_pred + line.intercept
    plt.plot(x_pred,y_pred,'r')
    # Create second line of best fit
    new_df = df.loc[df['Year']>=2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res_2 = linregress(new_x,new_y)
    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = res_2.slope*x_pred2 + res_2.intercept
    plt.plot(x_pred2,y_pred2,'green')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level') 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()