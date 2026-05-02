import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Load data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # First line of best fit (all data)
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880, 2051))
    ax.plot(years, intercept + slope * years, color="red")

    # Second line of best fit (from year 2000)
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, intercept2 + slope2 * years_recent, color="green")

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot
    fig.savefig("sea_level_plot.png")
    return fig