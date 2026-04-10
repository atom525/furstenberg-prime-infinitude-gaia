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
| `thm_infinitude_primes` | There are infinitely many primes: $\#P = \aleph_0$ |
| `thm_density_iff_infinite` | $\#P = \aleph_0$ iff $P$ is dense in $(\\mathbb{N}, \tau)$ |
| `thm_p_dense_x1` | $P$ is dense in $X_1 = (\mathbb{N} \setminus \\{1\\}, \tau_1)$ |
| `thm_subset_dense_iff_infinite` | For $A \subseteq P$: $A$ dense iff $\#A = \aleph_0$ |

### Holes (independent premises requiring external prior)

| Label | Statement |
|-------|-----------|
| `gcd_multiplicativity` | $\gcd(x,n)=1 \wedge \gcd(x,m)=1 \iff \gcd(x,nm)=1$ |
| `fundamental_theorem_arithmetic` | Every $n>1$ is divisible by some prime |
| `closure_union_containment` | $\bigcup \operatorname{cl}(A_\alpha) \subseteq \operatorname{cl}(\bigcup A_\alpha)$ |
| `density_transitivity` | Density is transitive in topological spaces |
| `sigma_n_infinite` | Each $\sigma_n$ is infinite |

## Belief propagation results

Using the included `self_review` sidecar (9 priors assigned):

| Claim | Belief |
|-------|--------|
| `thm_infinitude_primes` | **0.794** |
| `thm_p_dense_x1` | 0.783 |
| `thm_density_iff_infinite` | 0.761 |
| `thm_closure_n` | 0.831 |
| `lem_density_equivalence` | 0.937 |
| `x1_dense_in_x` | 0.926 |

Method: Junction Tree (exact), converged in 2 iterations, treewidth 3.

## Installation

```bash
uv add "furstenberg-prime-infinitude-gaia @ git+https://github.com/atom525/furstenberg-prime-infinitude-gaia@v0.1.0"
```

## Usage

```python
from prime_topo import thm_infinitude_primes, thm_density_iff_infinite
```

```bash
gaia compile .
gaia check .
gaia infer . --review self_review
```

## Modules

- **`motivation.py`** -- Coprimality sets $\sigma_n$, Furstenberg topology $\tau$, base properties (Thm 0.1)
- **`closure.py`** -- Closure characterization: $\operatorname{cl}_X(\{p\}) = M_p$, $\operatorname{cl}_X(\{n\}) = \bigcap M_p$ (Lem 0.4, Thm 0.5)
- **`density.py`** -- Density equivalence, main infinitude theorem, generalization (Thm 0.7--0.14)

## License

This is an AI-generated formalization. Belief values reflect the graph's probabilistic assessment, not the original author's confidence.
