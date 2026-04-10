"""Density and Infinitude of Primes

Establishes the equivalence between the density of $P$ in $X$ and the infinitude
of primes (Theorem 0.7), reduces the density question to the subspace $X_1$
(Lemma 0.8), proves $P$ is dense in $X_1$ (Theorem 0.9), and concludes the
infinitude of primes (Theorem 0.13) and a generalization to subsets of primes
(Theorem 0.14).
"""
from gaia.lang import claim, deduction

from .motivation import (
    closure_union_containment,
    density_transitivity,
    fundamental_theorem_arithmetic,
    s_base_and_topology,
    s_coprimality_set,
    s_positive_integers,
    s_primes_and_multiples,
    s_subspace,
    thm_base,
)
from .closure import (
    lem_closure_prime,
    x1_dense_in_x,
)

# ── Theorem 0.7 ───────────────────────────────────────────────────────

thm_density_iff_infinite = claim(
    "$\\#P = \\aleph_0$ if and only if $P$ is dense in $X = (\\mathbb{N}, \\tau)$, "
    "where $P$ is the set of prime numbers and $\\#P$ denotes its cardinality.\n\n"
    "($\\Rightarrow$) If there are infinitely many primes, then for any $n > 1$, "
    "there exists a prime $p > n$, and $\\gcd(n, p) = 1$ implies $p \\in \\sigma_n \\cap P$. "
    "Since $\\sigma_1 = \\mathbb{N} \\supseteq P$, every basic open set meets $P$.\n\n"
    "($\\Leftarrow$) If $P$ is dense, let $\\{p_1, \\ldots, p_k\\}$ be any finite "
    "collection of primes and set $x = p_1 \\cdots p_k$. The basic open set $\\sigma_x$ "
    "contains no $p_i$ (since $\\gcd(p_i, x) = p_i \\neq 1$), but density forces "
    "$\\sigma_x \\cap P \\neq \\emptyset$, producing a prime $q \\notin \\{p_1, \\ldots, p_k\\}$. "
    "Hence $P$ is infinite.",
    title="Theorem 0.7: Infinitude of P iff P is dense in X",
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
    source="arXiv:2402.03356, Theorem 0.7",
)

deduction(
    [thm_base],
    thm_density_iff_infinite,
    reason=(
        "Since $\\beta$ is a base for $\\tau$ (@thm_base), density of $P$ in $X$ is "
        "equivalent to $P \\cap \\sigma_n \\neq \\emptyset$ for every $\\sigma_n \\in \\beta$. "
        "($\\Rightarrow$) If $P$ is infinite, for any $n > 1$ pick a prime $p > n$; then "
        "$\\gcd(n, p) = 1$ so $p \\in \\sigma_n \\cap P$. For $n = 1$, $\\sigma_1 = \\mathbb{N} \\supseteq P$. "
        "($\\Leftarrow$) Given a finite set of primes $\\{p_1, \\ldots, p_k\\}$, set "
        "$x = p_1 \\cdots p_k$. None of the $p_i$ lie in $\\sigma_x$ (since "
        "$\\gcd(p_i, x) = p_i \\neq 1$). But $P$ is dense, so $\\exists q \\in P \\cap \\sigma_x$ "
        "with $q \\neq p_i$ for all $i$. Hence $P$ has more than $k$ elements for any $k$."
    ),
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
)

# ── Lemma 0.8 ─────────────────────────────────────────────────────────

lem_density_equivalence = claim(
    "$P$ is dense in $X_1 = (\\mathbb{N} \\setminus \\{1\\}, \\tau_1)$ "
    "if and only if $P$ is dense in $X = (\\mathbb{N}, \\tau)$.\n\n"
    "($\\Leftarrow$) If $P$ is dense in $X$, it is clearly dense in any subspace.\n\n"
    "($\\Rightarrow$) $X_1$ is dense in $X$ (every basic open set $\\sigma_n$ "
    "is infinite, hence meets $\\mathbb{N} \\setminus \\{1\\}$). So by transitivity "
    "of density, $P$ dense in $X_1$ and $X_1$ dense in $X$ imply $P$ dense in $X$.",
    title="Lemma 0.8: P dense in X_1 iff P dense in X",
    background=[s_base_and_topology, s_subspace, s_primes_and_multiples],
    source="arXiv:2402.03356, Lemma 0.8",
)

deduction(
    [x1_dense_in_x, density_transitivity],
    lem_density_equivalence,
    reason=(
        "($\\Leftarrow$) Trivial: density in the ambient space implies density in a subspace. "
        "($\\Rightarrow$) @x1_dense_in_x establishes that $X_1$ is dense in $X$. "
        "If $P$ is dense in $X_1$, then by @density_transitivity "
        "(density is transitive), $P$ is dense in $X$."
    ),
    background=[s_base_and_topology, s_subspace, s_primes_and_multiples],
)

# ── Theorem 0.9 ───────────────────────────────────────────────────────

