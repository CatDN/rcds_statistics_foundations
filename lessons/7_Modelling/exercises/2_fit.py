# ECRI Statistics foundations
# Chapter 7: Modelling
# Jesús Urtasun Elizari: RCDS 2026



# Exercise 2:

# 1. Load the 3_harmonic_motion.csv dataset from the data/ directory.

# 2. Do a scatter plot of the first two columns and discuss the relationship.

# 3. Implement a linear, polynomial, and sinusoidal fit with the np.polyfit() and np.polyval(coeffs_linear, x_vals)

# 4. Decide the best fitting curve by computing the Residual Sum of Squares (RSS) on the three attempts.



# Import libraries ............................................................

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# Load data ...................................................................

data = pd.read_json("data/3_harmonic_motion.json")

# Store columns as x and y
x = data.iloc[:, 0]
y = data.iloc[:, 1]

# Convert to numpy (cleaner handling)
x_vals = x.to_numpy()
y_vals = y.to_numpy()



# Scatter plot ................................................................

plt.figure()
plt.scatter(x_vals, y_vals, s = 10, edgecolors = 'black')
plt.title("Sinusoidal data")
plt.xlabel("x")
plt.ylabel("y = f(x)")
# plt.savefig("data_to_fit.png", dpi = 300, bbox_inches = "tight")
plt.show()



# Fit data ....................................................................

# 1. Linear fit
coeffs_linear = np.polyfit(x_vals, y_vals, 1)
y_linear = np.polyval(coeffs_linear, x_vals)

# 2. Polynomial fit (degree 5)
degree = 5
coeffs_poly = np.polyfit(x_vals, y_vals, degree)
y_poly = np.polyval(coeffs_poly, x_vals)

# 3. Sinusoidal fit: 

# Model: A * sin(omega * x + phi)
def sinusoidal(x, A, omega, phi):
    # A = amplitude, omega = angular frequency, phi = phase shift
    return A * np.sin(omega * x + phi)

# Initial guess for parameters (helps the fitting converge)
initial_guess = [5, 1, 0]

# Fit model to data (nonlinear least squares)
params, _ = curve_fit(sinusoidal, x_vals, y_vals, p0 = initial_guess)

# Generate fitted values using optimized parameters
y_sin = sinusoidal(x_vals, *params)



# Find the best model .........................................................

# RSS computation
def rss(y_true, y_pred):
    return np.sum((y_true - y_pred)**2)

# Compute RSS for each attempted fit
rss_linear = rss(y_vals, y_linear)
rss_poly = rss(y_vals, y_poly)
rss_sin = rss(y_vals, y_sin)
print("\nResidual Sum of Squares (RSS)")
print("Linear:", rss_linear)
print(f"Polynomial (degree {degree}):", rss_poly)
print("Sinusoidal:", rss_sin)

# Plot fitted curves
idx = np.argsort(x_vals)
plt.scatter(x_vals[idx], y_vals[idx], s = 10, edgecolors = 'black', label = "Observations")
plt.plot(x_vals[idx], y_linear[idx], label = "Linear fit")
plt.plot(x_vals[idx], y_poly[idx], label = f"Polynomial")
plt.plot(x_vals[idx], y_sin[idx], label = "Sinusoidal fit")
plt.legend()
plt.xlabel("x")
plt.ylabel("y = f(x)")
# plt.savefig("data_fitted.png", dpi = 300, bbox_inches = "tight")
plt.show()



# Discussion:
# Linear fit clearly does not capture or describe data
# Polynomial might overfit data
# Sinusoidal is best and achieves minimum RSS
