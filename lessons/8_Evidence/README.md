# ECRI Statistics Foundations

## Chapter 8: Evidence

## Exercise 1: Bayesian probability

1. Simulate an example where two dice are given, one fair with `P(6) = 1/6` and other biased `P(6) = 1/2`.

2. Compute the Bayesian probability of choosing the biased one, if:
    - 1st roll gives a `6` 
    - 2nd roll also gives a `6`

3. Simulate an example of a very rare disease, present only in `5%` of population, and a test with `99%` accuracy.

4. Compute the Bayesian probability of actually having the disease, if:
    - 1st test gives a `+`
    - 2nd test also gives a `+`

## Exercise 2: Posterior evolution

1. Simulate an example where two dice are given, one fair with `P(6) = 1/6` and other biased `P(6) = 1/2`.

2. Compute the Bayesian probability of choosing the biased one, if:
    - 1st roll gives a `6` 
    - 2nd roll also gives a `6`

3. Simulate 50 rolls and compute the total updated probability `P(bised | E)` and `P(fair | E)` given the results `E`

4. Plot both probabilities in terms of the number of rolls.

## Exercise 3: Bayesian inference

1. Suppose we observe the following sequence of coin tosses: `x = (1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0)` with `1 = heads` and `0 = tails`.

2. Compute the number of heads `k` and total number of trials `n`, and compute the posterior distribution for `\theta` (probability of H) given the observed x.

3. Plot the prior and posterior distributions of `\theta`.

4. Discuss how the observed data influence the updated belief about `\theta`.