thm_p_dense_x1 = claim(
    "$P$ is dense in $X_1 = (\\mathbb{N} \\setminus \\{1\\}, \\tau_1)$, i.e., "
    "$\\operatorname{cl}_{X_1}(P) = N_1$.\n\n"
    "The proof combines three ingredients:\n\n"
    "**(0.10)** By a standard topological fact, "
    "$\\bigcup_{p \\in P} \\operatorname{cl}_{X_1}(\\{p\\}) "
    "\\subseteq \\operatorname{cl}_{X_1}(P) \\subseteq N_1$.\n\n"
    "**(0.11)** By Lemma 0.4, $\\operatorname{cl}_X(\\{p\\}) = M_p$ for each prime $p$, "
    "so $\\bigcup_{p \\in P} \\operatorname{cl}_{X_1}(\\{p\\}) "
    "= \\bigcup_{p \\in P} (M_p \\cap N_1) = \\bigcup_{p \\in P} M_p$ "
    "(since $M_p \\subseteq N_1$ for all primes $p \\geq 2$).\n\n"
    "**(0.12)** By the Fundamental Theorem of Arithmetic, "
    "$\\bigcup_{p \\in P} M_p = N_1$.\n\n"
    "Chaining: $N_1 = \\bigcup_{p \\in P} M_p "
    "= \\bigcup_{p \\in P} \\operatorname{cl}_{X_1}(\\{p\\}) "
    "\\subseteq \\operatorname{cl}_{X_1}(P) \\subseteq N_1$, "
    "hence $\\operatorname{cl}_{X_1}(P) = N_1$.",
    title="Theorem 0.9: P is dense in X_1",
    background=[s_base_and_topology, s_subspace, s_primes_and_multiples, s_positive_integers],
    source="arXiv:2402.03356, Theorem 0.9",
)

deduction(
    [lem_closure_prime, fundamental_theorem_arithmetic, closure_union_containment],
    thm_p_dense_x1,
    reason=(
        "Step 1 (eq. 0.10): By @closure_union_containment (union of closures $\\subseteq$ "
        "closure of union), $\\bigcup_{p \\in P} \\operatorname{cl}_{X_1}(\\{p\\}) "
        "\\subseteq \\operatorname{cl}_{X_1}(P) \\subseteq N_1$. "
        "Step 2 (eq. 0.11): By @lem_closure_prime, $\\operatorname{cl}_X(\\{p\\}) = M_p$ "
        "for each prime $p$, so $\\operatorname{cl}_{X_1}(\\{p\\}) = M_p \\cap N_1 = M_p$ "
        "(since the smallest element of $M_p$ is $p \\geq 2 \\in N_1$). Hence "
        "$\\bigcup_{p \\in P} \\operatorname{cl}_{X_1}(\\{p\\}) = \\bigcup_{p \\in P} M_p$. "
        "Step 3 (eq. 0.12): By @fundamental_theorem_arithmetic, every integer $> 1$ has a "
        "prime divisor, so $\\bigcup_{p \\in P} M_p = N_1$. "
        "Combining: $N_1 = \\bigcup M_p = \\bigcup \\operatorname{cl}_{X_1}(\\{p\\}) "
        "\\subseteq \\operatorname{cl}_{X_1}(P) \\subseteq N_1$, hence $\\operatorname{cl}_{X_1}(P) = N_1$."
    ),
    background=[s_base_and_topology, s_subspace, s_primes_and_multiples, s_positive_integers],
)

# ── Theorem 0.13 (Main Result) ────────────────────────────────────────

thm_infinitude_primes = claim(
    "There are infinitely many prime numbers, i.e., $\\#P = \\aleph_0$.",
    title="Theorem 0.13: Infinitude of prime numbers",
    background=[s_primes_and_multiples],
    source="arXiv:2402.03356, Theorem 0.13",
)

deduction(
    [thm_density_iff_infinite, lem_density_equivalence, thm_p_dense_x1],
    thm_infinitude_primes,
    reason=(
        "By @thm_p_dense_x1, $P$ is dense in $X_1$. "
        "By @lem_density_equivalence, $P$ dense in $X_1$ implies $P$ dense in $X$. "
        "By the ($\\Leftarrow$) direction of @thm_density_iff_infinite, "
        "$P$ dense in $X$ implies $\\#P = \\aleph_0$. "
        "Therefore there are infinitely many prime numbers."
    ),
)

# ── Theorem 0.14 (Generalization) ─────────────────────────────────────

thm_subset_dense_iff_infinite = claim(
    "Let $A \\subseteq P$ be a non-empty subset of primes. Then $A$ is dense in "
    "$X = (\\mathbb{N}, \\tau)$ if and only if $\\#A = \\aleph_0$. "
    "The proof follows the same argument as Theorem 0.7 with $P$ replaced by $A$:\n\n"
    "($\\Rightarrow$) If $\\#A = \\aleph_0$, for any $n > 1$ there exists $p \\in A$ "
    "with $p > n$, so $p \\in \\sigma_n \\cap A$.\n\n"
    "($\\Leftarrow$) If $A$ is dense, for any finite subset $\\{p_1, \\ldots, p_k\\} \\subseteq A$, "
    "the set $\\sigma_{p_1 \\cdots p_k} \\cap A$ is non-empty and contains a prime "
    "not in $\\{p_1, \\ldots, p_k\\}$.",
    title="Theorem 0.14: Subset of primes dense iff infinite",
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
    source="arXiv:2402.03356, Theorem 0.14",
)

deduction(
    [thm_base],
    thm_subset_dense_iff_infinite,
    reason=(
        "The argument is identical to Theorem 0.7, replacing $P$ with an arbitrary "
        "non-empty $A \\subseteq P$. Since $\\beta$ is a base for $\\tau$ (@thm_base): "
        "($\\Rightarrow$) If $A$ is infinite, for any $n > 1$, pick $p \\in A$ with $p > n$; "
        "then $\\gcd(n, p) = 1$ so $p \\in \\sigma_n \\cap A$, proving density. "
        "($\\Leftarrow$) If $A$ is dense, for any finite $\\{p_1, \\ldots, p_k\\} \\subseteq A$, "
        "set $x = p_1 \\cdots p_k$; no $p_i$ lies in $\\sigma_x$, but density gives "
        "$q \\in A \\cap \\sigma_x$ distinct from all $p_i$, proving $A$ is infinite."
    ),
    background=[s_coprimality_set, s_base_and_topology, s_primes_and_multiples, s_positive_integers],
)
