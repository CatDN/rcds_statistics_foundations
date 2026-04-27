# ECRI Statistics Foundations

### Chapter 7: Modelling

## 🧪 Exercise 1 — Correlation

1. Load:
   - `data/1_force_wire.csv`
   - `data/2_accelerated_motion.tsv`
   - `data/3_harmonic_motion.json`
2. Scatter plot (col1 vs col2) for each dataset  
3. Briefly **describe the relationship** (linear, non-linear, none)  
4. Implement Pearson correlation manually  
5. Verify with `x.corr(y)`

**Goal:** Understand correlation and its limits for non-linear data


## Exercise 2 — Curve Fitting

1. Load `data/3_harmonic_motion.json`  
2. Scatter plot + **describe pattern**  
3. Fit:
   - Linear (deg 1)
   - Quadratic (deg 2)
   - Sinusoidal (`curve_fit`)
4. Compute RSS:

5. Compare and **select best model**

**Goal:** Compare models and identify appropriate fit for periodic data


## Exercise 3 — Anscombe’s Quartet

1. Load:
- `data/anscombe1.csv` … `anscombe4.csv`
2. For each dataset compute:
- Mean, variance, correlation
3. Plot all (e.g. 2×2 grid)
4. **Discuss differences despite similar statistics**

**Goal:** Show why visualization is essential beyond summary statistics

