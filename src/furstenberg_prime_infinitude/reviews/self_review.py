"""Self-review sidecar for the prime-topo-gaia knowledge package.

All strategies are deduction (deterministic), so no conditional_probability
parameters are needed. Only leaf claims and orphaned claims require priors.
"""
from gaia.review import ReviewBundle, review_claim

from ..motivation import (
    gcd_multiplicativity,
    fundamental_theorem_arithmetic,
    closure_union_containment,
    density_transitivity,
    sigma_n_infinite,
    tau_coarser_golomb,
    x_not_t0,
    x_hyperconnected,
    x_ultraconnected,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Independent premises (leaf claims used in proof chain) ──────

        review_claim(
            gcd_multiplicativity,
            prior=0.99,
            judgment="supporting",
            justification=(
                "Foundational number-theoretic fact: gcd(x,n)=1 and gcd(x,m)=1 iff "
                "gcd(x,nm)=1. Follows directly from unique prime factorization and the "
                "multiplicativity of gcd. Textbook result (Niven-Zuckerman-Montgomery, "
                "Theorem 1.9). Prior 0.99 reflects mathematical certainty."
            ),
        ),
        review_claim(
            fundamental_theorem_arithmetic,
            prior=0.99,
            judgment="supporting",
            justification=(
                "The Fundamental Theorem of Arithmetic: every integer > 1 has a unique "
                "prime factorization. Rigorously established since Euclid. The consequence "
                "that union of M_p over all primes equals N\\{1} is immediate. "
                "Prior 0.99 reflects mathematical certainty."
            ),
        ),
        review_claim(
            closure_union_containment,
            prior=0.99,
            judgment="supporting",
            justification=(
                "Standard point-set topology theorem: the union of closures is contained "
                "in the closure of the union. Proved in every introductory topology "
                "textbook (Munkres, Theorem 17.6). Prior 0.99 reflects mathematical certainty."
            ),
        ),
        review_claim(
            density_transitivity,
            prior=0.99,
            judgment="supporting",
            justification=(
                "Standard topological fact: density is transitive. If A is dense in B "
                "and B is dense in C, then A is dense in C. Follows directly from the "
                "definition. Prior 0.99 reflects mathematical certainty."
            ),
        ),
        review_claim(
            sigma_n_infinite,
            prior=0.97,
            judgment="supporting",
            justification=(
                "For n > 1, sigma_n contains all integers in arithmetic progressions "
                "m, m+n, m+2n, ... for each m coprime to n, each infinite. "
                "For n = 1, sigma_1 = N trivially. Requires a brief argument, "
                "hence 0.97 rather than 0.99."
            ),
        ),

        # ── Orphaned claims (not in proof chain, but in paper) ─────────

        review_claim(
            tau_coarser_golomb,
            prior=0.90,
            judgment="supporting",
            justification=(
                "Stated in the paper (Remark 0.2) and attributed to reference [2]. "
                "The claim that tau is strictly coarser than Golomb's topology follows "
                "from the fact that Golomb's base (arithmetic progressions {a+nd}) is "
                "finer-grained than beta = {sigma_n}. Each sigma_n can be written as a "
                "union of Golomb basic sets, but not vice versa."
            ),
        ),
        review_claim(
            x_not_t0,
            prior=0.90,
            judgment="supporting",
            justification=(
                "Stated without proof in the paper, attributed to reference [2]. "
                "Plausible: for example, 2 and 3 belong to exactly the same sigma_n sets "
                "when n is not divisible by 2 or 3, suggesting T_0 failure. "
                "Prior reflects trust in the referenced source."
            ),
        ),
        review_claim(
            x_hyperconnected,
            prior=0.90,
            judgment="supporting",
            justification=(
                "Stated without proof, attributed to reference [2]. Hyperconnectedness "
                "means any two non-empty open sets intersect. Since sigma_n sets are "
                "infinite and N is countable, intersections are plausibly non-empty. "
                "Prior reflects trust in the referenced source."
            ),
        ),
        review_claim(
            x_ultraconnected,
            prior=0.90,
            judgment="supporting",
            justification=(
                "Stated without proof, attributed to reference [2]. Ultraconnectedness "
                "means any two non-empty closed sets intersect. This is a strong "
                "connectivity property consistent with the non-T_0 nature of X. "
                "Prior reflects trust in the referenced source."
            ),
        ),
    ],
)
