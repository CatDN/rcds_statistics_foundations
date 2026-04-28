# ECRI Statistics foundations
# Chapter 7: Modelling
# Jesús Urtasun Elizari: RCDS 2026



# Exercise 3:

# 1. Load the four anscombe csv files from the data/ directory.

# 2. Compute mean, variance and correlation for each of them.

# 3. Do a scatter plot of each of them.

# 4. Discuss the result and limitations of summary statistics.



# Import libraries ............................................................

import pandas as pd
import matplotlib.pyplot as plt

# File paths
files = [
    "data/anscombe1.csv",
    "data/anscombe2.csv",
    "data/anscombe3.csv",
    "data/anscombe4.csv"
]



# Compute summary statistics ..................................................

for f in files:

    # Read files
    df = pd.read_csv(f)
    x = df["x"]
    y = df["y"]

    # Compute summary statistics
    print(f"\n{f}")
    print("Mean (x, y):", x.mean(), ", ", y.mean())
    print("Variance (x, y):", x.var(), ", ", y.var())
    print("Correlation:", x.corr(y))



# Scatter plots ...............................................................

fig, axs = plt.subplots(2, 2, figsize = (8, 8))

for i, f in enumerate(files):

    # Read files
    df = pd.read_csv(f)
    x = df["x"]
    y = df["y"]

    # Plot in 2x2 grid
    ax = axs[i // 2, i % 2]
    ax.scatter(x, y, s = 20, edgecolors = 'black')
    ax.set_title(f)

plt.tight_layout()
# plt.savefig("anscombe_quartet.png", dpi = 300, bbox_inches = "tight")
# plt.show()



# Discussion (...):
