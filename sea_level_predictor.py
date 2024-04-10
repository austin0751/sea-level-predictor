import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], label='Sea Level')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(1880, 2051)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, label='Best Fit Line 1', color='red')

    # Create second line of best fit
    recent_years_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years_df['Year'], recent_years_df['CSIRO Adjusted Sea Level'])
    x_values_recent = range(2000, 2051)
    y_values_recent = slope_recent * x_values_recent + intercept_recent
    plt.plot(x_values_recent, y_values_recent, label='Best Fit Line 2', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()