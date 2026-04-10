"""Closure Characterization in X

Characterizes the closure of singleton sets in $X = (\\mathbb{N}, \\tau)$.
For primes $p$, the closure $\\operatorname{cl}_X(\\{p\\}) = M_p$ (Lemma 0.4).
For any $n > 1$, the closure $\\operatorname{cl}_X(\\{n\\}) = \\bigcap_{p|n} M_p$
(Theorem 0.5). Also establishes that $X_1$ is dense in $X$.
"""
from gaia.lang import claim, deduction

from .motivation import (
    s_base_and_topology,
    s_coprimality_set,
    s_positive_integers,
    s_primes_and_multiples,
    s_subspace,
    sigma_n_infinite,
    thm_base,
)

# ── Lemma 0.4 ─────────────────────────────────────────────────────────

lem_closure_prime = claim(
    "If $p$ is a prime number, then $\\operatorname{cl}_X(\\{p\\}) = M_p$ "
    "in the topological space $X = (\\mathbb{N}, \\tau)$, where $M_p$ is the "
    "set of all positive multiples of $p$ and $\\operatorname{cl}_X$ denotes "
    "closure in $X$.\n\n"
    "**Proof sketch:** ($\\subseteq$) If $x \\in \\operatorname{cl}_X(\\{p\\})$ and "
    "$x \\notin M_p$, then $\\gcd(x, p) = 1$, so $x \\in \\sigma_p$. But then "
    "$p \\in \\sigma_p$ would require $\\gcd(p, p) = 1$, a contradiction since "
    "$\\gcd(p, p) = p \\geq 2$. ($\\supseteq$) If $x = np \\in M_p$ and "
    "$\\sigma_k$ is any basic open set containing $x$, then $\\gcd(np, k) = 1$ "
    "implies $\\gcd(p, k) = 1$, so $p \\in \\sigma_k$. Hence $x \\in \\operatorname{cl}_X(\\{p\\})$.",
    title="Lemma 0.4: cl_X({p}) = M_p",
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
    source="arXiv:2402.03356, Lemma 0.4",
)

deduction(
    [thm_base],
    lem_closure_prime,
    reason=(
        "The proof uses that $\\beta$ is a base for $\\tau$ (@thm_base), so the "
        "basic open sets $\\sigma_k$ determine closure in $X$. "
        "($\\subseteq$) Suppose $x \\in \\operatorname{cl}_X(\\{p\\})$ but $x \\notin M_p$. "
        "Then $\\gcd(x, p) = 1$, so $x \\in \\sigma_p$. Since $x$ is in the closure of $\\{p\\}$, "
        "every open set containing $x$ must contain $p$, so $p \\in \\sigma_p$. But "
        "$\\gcd(p, p) = p \\neq 1$, contradiction. "
        "($\\supseteq$) If $x = np \\in M_p$ and $x \\in \\sigma_k$, then $\\gcd(np, k) = 1$, "
        "which forces $\\gcd(p, k) = 1$, so $p \\in \\sigma_k$. Every basic open neighborhood "
        "of $x$ contains $p$, hence $x \\in \\operatorname{cl}_X(\\{p\\})$."
    ),
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
)

# ── Theorem 0.5 ───────────────────────────────────────────────────────

thm_closure_n = claim(
    "For every integer $n > 1$, "
    "$\\operatorname{cl}_X(\\{n\\}) = \\bigcap_{p \\mid n} M_p$ "
    "in the topological space $X = (\\mathbb{N}, \\tau)$, where the intersection "
    "ranges over all prime divisors $p$ of $n$.",
    title="Theorem 0.5: cl_X({n}) = intersection of M_p over prime divisors of n",
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
    source="arXiv:2402.03356, Theorem 0.5",
)

