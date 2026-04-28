# ECRI Statistics foundations
# Chapter 7: Modelling
# Jesús Urtasun Elizari: RCDS 2026



# Exercise 1:

# 1. Load data from the three csv files inside the data/ directory.

# 2. For each, do a scatter plot of the first two columns and discuss the relationship.

# 3. Implement a manual calculation of the Pearson correlation coefficient.

# 4. Verify implementation with pandas .corr() function.



# Import libraries ............................................................

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Pearson correlation .........................................................

def pearson_manual(x, y):

    # Compute expected values
    x_bar = x.mean()
    y_bar = y.mean()
    
    # Compute Pearson correlation coefficient
    cov = np.sum((x - x_bar) * (y - y_bar)) / (len(x) - 1)
    std_x = x.std()
    std_y = y.std()
    
    return cov / (std_x * std_y)



# 1. Linear dataset ...........................................................

linear = pd.read_csv("data/1_force_wire.csv")

# Select all rows, first column as x, second column as y
x = linear.iloc[:, 0]
y = linear.iloc[:, 1]
print("\nLinear dataset")
print("Mean (x, y):", x.mean(), ", ", y.mean())
print("Variance (x, y):", x.var(), ", ", y.var())

# Scatter
plt.figure()
plt.scatter(x, y, s = 10, edgecolors = 'black')
plt.scatter(x.mean(), y.mean(), marker = 'x', s = 100)
plt.title("Scatter plot: linear")
plt.xlabel("x")
plt.ylabel("y = f(x)")
# plt.savefig("scatter_force_wire.png", dpi = 300, bbox_inches = "tight")
# plt.show()

# Compute manual correlation and compare with Pandas implementation
r_manual = pearson_manual(x, y)
r_library = x.corr(y)
print("Pearson r (manual):", r_manual)
print("Pearson r (pandas):", r_library)



# 2. Quadratic dataset ........................................................

quadratic = pd.read_csv("data/2_accelerated_motion.tsv", sep = "\t")

# Select all rows, first column as x, second column as y
x = quadratic.iloc[:, 0]
y = quadratic.iloc[:, 1]
print("\nQuadratic dataset")
print("Mean (x, y):", x.mean(), ", ", y.mean())
print("Variance (x, y):", x.var(), ", ", y.var())

# Scatter
plt.figure()
plt.scatter(x, y, s = 10, edgecolors = 'black')
plt.scatter(x.mean(), y.mean(), marker = 'x', s = 100)
plt.title("Scatter plot: quadratic")
plt.xlabel("x")
plt.ylabel("y = f(x)")
# plt.savefig("scatter_accelerated_motion.png", dpi = 300, bbox_inches = "tight")
# plt.show()

# Compute manual correlation and compare with Pandas implementation
r_manual = pearson_manual(x, y)
r_library = x.corr(y)
print("Pearson r (manual):", r_manual)
print("Pearson r (pandas):", r_library)



# 3. Sinusoidal dataset .......................................................

sinusoidal = pd.read_json("data/3_harmonic_motion.json")

# Select all rows, first column as x, second column as y
x = sinusoidal.iloc[:, 0]
y = sinusoidal.iloc[:, 1]
print("\nSinusoidal dataset")
print("Mean (x, y):", x.mean(), ", ", y.mean())
print("Variance (x, y):", x.var(), ", ", y.var())

# Scatter
plt.figure()
plt.scatter(x, y, s = 10, edgecolors = 'black')
plt.scatter(x.mean(), y.mean(), marker = 'x', s = 100)
plt.title("Scatter plot: sinusoidal")
plt.xlabel("x")
plt.ylabel("y = f(x)")
# plt.savefig("scatter_harmonic_motion.png", dpi = 300, bbox_inches = "tight")
# plt.show()

# Compute manual correlation and compare with Pandas implementation
r_manual = pearson_manual(x, y)
r_library = x.corr(y)
print("Pearson r (manual):", r_manual)
print("Pearson r (pandas):", r_library)



# Discussion:
# Linear: strong positive correlation
# Quadratic: non-linear, correlation misleading
# Sinusoidal: near zero correlation despite structure
