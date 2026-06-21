# Math Syntax Guide

FreateOJ uses **MathJax 3.2.0** for rendering mathematical expressions. This guide covers the syntax conventions used across the platform.

## Quick Reference

| Type | Syntax | Example | Renders |
|------|--------|---------|---------|
| Inline | `$expr$` | `$x^2$` | $x^2$ |
| Display | `$$expr$$` | `$$\sum_{i=1}^{n} i$$` | $$\sum_{i=1}^{n} i$$ |

## Inline Math

Use single dollar signs `$` to wrap inline mathematical expressions:

```markdown
The value of $\pi$ is approximately 3.14159.
```

Renders as: The value of $\pi$ is approximately 3.14159.

### Common Examples

| Expression | Syntax |
|-----------|--------|
| Superscript | `$x^2$` |
| Subscript | `$a_i$` |
| Fraction | `$\frac{a}{b}$` |
| Square root | `$\sqrt{n}$` |
| Summation | `$\sum_{i=1}^{n} a_i$` |
| Integral | `$\int_0^1 f(x) \, dx$` |
| Limit | `$\lim_{n \to \infty} a_n$` |
| Binomial | `$\binom{n}{k}$` |

## Display Math

Use double dollar signs `$$` for centered, display-style equations:

```markdown
$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$
```

### Piecewise Functions

```markdown
$$f(x) = \begin{cases} 1 & \text{if } x \ge 0 \\\\ -1 & \text{if } x < 0 \end{cases}$$
```

## Common LaTeX Commands

### Greek Letters

| Letter | Syntax | Letter | Syntax |
|--------|--------|--------|--------|
| α | `$\alpha$` | Α | `$\Alpha$` |
| β | `$\beta$` | Β | `$\Beta$` |
| γ | `$\gamma$` | Γ | `$\Gamma$` |
| δ | `$\delta$` | Δ | `$\Delta$` |
| ε | `$\epsilon$` | Ε | `$\Epsilon$` |
| θ | `$\theta$` | Θ | `$\Theta$` |
| λ | `$\lambda$` | Λ | `$\Lambda$` |
| μ | `$\mu$` | Μ | `$\Mu$` |
| π | `$\pi$` | Π | `$\Pi$` |
| σ | `$\sigma$` | Σ | `$\Sigma$` |
| φ | `$\phi$` | Φ | `$\Phi$` |
| ω | `$\omega$` | Ω | `$\Omega$` |

### Operators

| Operation | Syntax |
|-----------|--------|
| Modulo | `$a \bmod b$` |
| Logarithm | `$\log n$` |
| Natural log | `$\ln n$` |
| Greatest common divisor | `$\gcd(a, b)$` |
| Maximum | `$\max(a, b)$` |
| Minimum | `$\min(a, b)$` |
| Absolute value | `$\|x\|$` |
| Floor | `$\lfloor x \rfloor$` |
| Ceiling | `$\lceil x \rceil$` |

### Sets and Logic

| Symbol | Syntax |
|--------|--------|
| Set | `$\{1, 2, 3\}$` |
| Union | `$A \cup B$` |
| Intersection | `$A \cap B$` |
| Subset | `$A \subseteq B$` |
| Element of | `$x \in A$` |
| For all | `$\forall$` |
| Exists | `$\exists$` |
| Therefore | `$\therefore$` |
| Because | `$\because$` |

### Big Operators

| Symbol | Syntax |
|--------|--------|
| Sum | `$\sum_{i=1}^{n} a_i$` |
| Product | `$\prod_{i=1}^{n} a_i$` |
| Union | `$\bigcup_{i=1}^{n} A_i$` |
| Intersection | `$\bigcap_{i=1}^{n} A_i$` |

## Complexity Notation

```markdown
The time complexity is $\mathcal{O}(N \log N)$.
```

Renders as: The time complexity is $\mathcal{O}(N \log N)$.

## Colored Math

FreateOJ supports the `\color` command:

```markdown
$\color{red}x + \color{blue}y$
```

## Tips

1. **Escape dollar signs**: Use `\$` for a literal dollar sign outside math mode
2. **Spacing**: Use `\,`, `\;`, `\:` for different spacing widths
3. **Newlines in display math**: Use `\\\\` for line breaks
4. **Text in math**: Use `\text{...}` for text within expressions
5. **Operators**: Use `\operatorname{...}` for custom operators