deduction(
    [lem_closure_prime],
    thm_closure_n,
    reason=(
        "($\\supseteq$) Take $x \\in \\bigcap_{p|n} M_p$. By @lem_closure_prime, "
        "$x \\in \\operatorname{cl}_X(\\{p\\})$ for every prime $p | n$. So for every "
        "$\\sigma_k \\ni x$, we have $p \\in \\sigma_k$ for all $p | n$, meaning "
        "$\\gcd(p, k) = 1$ for all $p | n$, hence $\\gcd(n, k) = 1$, thus $n \\in \\sigma_k$. "
        "Therefore $x \\in \\operatorname{cl}_X(\\{n\\})$. "
        "($\\subseteq$) Take $x \\in \\operatorname{cl}_X(\\{n\\})$ and $\\sigma_k \\ni x$. "
        "Then $n \\in \\sigma_k$, so $\\gcd(n, k) = 1$, which forces $\\gcd(p, k) = 1$ "
        "for every $p | n$, hence $p \\in \\sigma_k$. By @lem_closure_prime, "
        "$x \\in \\bigcap_{p|n} M_p$."
    ),
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
)

# ── Remark 0.6 ────────────────────────────────────────────────────────

remark_closure_1 = claim(
    "$\\operatorname{cl}_X(\\{1\\}) = \\mathbb{N}$, since $\\sigma_1 = \\mathbb{N}$ "
    "implies that 1 belongs to every basic open set, so every point of "
    "$\\mathbb{N}$ is in the closure of $\\{1\\}$. Moreover, for every integer "
    "$n > 1$, $1 \\notin \\operatorname{cl}_X(\\{n\\})$, because $1 \\in \\sigma_n$ "
    "(since $\\gcd(1, n) = 1$) while $n \\notin \\sigma_n$ "
    "(since $\\gcd(n, n) = n > 1$), so $\\sigma_n$ is an open neighborhood of 1 "
    "that does not contain $n$.",
    title="Remark 0.6: cl_X({1}) = N and 1 not in cl_X({n})",
    background=[s_coprimality_set, s_base_and_topology, s_positive_integers],
    source="arXiv:2402.03356, Remark 0.6",
)

deduction(
    [thm_base],
    remark_closure_1,
    reason=(
        "Since $\\beta$ is a base for $\\tau$ (@thm_base), closure is determined by "
        "the basic open sets $\\sigma_n$. For $\\{1\\}$: since $\\gcd(1, n) = 1$ for all $n$, "
        "we have $1 \\in \\sigma_n$ for all $n$, so $\\sigma_1 = \\mathbb{N}$ and every "
        "basic open set containing any point $m$ also contains $1$ (because "
        "$m \\in \\sigma_k \\Rightarrow 1 \\in \\sigma_k$). Hence "
        "$\\operatorname{cl}_X(\\{1\\}) = \\mathbb{N}$. "
        "For $n > 1$: $1 \\in \\sigma_n$ but $n \\notin \\sigma_n$ (since $\\gcd(n,n)=n>1$), "
        "so $\\sigma_n$ separates 1 from $n$, giving $1 \\notin \\operatorname{cl}_X(\\{n\\})$."
    ),
    background=[s_coprimality_set, s_base_and_topology, s_positive_integers],
)

# ── X₁ is dense in X (used in Lemma 0.8) ─────────────────────────────

x1_dense_in_x = claim(
    "The subspace $X_1 = (\\mathbb{N} \\setminus \\{1\\}, \\tau_1)$ is dense in "
    "$X = (\\mathbb{N}, \\tau)$, i.e., "
    "$\\operatorname{cl}_X(\\mathbb{N} \\setminus \\{1\\}) = \\mathbb{N}$. "
    "This holds because every non-empty basic open set $\\sigma_n$ is infinite "
    "(hence contains elements $> 1$), so $\\sigma_n \\cap (\\mathbb{N} \\setminus \\{1\\}) \\neq \\emptyset$.",
    title="X_1 is dense in X",
    background=[s_base_and_topology, s_subspace],
)

deduction(
    [sigma_n_infinite],
    x1_dense_in_x,
    reason=(
        "By @sigma_n_infinite, every $\\sigma_n$ is infinite and hence contains "
        "elements greater than 1. Therefore every non-empty basic open set in $\\tau$ "
        "has non-empty intersection with $\\mathbb{N} \\setminus \\{1\\} = N_1$. "
        "This means $N_1$ meets every open set, so $\\operatorname{cl}_X(N_1) = \\mathbb{N}$, "
        "i.e., $X_1$ is dense in $X$."
    ),
    background=[s_base_and_topology, s_subspace],
)
