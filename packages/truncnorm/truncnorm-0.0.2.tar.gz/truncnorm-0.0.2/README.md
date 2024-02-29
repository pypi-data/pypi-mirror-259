# TruncNorm

Arbitrary order moments for truncated multivariate normal distributions.

## Introduction

Given

```
X ~ N(m, C), a <= X <= b
```

with mean vector `m`, covariance matrix `C`, lower limit vector `a` and upper
limit vector `b`,

``` python
import truncnorm
truncnorm.moments(m, C, a, b, 4)
```

returns all the following moments of total order less or equal to 4 as a list:

```
[
  P(a<=X<=b),           (scalar)
  E[X_i],               (N vector)
  E[X_i*X_j],           (NxN matrix)
  E[X_i*X_j*X_k],       (NxNxN array)
  E[X_i*X_j*X_k*X_l],   (NxNxNxN array)
]
```

for all `i`, `j`, `k` and `l`. Note that the first element in the list is a bit
of a special case. That's because `E[1]` is trivially `1` so giving the
normalisation constant instead is much more useful.

## TODO

- Double truncation
- Numerical stability could probably be increased by using logarithic scale in
  critical places of the algorithm
- Sampling (see Gessner et al below)
- Folded distribution
- Optimize recurrent integrals by using vector and index-mapping representation
  instead of arrays. Using arrays makes computations efficient and simple, but
  same elements are computed multiple times because of symmetry in the moments.

## References

- "On Moments of Folded and Truncated Multivariate Normal Distributions" by
Raymond Kan & Cesare Robotti, 2016

- "Integrals over Gaussians under Linear Domain Constraints" by Alexandra Gessner
& Oindrila Kanjilal & Philipp Hennig, 2020
