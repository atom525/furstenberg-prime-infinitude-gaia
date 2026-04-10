"""Self-review sidecar for the prime-topo-gaia knowledge package.

所有 strategies 均为 deduction（确定性），不需要 conditional_probability。
为 independent claims（leaf）提供 prior 反映数学确定性；
为 derived claims 提供 prior 反映证明草图的完整性和严密性，
用于对抗 BP 中 IMPLICATION modus tollens 的反向拉低效应。
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
    thm_base,
)
from ..closure import (
    lem_closure_prime,
    thm_closure_n,
    remark_closure_1,
    x1_dense_in_x,
)
from ..density import (
    thm_density_iff_infinite,
    lem_density_equivalence,
    thm_p_dense_x1,
    thm_infinitude_primes,
    thm_subset_dense_iff_infinite,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Independent premises (leaf claims, 数学确定性) ──────────────

        review_claim(
            gcd_multiplicativity,
            prior=0.99,
            judgment="supporting",
            justification=(
                "基础数论事实: gcd(x,n)=1 且 gcd(x,m)=1 当且仅当 gcd(x,nm)=1。"
                "直接由唯一素因子分解和 gcd 的乘性得出。"
                "教科书结果 (Niven-Zuckerman-Montgomery, Theorem 1.9)。"
            ),
        ),
        review_claim(
            fundamental_theorem_arithmetic,
            prior=0.99,
            judgment="supporting",
            justification=(
                "算术基本定理: 每个大于 1 的整数都有唯一的素因子分解。"
                "自 Euclid 以来严格建立。推论 ∪M_p = N\\{1} 是直接的。"
            ),
        ),
        review_claim(
            closure_union_containment,
            prior=0.99,
            judgment="supporting",
            justification=(
                "标准点集拓扑定理: 闭包的并包含在并的闭包中。"
                "见任何拓扑学导论教材 (Munkres, Theorem 17.6)。"
            ),
        ),
        review_claim(
            density_transitivity,
            prior=0.99,
            judgment="supporting",
            justification=(
                "标准拓扑事实: 稠密性具有传递性。"
                "若 A 在 B 中稠密、B 在 C 中稠密，则 A 在 C 中稠密。"
                "直接由定义得出。"
            ),
        ),
        review_claim(
            sigma_n_infinite,
            prior=0.97,
            judgment="supporting",
            justification=(
                "对 n > 1，σ_n 包含与 n 互素的所有等差数列 m, m+n, m+2n, ...，"
                "每条等差数列都是无限的。对 n=1, σ_1 = N 显然。"
                "需要简短论证，故 0.97 而非 0.99。"
            ),
        ),

        # ── Derived claims (有完整证明草图，高置信度) ───────────────────

        review_claim(
            thm_base,
            prior=0.98,
            judgment="supporting",
            justification=(
                "Theorem 0.1: β 是 N 上拓扑基。"
                "证明简洁完整: (1) ∪σ_n ⊇ σ_1 = N, "
                "(2) σ_n ∩ σ_m = σ_{nm} ∈ β 由 gcd 乘性直接得出。"
                "论文 arXiv:2402.03356 正式证明。"
            ),
        ),
        review_claim(
            lem_closure_prime,
            prior=0.97,
            judgment="supporting",
            justification=(
                "Lemma 0.4: cl_X({p}) = M_p。"
                "两方向证明均完整: "
                "(⊆) 反证法利用 gcd(p,p)=p≠1, "
                "(⊇) 利用 gcd(np,k)=1 → gcd(p,k)=1。"
                "论文 arXiv:2402.03356 正式证明。"
            ),
        ),
        review_claim(
            thm_closure_n,
            prior=0.96,
            judgment="supporting",
            justification=(
                "Theorem 0.5: cl_X({n}) = ∩_{p|n} M_p。"
                "推广 Lemma 0.4 到一般正整数，"
                "两方向证明均完整且严密。"
            ),
        ),
        review_claim(
            remark_closure_1,
            prior=0.98,
            judgment="supporting",
            justification=(
                "Remark 0.6: cl_X({1}) = N 且 1 ∉ cl_X({n}) 对 n>1。"
                "直接计算: gcd(1,n)=1 对所有 n, "
                "而 gcd(n,n)=n>1 给出分离。极简证明。"
            ),
        ),
        review_claim(
            x1_dense_in_x,
            prior=0.97,
            judgment="supporting",
            justification=(
                "X_1 在 X 中稠密: 每个 σ_n 无限（由 sigma_n_infinite），"
                "故必含大于 1 的元素。简洁直接。"
            ),
        ),
        review_claim(
            thm_density_iff_infinite,
            prior=0.97,
            judgment="supporting",
            justification=(
                "Theorem 0.7: #P = ℵ₀ ↔ P 在 X 中稠密。"
                "两方向证明完整: "
                "(⇒) 取 p>n 则 p∈σ_n∩P, "
                "(⇐) 反证法构造 x=p₁···pₖ 排除已知素数。"
            ),
        ),
        review_claim(
            lem_density_equivalence,
            prior=0.97,
            judgment="supporting",
            justification=(
                "Lemma 0.8: P 在 X_1 中稠密 ↔ P 在 X 中稠密。"
                "(⇐) 平凡; (⇒) 由 X_1 稠密性和传递性。"
                "逻辑链条完整。"
            ),
        ),
        review_claim(
            thm_p_dense_x1,
            prior=0.97,
            judgment="supporting",
            justification=(
                "Theorem 0.9: P 在 X_1 中稠密。"
                "三步论证: (0.10) 闭包并的包含, "
                "(0.11) cl_X({p})=M_p 由 Lemma 0.4, "
                "(0.12) ∪M_p=N₁ 由算术基本定理。"
                "每步均有前序定理支撑。"
            ),
        ),
        review_claim(
            thm_infinitude_primes,
            prior=0.98,
            judgment="supporting",
            justification=(
                "Theorem 0.13 (主定理): 素数有无限多个。"
                "三步链: P 在 X_1 中稠密 (Thm 0.9) "
                "→ P 在 X 中稠密 (Lem 0.8) "
                "→ P 无限 (Thm 0.7)。"
                "每步已独立建立，推理严密。"
            ),
        ),
        review_claim(
            thm_subset_dense_iff_infinite,
            prior=0.96,
            judgment="supporting",
            justification=(
                "Theorem 0.14: 素数子集 A 在 X 中稠密 ↔ A 无限。"
                "论证与 Theorem 0.7 完全平行，用 A 替换 P。"
                "推广自然，稍低 prior 反映额外的一般化步骤。"
            ),
        ),

        # ── Orphaned claims (论文中提及但不在证明链中) ──────────────────

        review_claim(
            tau_coarser_golomb,
            prior=0.90,
            judgment="supporting",
            justification=(
                "Remark 0.2 中陈述, 归因于参考文献 [2]。"
                "τ 严格粗于 Golomb 拓扑, 因 Golomb 基更精细。"
            ),
        ),
        review_claim(
            x_not_t0,
            prior=0.90,
            judgment="supporting",
            justification=(
                "论文中无证明地陈述, 归因于参考文献 [2]。"
                "合理: 例如 2 和 3 属于完全相同的 σ_n 集合（n 不被 2 或 3 整除时）。"
            ),
        ),
        review_claim(
            x_hyperconnected,
            prior=0.90,
            judgment="supporting",
            justification=(
                "论文中无证明地陈述, 归因于参考文献 [2]。"
                "超连通性: 任意两个非空开集交非空。"
                "σ_n 无限且 N 可数, 交集非空是合理的。"
            ),
        ),
        review_claim(
            x_ultraconnected,
            prior=0.90,
            judgment="supporting",
            justification=(
                "论文中无证明地陈述, 归因于参考文献 [2]。"
                "超连通性: 任意两个非空闭集交非空。"
                "与 X 的非 T_0 性质一致。"
            ),
        ),
    ],
)
