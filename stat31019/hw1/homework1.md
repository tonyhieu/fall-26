# STAT 31019 Homework 1

AI Usage Disclosure: LLMs were used in order to help when stuck on a problem and to reformat this file from Markdown to LaTeX on Overleaf. Answers were NOT copied verbatim.

## Problem 1

### (a)

$$
\begin{align}
  \theta(1) &= \theta(0) + \int_0^1 \theta'(t)\, dt && \text{(FTC)}\\
  f(x + s) &= f(x) + \int_0^1 \nabla f(x+ts)^T s  \, dt && \text{(Chain rule)} \\
  f(x + s) - f(x) &= \int_0^1 \nabla f(x+ts)^T s  \, dt \\
  f(x + s) - f(x) - \nabla f(x)^Ts &= \int_0^1 \nabla f(x+ts)^T s \, dt - \nabla f(x)^Ts\\
  &= \int_0^1 (\nabla f(x+ts) - \nabla f(x))^Ts \, dt \\
  \vert f(x + s) - f(x) - \nabla f(x)^Ts \vert &= \left\vert \int_0^1 (\nabla f(x+ts) - \nabla f(x))^Ts \, dt \right\vert \\
  &\leq \int_0^1 \vert (\nabla f(x+ts) - \nabla f(x))^Ts \vert \, dt\\
  &\leq \int_0^1 \lVert \nabla f(x+ts) - \nabla f(x)\rVert \lVert s\rVert \, dt && \text{(Cauchy-Schwarz inequality)}\\
  &\leq \int_0^1 L\lVert x+ts - x\rVert \lVert s\rVert \, dt && \text{($L$-Lipschitz definition)}\\
  &= \int_0^1 L\lVert ts \rVert \lVert s\rVert \, dt \\
  &= \int_0^1 Lt\lVert s \rVert^2 \, dt && \text{($t\geq 0$ so it can be pulled out)}\\
  &= L\lVert s \rVert^2 \int_0^1 t\, dt \\
  &= \frac{1}{2} L\lVert s \rVert^2
\end{align}
$$

### (b)

