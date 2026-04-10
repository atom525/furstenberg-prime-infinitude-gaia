# furstenberg-prime-infinitude-gaia

A [Gaia](https://github.com/SiliconEinstein/Gaia) knowledge package formalizing the topological proof of the infinitude of prime numbers.

**Source paper:** M. Lobo, *Another Topological Proof of the Infinitude of Prime Numbers* ([arXiv:2402.03356](https://arxiv.org/abs/2402.03356))

## Overview

This package encodes the complete argument from the paper using the Furstenberg-style coprimality topology on $\mathbb{N}$. The core insight: primes are infinite if and only if they form a dense subset of a natural topological space on the positive integers.

### Knowledge graph

| Category | Count |
|----------|-------|
| Settings | 5 |
| Claims | 22 |
| Deduction strategies | 10 |
| Exported claims | 4 |
| Holes (premises) | 5 |

### Proof chain

```
gcd_multiplicativity + sigma_n_infinite + FTA + closure_union + density_transitivity
        |                    |               |          |                |
        v                    |               |          |                |
    thm_base ----------------+               |          |                |
        |                                    |          |                |
        v                                    |          |                |
  lem_closure_prime                          |          |                |
        |                                    |          |                |
        v                                    |          |                |
   thm_closure_n                             |          |                |
        |                                    v          v                |
        +--------------------> thm_p_dense_x1 <--------+                |
                                     |                                  |
                                     v                                  |
                             thm_density_iff_infinite                   |
                                     |                                  v
                                     +----------> thm_infinitude_primes
```

### Exported claims

| Label | Statement |
|-------|-----------|
|  | There are infinitely many primes |
|  | Infinitude iff density in X |
|  | P is dense in X_1 |
|  | For A subset P: A dense iff infinite |

### Holes (independent premises requiring external prior)

| Label | Statement |
|-------|-----------|
|  | GCD multiplicativity |
|  | Every n>1 divisible by some prime |
|  | Union of closures in closure of union |
|  | Density is transitive |
|  | Each sigma_n is infinite |

## Belief propagation results

Using the included  sidecar (19 priors assigned to both independent and derived claims):

| Claim | Belief |
|-------|--------|
|  | **0.9999** |
|  | 0.9993 |
|  | 0.9996 |
|  | 0.9995 |
|  | 0.9997 |
|  | 0.9996 |
|  | 0.9898 |

Method: Junction Tree (exact), converged in 2 iterations, treewidth 3.

## Installation

```bash
uv add furstenberg-prime-infinitude-gaia @ git+https://github.com/atom525/furstenberg-prime-infinitude-gaia@v0.1.0
```

## Usage

```python
from furstenberg_prime_infinitude import thm_infinitude_primes, thm_density_iff_infinite
```

```bash
gaia compile .
gaia check .
gaia infer . --review self_review
```

## Modules

- **** -- Coprimality sets, Furstenberg topology, base properties (Thm 0.1)
- **** -- Closure characterization (Lem 0.4, Thm 0.5)
- **** -- Density equivalence, main infinitude theorem, generalization (Thm 0.7--0.14)