Begin by justifying the first statement:
$$
\begin{align}
  \theta(1) &= \theta(0) + \int_0^1 \theta'(t)\, dt && \text{(FTC)} \\
  &= \theta(0) + \int_0^1 \left(\theta'(0) + \int_0^t \theta''(\alpha)\, d\alpha \right) \, dt && \text{(FTC)} \\
  &= \theta(0) + \int_0^1 \theta'(0) \, dt + \int_0^1 \int_0^t \theta''(\alpha)\, d\alpha dt \\
  &= \theta(0) + \theta'(0) + \int_0^1 \int_0^t \theta''(\alpha)\, d\alpha dt \\
\end{align}
$$

Now we can take similar steps from part (a) to simplify this:
$$
\begin{align}
  \theta(1) &= \theta(0) + \theta'(0) + \int_0^1 \int_0^t \theta''(\alpha)\, d\alpha dt \\
  f(x + s) &= f(x) + \nabla f(x)^T s + \int_0^1 \int_0^t s^T\nabla^2 f(x + \alpha s)s \, d\alpha dt && \text{(Chain rule)} \\
  f(x + s) - f(x) - \nabla f(x)^T s &= \int_0^1 \int_0^t s^T\nabla^2 f(x + \alpha s)s \, d\alpha dt \\
  f(x + s) - f(x) - \nabla f(x)^T s - \frac{1}{2}s^T\nabla^2 f(x)s &= \int_0^1 \int_0^t s^T\nabla^2 f(x + \alpha s)s \, d\alpha dt - \frac{1}{2}s^T\nabla^2 f(x)s\\
  &= \int_0^1 \int_0^t s^T\nabla^2 f(x + \alpha s)s \, d\alpha dt - \int_0^1 \int_0^t s^T\nabla^2 f(x)s \, d\alpha dt \\
  &= \int_0^1 \int_0^t \left(s^T\nabla^2 f(x + \alpha s)s - s^T\nabla^2 f(x)s\right) \, d\alpha dt \\
  &= \int_0^1 \int_0^t s^T (\nabla^2 f(x + \alpha s) - \nabla^2 f(x))s \, d\alpha dt \\
  \vert f(x + s) - f(x) - \nabla f(x)^T s - \frac{1}{2}s^T\nabla^2 f(x)s \vert &= \left\vert \int_0^1 \int_0^t s^T (\nabla^2 f(x + \alpha s) - \nabla^2 f(x))s \, d\alpha dt \right\vert \\
  &\leq \int_0^1 \int_0^t \vert s^T (\nabla^2 f(x + \alpha s) - \nabla^2 f(x))s \vert \, d\alpha dt  \\
  &\leq \int_0^1 \int_0^t \lVert s \rVert \lVert (\nabla^2 f(x + \alpha s) - \nabla^2 f(x))s \rVert \, d\alpha dt  && \text{(Cauchy-Schwarz)}\\
  &\leq \int_0^1 \int_0^t \lVert s \rVert \lVert \nabla^2 f(x + \alpha s) - \nabla^2 f(x) \rVert_{\text{op}} \lVert s \rVert \, d\alpha dt  && \text{($\left\lVert M \right\rVert_{\text{op}} = \sup \{\left\lVert Mu \right\rVert \vert \left\lVert u \right\rVert \leq 1\}$)}\\
  &= \int_0^1 \int_0^t \lVert s \rVert^2 \lVert \nabla^2 f(x + \alpha s) - \nabla^2 f(x) \rVert_{\text{op}} \, d\alpha dt \\
  &\leq \int_0^1 \int_0^t Q\lVert s \rVert^2 \lVert x + \alpha s - x \rVert \, d\alpha dt && \text{(Definition of $Q$-Lipschitz continuous Hessian)}\\
  &= Q\int_0^1 \int_0^t \lVert s \rVert^2 \lVert \alpha s \rVert \, d\alpha dt  \\
  &= Q\int_0^1 \int_0^t \alpha\lVert s \rVert^3 \, d\alpha dt && \text{($\alpha > 0$ so it can be pulled out)} \\
  &= Q\lVert s \rVert^3 \int_0^1 \int_0^t \alpha \, d\alpha dt \\
  &= \frac{1}{2}Q\lVert s \rVert^3 \int_0^1 t^2 \, dt \\
  \vert f(x + s) - f(x) - \nabla f(x)^T s - \frac{1}{2}s^T\nabla^2 f(x)s \vert &= \frac{1}{6}Q\lVert s \rVert^3
\end{align}
$$

## Problem 2

### (a)

Let $g = af + b$. The gradient of $g$ is $$\nabla g(x) = \nabla (af(x) + b) = a \nabla f(x).$$ $g^* = \min_x g(x)$ can be written in terms of $f^*$ as $$g^* = af^* + b.$$ This is possible because $a>0$, so the minimum is preserved. Let's also rewrite $g(x) - g^*$ in terms of $f$: $$g(x) - g^* = af(x) + b - af^* - b = a(f(x) - f^*).$$

Using these facts, we can manipulate the PL-inequality for $f$ to show that it holds for $g$.
$$
\begin{align}
  \mu(f(x) - f^*) &\leq \frac{1}{2}\left\lVert \nabla f(x) \right\rVert^2\\
  a\mu\cdot a(f(x) - f^*) &\leq \frac{1}{2}a^2\left\lVert \nabla f(x) \right\rVert^2\\
  a\mu(g(x) - g^*)&\leq \frac{1}{2}\left\lVert a\nabla f(x) \right\rVert^2 && \text{(Since $a>0$, it can be pulled into the norm)}\\
  a\mu(g(x) - g^*)&= \frac{1}{2}\left\lVert \nabla g(x) \right\rVert^2 
\end{align}
$$

Thus, we have shown that $g$ is $a\mu$-PL.

### (b)

Let $x = (x_1, \ldots, x_k)$ be the stacked vector in $\mathbb{R}^{\sum_{i=1}^k d_i}$ of all input vectors $x_i$. We want to show that $$(\min_i a_i\mu_i) (F(x) - F^*) \leq \frac{1}{2}\left\lVert \nabla F(x) \right\rVert.$$

To prove this, we need to find both the gradient and minimum of $F$. Consider one $i$. Because each input vector $x_i$ is separate, the gradient of $F$ with respect to $x_i$ is $\nabla_{x_i} F(x) = \nabla (a_if_i)(x_i)$. This means that the gradient of $F$ is a stacked vector of the gradients of the summed functions: $$\nabla F(x) = (\nabla (a_1f_1)(x_1), \ldots, \nabla (a_kf_k)(x_k)).$$ Taking the squared Euclidean norm of this gradient thus gives $$\left\lVert \nabla F(x) \right\rVert^2 = \sum_{i=1}^k \left\lVert \nabla (a_if_i)(x_i) \right\rVert^2.$$

Next, let's consider the minimum. Because the variables are separate, each individual function can minimize themselves freely without affecting other functions, and the minimizer exists because each function satisfies PL. Thus, $$F^* = \sum_{i=1}^k (a_if_i)^*.$$

We know that, because each function $f_i$ is $\mu_i$-PL, each $(a_if_i)$ is $a_i\mu_i$-PL by part (a). Therefore, each function satisfies $$a_i\mu_i(a_if_i(x_i) - a_if_i^*) \leq \frac{1}{2}\left\lVert \nabla (a_if_i)(x_i) \right\rVert^2.$$ Let $\mu^* = \min_i a_i\mu_i$. Because $\mu^* \leq a_i\mu_i \, \forall i$ by construction and $a_if_i(x_i) - a_if^*$ is nonnegative, each function also satisfies $$\mu^*(a_if_i(x_i) - a_if_i^*) \leq \frac{1}{2}\left\lVert \nabla (a_if_i)(x_i) \right\rVert^2.$$

Adding each individual PL-inequality maintains the inequality and gives $$\mu^*\left( \sum_{i=1}^k a_if_i(x_i) - \sum_{i=1}^k a_if_i^* \right) \leq \frac{1}{2} \sum_{i=1}^k \left\lVert \nabla (a_i f_i)(x_i) \right\rVert^2.$$ Using the identities derived above for $F(x)$, $F^*$, and $\left\lVert \nabla F(x) \right\rVert^2$, we arrive at $$\mu^*\left( F(x) - F^* \right) \leq \frac{1}{2} \left\lVert \nabla F(x) \right\rVert^2$$ which proves that $F$ satisfies $(\min_i a_i\mu_i)$-PL.

### (c)

Consider the two functions $f(x,y) = \frac{1}{2}y^2$ and $g(x, y) = \frac{1}{2}(y-x^2)^2$. The minimizers of these two functions is $f^* = g^* = 0$, as they are both nonnegative. This occurs for $f$ at $y=0$ and for $g$ at $y=x^2$. First, let's show that they are both $1$-PL.

The gradient of $f$ is $\nabla f = (0, y)$. Plugging this into the PL-inequality gives $$\frac{1}{2}y^2 \leq \frac{1}{2} \left\lVert (0, y) \right\rVert^2 = \frac{1}{2}y^2$$ which is obviously true.

Let $u = y-x^2$. The gradient of $g$ is $\nabla g = (-2xu, u)$ by the chain rule. Plugging this into the PL-inequality gives $$\frac{1}{2}(y-x^2) \leq \frac{1}{2} \left\lVert (-2xu, u) \right\rVert^2 = \frac{1}{2}(4x^2u^2 + u^2) = \frac{1}{2}(4x^2 + 1)(y-x^2)^2.$$ Because $4x^2 + 1 \leq 1$, the inequality is always true.

Adding these two functions gives $$f + g = \frac{1}{2}y^2 + \frac{1}{2}(u)^2$$ and the gradient of $f+g$ is $$\nabla(f + g) = (-2xu, u + y),$$ maintaining the same $u = y-x^2$ from before. 

To show that the PL-inequality doesn't hold, consider when $y=\frac{x^2}{2}$. Note that this means $$u = \frac{x^2}{2} - x^2 = -\frac{x^2}{2}, \, u + y = \frac{1}{2}x^2 + \frac{1}{2}x^2 - x^2 = 0.$$ 

The left side becomes $$\frac{1}{2}y^2 + \frac{1}{2}u^2 = \frac{1}{2}(x^2)^2 + \frac{1}{2}(-x^2)^2 = \frac{x^4}{4}.$$ The right side becomes $$\frac{1}{2} \left\lVert \nabla (f+g) \right\rVert^2 = \frac{1}{2} \left\lVert (-x^3, 0) \right\rVert^2 = \frac{x^6}{2}.$$ 

Applying the PL-inequality gives $$\mu \cdot \frac{x^4}{4} \leq \frac{x^6}{2} \rightarrow \mu \leq 2x^2$$ for every $x \neq 0$ (as $\mu>0$). However, this inequality is provably false for a wide range of $x$ values. Consider $x = \frac{\sqrt{\mu}}{2}$ which is nonzero. This gives $$\mu \nleq \frac{\mu}{2}$$ which is always false. Thus, $f+g$ does not satisfy the PL-inequality.

This is distinct from the case in part (b), as $f$ and $g$ share variables (in this case, $x$ and $y$) as opposed to having separate variables (e.g. $x$, $y$, $w$, and $z$).

### (d)

Let us first rewrite the right hand side of the PL-inequality. Starting with the gradient, we have $$\nabla (f+g) = \nabla f + \nabla g$$ so we can expand the norm as $$\left\lVert \nabla (f+g) \right\rVert = \left\lVert \nabla f+ \nabla g \right\rVert = \left\lVert \nabla f \right\rVert^2 + \left\lVert \nabla f \right\rVert^2 + 2 \langle \nabla f, \nabla g \rangle.$$

Then, we can use the information given in the problem statement as an upper-bound for the right hand side:
$$
\begin{align}
  \frac{1}{2}\left\lVert \nabla (f+g) \right\rVert &= \frac{1}{2} \left(\left\lVert \nabla f \right\rVert^2 + \left\lVert \nabla f \right\rVert^2 + 2 \langle \nabla f, \nabla g \rangle\right)\\
  &\geq \frac{1}{2} \left(\left\lVert \nabla f \right\rVert^2 + \left\lVert \nabla f \right\rVert^2 + 2 \langle \nabla f, \nabla g \rangle\right)\\
\end{align}
$$
