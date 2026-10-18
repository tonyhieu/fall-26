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
  \vert f(x + s) - f(x) - \nabla f(x)^Ts \vert &\leq \frac{1}{2} L\lVert s \rVert^2
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
  \vert f(x + s) - f(x) - \nabla f(x)^T s - \frac{1}{2}s^T\nabla^2 f(x)s \vert &\leq \frac{1}{6}Q\lVert s \rVert^3
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

Let $u = y-x^2$. The gradient of $g$ is $\nabla g = (-2xu, u)$ by the chain rule. Plugging this into the PL-inequality gives $$\frac{1}{2}(y-x^2) \leq \frac{1}{2} \left\lVert (-2xu, u) \right\rVert^2 = \frac{1}{2}(4x^2u^2 + u^2) = \frac{1}{2}(4x^2 + 1)(y-x^2)^2.$$ Because $4x^2 + 1 \geq 1$, the inequality is always true.

Adding these two functions gives $$f + g = \frac{1}{2}y^2 + \frac{1}{2}(u)^2$$ and the gradient of $f+g$ is $$\nabla(f + g) = (-2xu, u + y),$$ maintaining the same $u = y-x^2$ from before. 

To show that the PL-inequality doesn't hold, consider when $y=\frac{x^2}{2}$. Note that this means $$u = \frac{x^2}{2} - x^2 = -\frac{x^2}{2}, \, u + y = \frac{1}{2}x^2 + \frac{1}{2}x^2 - x^2 = 0.$$ 

The left side becomes $$\frac{1}{2}y^2 + \frac{1}{2}u^2 = \frac{1}{2}(x^2)^2 + \frac{1}{2}(-x^2)^2 = \frac{x^4}{4}.$$ The right side becomes $$\frac{1}{2} \left\lVert \nabla (f+g) \right\rVert^2 = \frac{1}{2} \left\lVert (-x^3, 0) \right\rVert^2 = \frac{x^6}{2}.$$ 

Applying the PL-inequality gives $$\mu \cdot \frac{x^4}{4} \leq \frac{x^6}{2} \rightarrow \mu \leq 2x^2$$ for every $x \neq 0$ (as $\mu>0$). However, this inequality is provably false for a wide range of $x$ values. Consider $x = \frac{\sqrt{\mu}}{2}$ which is nonzero. This gives $$\mu \nleq \frac{\mu}{2}$$ which is always false. Thus, $f+g$ does not satisfy the PL-inequality.

This is distinct from the case in part (b), as $f$ and $g$ share variables (in this case, $x$ and $y$) as opposed to having separate variables (e.g. $x$, $y$, $w$, and $z$).

### (d)

Let us first rewrite the right hand side of the PL-inequality. Starting with the gradient, we have $$\nabla (f+g) = \nabla f + \nabla g$$ so we can expand the norm as $$\left\lVert \nabla (f+g) \right\rVert^2 = \left\lVert \nabla f+ \nabla g \right\rVert^2 = \left\lVert \nabla f \right\rVert^2 + \left\lVert \nabla g \right\rVert^2 + 2 \langle \nabla f, \nabla g \rangle.$$

Then, we can use the information given in the problem statement as an lower-bound for the right hand side:
$$
\begin{align}
  \frac{1}{2}\left\lVert \nabla (f+g) \right\rVert^2 &= \frac{1}{2} \left(\left\lVert \nabla f \right\rVert^2 + \left\lVert \nabla g \right\rVert^2 + 2 \langle \nabla f, \nabla g \rangle\right)\\
  &\geq \frac{1}{2} \left(\left\lVert \nabla f \right\rVert^2 + \left\lVert \nabla g \right\rVert^2 - 2\gamma \left\lVert \nabla f(x) \right\rVert \left\lVert \nabla g(x) \right\rVert \right)\\
\end{align}
$$

Let $a=\lVert \nabla f(x)\rVert$ and $b=\lVert\nabla g(x)\rVert$. The right hand term now becomes $$\frac{1}{2}(a^2 +b^2 - 2\gamma ab).$$ We can further bound this term by $\frac{1}{2}(1-\gamma)(a^2 + b^2)$, as 
$$
\begin{align}
  a^2 + b^2 - 2\gamma ab - (1-\gamma)(a^2 + b^2) &= a^2 + b^2 - 2\gamma ab - (a^2 + b^2 - \gamma a^2 - \gamma b^2)\\
  &= \gamma (a^2 + b^2 - 2ab)\\
  &= \gamma (a-b)^2.
\end{align}
$$

Because $\gamma \geq 0$ and squares are always nonnegative, $\gamma (a-b)^2 \geq 0$. Thus, we have shown that the lower bound for the right hand side can be reduced to $$\frac{1}{2}(1-\gamma)(a^2+b^2).$$

Let $\mu = \min\{\mu_f, \mu_g\}$. $f, g$ obviously satisfy $\mu$-PL since $\mu \leq \mu_f, \mu_g$. Adding up the two inequalities gives 
$$
\begin{align}
  \mu(f(x) - f^* + g(x) - g^*) &\leq \frac{1}{2}(\left\lVert \nabla f(x) \right\rVert^2 + \left\lVert \nabla g(x) \right\rVert^2)\\
  (1-\gamma)\mu(f(x) - f^* + g(x) - g^*) &\leq (1-\gamma)\frac{1}{2}(\left\lVert \nabla f(x) \right\rVert^2 + \left\lVert \nabla g(x) \right\rVert^2)\\
  &= \frac{1}{2}(1-\gamma) (a^2+b^2)\\
  &\leq \frac{1}{2}\left\lVert \nabla (f+g) \right\rVert^2.
\end{align}
$$

Note that $f(x) + g(x) \geq f^* + g^*$ because $f^*$ and $g^*$ are minimizers. This also means that $(f+g)^* \geq f^* + g^*$. We can now put everything together:
$$
\begin{align}
  (1-\gamma)\mu(f(x) + g(x) - (f+g)^*) &\leq (1-\gamma)\mu(f(x) - f^* + g(x) - g^*)\\
  &\leq \frac{1}{2}(1-\gamma) (a^2+b^2)\\
  &\leq \frac{1}{2} \left\lVert \nabla(f+g) \right\rVert^2
\end{align}
$$

Thus, we have shown that $(f+g)$ is $(1-\gamma)\min\{\mu_f, \mu_g\}$-PL.

At $(x, \frac{x^2}{2}$, the example from (c) does not satisfy the gradient condition, as shown below
$$
\begin{align}
  \langle \nabla f(x), \nabla g(x) \rangle &\geq -\gamma \left\lVert \nabla f(x) \right\rVert \left\lVert \nabla g(x) \right\rVert\\
  \langle (0, \frac{x^2}{2}), (x^3, -\frac{x^2}{2}) \rangle &\geq -\gamma \left\lVert (0, \frac{x^2}{2}) \right\rVert \left\lVert (x^3, -\frac{x^2}{2}) \right\rVert \\
  -\frac{x^4}{4} &\geq -\gamma \frac{x^2}{2} \sqrt{x^6 + \frac{x^4}{4}}\\
  -\frac{x^4}{4} &\geq -\gamma \frac{x^4}{4} \sqrt{4x^2 + 1}\\
  1 &\leq \gamma \sqrt{4x^2 + 1}\\
\end{align}
$$

This fails for many small values of $x$ and $\gamma$, so the condition is not true at all points, and the sum of the functions thus does not satisfy the gradient condition.

### (e)

Consider $h(x) = \frac{1}{2}x^2$. The function is smooth and twice differentiable with a minimum value $h^* = 0$. This function satisfies $1$-PL:
$$
\begin{align}
  h(x) - h^* &\leq \frac{1}{2} \left\vert h'(x) \right\vert^2\\
  \frac{1}{2}x^2 &\leq \frac{1}{2} x^2.
\end{align}
$$

Now consider $(h \cdot h)(x) = \frac{1}{4}x^4$. Suppose $(h*h)$ is $\mu$-PL for some $\mu > 0$. Plugging it into the PL-inequality, we get
$$
\begin{align}
  \mu\left((h\cdot h)(x) - (h*h)^*\right) &\leq \frac{1}{2} \left\vert (h*h)'(x) \right\vert^2\\
  \mu\left(\frac{1}{4}x^4\right) &\leq \frac{1}{2} x^6\\
  \mu &\leq 2 x^2\\
\end{align}
$$

This inequality does not hold when $x < \sqrt{\frac{\mu}{2}}$. Thus, $(h\cdot h)$ does not satisfy the PL property for any $\mu>0$.

### (f)

Consider $f(x) = x^2 + \sin x - x \cos x$. The derivative of this function is $f'(x) = x(2+\sin x)$. $f^*$ must have a minimum of $f^*=0$ at $x=0$, as that is the only value that satisfies the first order condition. 

$f(x)$ satisfies the PL-inequality. Note that $1 \leq 2+\sin x \leq 3$. Therefore, $$\left\vert x  \right\vert \leq \left\vert f'(x) \right\vert \leq 3 \left\vert x \right\vert.$$ By integrating $\left\vert f'(x) \right\vert \leq 3 \left\vert x \right\vert$, we can then conclude that $$f(x) \leq \frac{3x^2}{2}.$$ We can now prove that $f(x)$ satisfies the PL-inequality:
$$
\begin{align}
  \left\vert f'(x) \right\vert &\geq \left\vert x \right\vert\\
  \frac{1}{2} f'(x)^2 &\geq \frac{1}{2}x^2\\
  &= \frac{1}{3} \cdot \frac{3x^2}{2}\\
  &\geq \frac{1}{3}f(x)\\
  &= \frac{1}{3}(f(x) - f^*)
\end{align}
$$

Therefore, $f(x)$ is $\frac{1}{3}$-PL. Despite satisfying the PL-inequality, $f(x)$ is nonconvex, as its second derivative $$f''(x) = 2 + \sin x + x\cos x$$ is NOT nonnegative. Consider $x=-2\pi$. The second derivative at this point is $$f''(-2\pi) = 2 + 0 - 2\pi (1) < 0.$$ Therefore, $f(x)$ is not convex.

## Problem 3

### (a)

$$
\begin{align}
  \mathcal{R}(By) &= \frac{1}{n} \mathbb{E} \left\lVert By - s \right\rVert^2\\
  &= \frac{1}{n} \mathbb{E} \left\lVert B(s + \varepsilon) - s \right\rVert^2 && \text{(Definition of $y$)}\\
  &= \frac{1}{n} \mathbb{E} \left\lVert (B - I_n)s + B\varepsilon \right\rVert^2\\
  &= \frac{1}{n} \mathbb{E} \left[ \left\lVert (B-I_n)s \right\rVert^2 + 2\varepsilon^TB^T(B-I_n)s + \left\lVert B\varepsilon \right\rVert^2 \right]\\
  &= \frac{1}{n}  \left[ \mathbb{E}\left\lVert (B-I_n)s \right\rVert^2 + \mathbb{E}\left(2\varepsilon^TB^T(B-I_n)s\right) + \mathbb{E}\left\lVert B\varepsilon \right\rVert^2 \right]\\
  &= \frac{1}{n}  \left[ \left\lVert (B-I_n)s \right\rVert^2 + 2\mathbb{E}[\varepsilon]^T B^T(B-I_n)s + \mathbb{E} \varepsilon^TB^T B\varepsilon \right] && \text{($B$ and $s$ are deterministic)}\\
  &= \frac{1}{n}  \left[\left\lVert (B-I_n)s \right\rVert^2 + \mathbb{E} \varepsilon^TB^T B\varepsilon \right] && \text{($\mathbb{E}[\varepsilon] = 0$)}\\
  &= \frac{1}{n} \left\lVert (B-I_n)s \right\rVert^2 + \frac{1}{n} \mathbb{E} \, \text{tr}\left(\varepsilon^TB^T B\varepsilon\right) && \text{($\varepsilon^TB^T B\varepsilon$ is a scalar)}\\
  &= \frac{1}{n} \left\lVert (B-I_n)s \right\rVert^2 + \frac{1}{n} \mathbb{E} \,\text{tr}\left(B^T B\varepsilon\varepsilon^T\right) && \text{(Cyclic property)}\\
  &= \frac{1}{n} \left\lVert (B-I_n)s \right\rVert^2 + \frac{1}{n} \text{tr}\left(B^T B \,  \mathbb{E}[\varepsilon\varepsilon^T]\right) && \text{(Linearity of expectation)}\\
  &= \frac{1}{n} \left\lVert (B-I_n)s \right\rVert^2 + \frac{\sigma^2}{n} \text{tr}\left(B B^T \right) && \text{(Cyclic property + definition)}\\
\end{align}
$$

Expressing this in terms of $B=U \text{diag}(b_1, \ldots, b_n)U^T$ leads to
$$
\begin{align}
  \frac{1}{n} \left\lVert (B-I_n)s \right\rVert^2 + \frac{\sigma^2}{n} \text{tr}\left(B B^T \right) &= \frac{1}{n} \left\lVert U \text{diag}(b_1-1,\ldots,b_n-1) U^Ts \right\rVert^2 + \frac{\sigma^2}{n} \text{tr}\left(U \text{diag}(b_1,\ldots,b_n)^2 U^T \right)\\
  &= \frac{1}{n} \left\lVert \text{diag}(b_1-1,\ldots,b_n-1) U^Ts \right\rVert^2 + \frac{\sigma^2}{n} \text{tr}\left(\text{diag}(b_1,\ldots,b_n)^2 U^TU \right)\\
  &= \frac{1}{n} \sum_j (b_j-1)^2(u_j^Ts)^2 + \frac{\sigma^2}{n} \sum_j b_j^2\\
\end{align}
$$

### (b)

Using the formulas from class, we have
$$
\begin{align}
  B_\alpha y &= Xw_\alpha\\
  &= X(X^TX + \alpha nI)^{-1}X^Ty\\
  B_\alpha &= X(X^TX + \alpha nI)^{-1}X^T\\
  &= (XX^T + \alpha nI)^{-1}XX^T && \text{(Push-through identity)}\\
  &= (nK + \alpha nI)^{-1}nK && \text{(Definition of $K$)}\\
  &= (K + \alpha I)^{-1}K\\
  &= K(K + \alpha I)^{-1} && \text{(Commutativity due to being functions of $K$)}\\
\end{align}
$$

The existence of a orthogonal matrix $U$ whose columns satisfy $Ku_j = \lambda_j u_j$ means that $u_j$ are the eigenvectors of $K$. Because $B_\alpha$ is a function of $K$, $B_\alpha$ shares these eigenvectors. Let us calculate the value of $B_\alpha u_j$.

Starting with the $(K+\alpha I)^{-1}$ term, we have
$$
\begin{align}
  (K+\alpha I)u_j &= Ku_j + \alpha u_j\\
  &= (\lambda_j + \alpha) u_j\\
  (K+\alpha I)^{-1}u_j &= \frac{1}{\lambda_j + \alpha} \cdot u_j.
\end{align}
$$

Multiplying this by $K$ gives
$$
\begin{align}
  B_\alpha u_j &= K(K+\alpha I)^{-1}u_j\\
  &= K \cdot \frac{1}{\lambda_j + \alpha} \cdot u_j\\
  &= \frac{\lambda_j}{\lambda_j + \alpha} \cdot u_j
\end{align}
$$

This means that $u_j$ is an eigenvector of $B_\alpha$ with an eigenvalue of $b_j = \frac{\lambda_j}{\lambda_j + \alpha}$. We have thus found all of the eigenvalues of $B_\alpha$ in this basis.

Note that we can rewrite any vector $y$ in the $u_j$ basis using $y=\sum_j (u_j^Ty)u_j$. Thus, when we apply $B_\alpha$ to $y$, we get $$B_\alpha y = \sum_j (u_j^Ty)B_\alpha u_j = \sum_j b_j (u_j^Ty)u_j.$$

Observed responses with small eigenvalues get shrunk the most. Due to the eigenvalue being $\frac{\lambda_j}{\lambda_j + \alpha}$, any value of $\lambda_j \ll \alpha$ shrinks the corresponding eigenvector, causing them to go to 0.

### (c)

Using the answer from (a), we have
$$
\begin{align}
  \mathcal{R}(By) &= \frac{1}{n} \sum_j (b_j-1)^2(u_j^Ts)^2 + \frac{\sigma^2}{n} \sum_j b_j^2\\
  \mathcal{R}(\alpha) &= \frac{1}{n} \sum_j \left(\frac{\lambda_j}{\lambda_j + \alpha}-1\right)^2(u_j^Ts)^2 + \frac{\sigma^2}{n} \sum_j \left(\frac{\lambda_j}{\lambda_j + \alpha}\right)^2\\
  &= \frac{1}{n} \sum_j \frac{\alpha^2}{(\lambda_j + \alpha)^2}(u_j^Ts)^2 + \frac{\sigma^2}{n} \sum_j \frac{\lambda_j^2}{(\lambda_j + \alpha)^2}\\
\end{align}
$$

As $\alpha \downarrow 0$, the bias term goes to 0 while the variance goes to $\sigma^2$. As $\alpha \rightarrow \infty$, the bias term goes to $$\frac{1}{n} \sum_j (u_j^Ts)^2 = \frac{1}{n} \left\lVert U^Ts \right\rVert^2 = \frac{1}{n}\left\lVert s \right\rVert^2$$ while the variance goes to 0.

The prediction risk of an estimator that satisfies $X\hat{w}=y$ is the same as using $B=I_n$ in the first problem, leading to a prediction risk of $$\mathcal{R} = 0 + \frac{\sigma^2}{n}\cdot n = \sigma^2.$$

### (d)

By the limit as $\alpha \rightarrow 0$, $\mathcal{R}(0) = \sigma^2$. Note that this is the same value as when the training data is fit exactly by a predictor $\hat{w}$.

Let $c_j = u_j^Ts$. Using the result from part (c), we can calculate the difference between $\mathcal{R}(\alpha)$ and $\mathcal{R}(0)$ in order to show that it is negative for some value of $\alpha$:
$$
\begin{align}
  \mathcal{R}(\alpha) - \mathcal{R}(0) &= \frac{1}{n} \sum_j \frac{\alpha^2}{(\lambda_j + \alpha)^2}c_j^2 + \frac{\sigma^2}{n} \sum_j \frac{\lambda_j^2}{(\lambda_j + \alpha)^2} - \sigma^2\\
  &= \frac{1}{n} \sum_j \frac{\alpha^2c_j^2 + \sigma^2 \lambda_j^2}{(\lambda_j + \alpha)^2} - \frac{1}{n} \sum_j \frac{\sigma^2(\lambda_j + \alpha)^2}{(\lambda_j + \alpha)^2}\\
  &= \frac{1}{n} \sum_j \frac{\alpha^2c_j^2 + \sigma^2 \lambda_j^2 - \sigma^2(\lambda_j + \alpha)^2}{(\lambda_j + \alpha)^2}\\
  &= \frac{1}{n} \sum_j \frac{\alpha^2c_j^2 -2 \sigma^2\lambda_j\alpha - \alpha^2\sigma^2}{(\lambda_j + \alpha)^2}\\
  &= \frac{\alpha}{n} \sum_j \frac{\alpha(c_j^2 - \sigma^2) -2 \sigma^2\lambda_j}{(\lambda_j + \alpha)^2}\\
\end{align}
$$

Because $\alpha > 0$, the sign of the sum is the sign of $\mathcal{R}(\alpha) - \mathcal{R}(0)$. Let us first fix $s$, and let $\lambda_\min = \min_j \lambda_j > 0$ (positive because the rank of $X$ is $n$). Choose any $\alpha$ such that $$0 < \alpha < \frac{2\sigma^2\lambda_\min}{\left\lVert s \right\rVert^2}.$$

For each $j$, $$c_j^2 \leq \sum_i c_i^2 = \left\lVert U^Ts \right\rVert^2 = \left\lVert s \right\rVert^2.$$ We can now use this fact to show that the numerator is negative:
$$
\begin{align}
  \alpha(c_j^2 - \sigma^2) &= \alpha c_j^2 - \alpha \sigma^2 \\
  &\leq \alpha c_j^2 && \text{($\alpha, \sigma > 0$)}\\
  &\leq \alpha \left\lVert s \right\rVert^2 \\
  &\leq 2\sigma^2 \lambda_\min && \text{(Defined by our choice of $\alpha$)}\\
  &\leq 2\sigma^2\lambda_j && \text{(Definition of $\min$)}.
\end{align}
$$

Therefore, we have $$\alpha(c_j^2 - \sigma^2) - 2\sigma^2\lambda_j < 0, \, \forall j$$ proving that there exists a value of $\alpha$ such that $\mathcal{R}(\alpha) < \mathcal{R}(0)$. Note that if $s=0$, then any value of $\alpha > 0$ satisfies this inequality, as $$-\alpha\sigma^2 - 2\sigma^2 \lambda_j < 0.$$

## Problem 4

### (a)

From the lecture notes, we have $r_k = Xw_k - y$ which can be written as $$r_{k} = X_{w_{k}}-y = \left(I - \eta \frac{XX^T}{n}\right)^{k}r_0.$$ Using the identity $K= \frac{1}{n}XX^T$ from Problem 3, this can be further simplified as $$r_k = \left(I - \eta K\right)^{k}r_0.$$

In the problem description, we are given $w_0 = 0$. This means that $$r_0 = X \cdot 0 - y = -y$$ making the final expression for $r_k$ be $$r_k = - \left(I - \eta K\right)^{k}y.$$ 

Applying this to the original $r_k = Xw_k - y$ equation gives
$$
\begin{align}
  Xw_k &= y + r_k\\
  &= y - \left(I - \eta K\right)^{k}y
\end{align}
$$

We can use the same eigenbasis as in Problem 3: $$Ku_j = \lambda u_j$$ with $U$ being an orthogonal matrix. Let us first project the $\left(I - \eta K\right)^{k}y$ term onto this eigenbasis:
$$
\begin{align}
  (I-\eta K)u_j &= Iu_j - \eta Ku_j\\
  &= u_j - \eta \lambda_j u_j\\
  &= (1 - \eta \lambda_j)u_j\\
  (I-\eta K)^ku_j &= (1 - \eta \lambda_j)^ku_j
\end{align}
$$

When applying the $u^T_j$ term to both sides of the equation (as is asked in the problem description), we can use the fact that $I-\eta K$ is symmetric in order to simplify the right side as 
$$
\begin{align}
  u_j^T (I-\eta K)^k &= \left[(I-\eta K)^k u_j\right]^T\\
  &= (1-\eta \lambda_j)^k u_j^T.
\end{align}
$$

Thus, we have
$$
\begin{align}
  u_j^T Xw_k &= u_j^T y - (1-\eta \lambda_j)^k u_j^Ty\\
  &= \left[1 - (1-\eta \lambda_j)^k\right] u_j^Ty.
\end{align}
$$

Therefore, the multiplier is $$g_k(\lambda) = 1 - (1-\eta \lambda)^k.$$

Let $t=1-\eta\lambda$. Because $0\leq \eta\lambda \leq 1$ is given, $t\in [0,1]$. Plugging $t$ into $g_k(\lambda)$ gives $$g_k(\lambda) = 1-t^k.$$ The following properties hold:
1. **$g_k(\lambda)$ takes values in $[0,1]$**. Since $t\in [0,1]$, this holds, as it implies that $t^k \in [0,1]$ and thus $g_k(\lambda)= 1-t^k \in [0,1]$.
2. **Nondecreasing in $k$**. Since $t \leq 1$, as $k$ increases, $t^k$ is nonincreasing, meaning that $g_k(\lambda)=1-t^k$ is nondecreasing.
3. **Nondecreasing in $\lambda$**. Since the value of $t$ is decreasing in $\lambda$, $t^k$ is also decreasing in $\lambda$ and $g_k(\lambda) = 1-t^k$ is nondecreasing in $\lambda$.

### (b)

Let $x=\eta\lambda$. We know that $x\in [0,1]$ from the last question. We can rewrite the spectral filter as $$g_k(\lambda) = 1-(1-x)^k.$$

To prove the upper bound, we need to prove that $g_k$ is less than or equal to both $1$ and $kx$, as those facts imply that $g_k \leq \min\{1, kx\}$. We have already shown in the last question that $g_k(\lambda) \in [0,1]$, so $g_k \leq 1$ must be true.

Using the definition of $t = 1-\eta\lambda = 1-x$, we can rewrite $1 - (1-x)^k$ as $$1-t^k = (1-t)(1+t+\cdots+t^{k-1}).$$ Note that, because $t\leq 1$, all of the terms in the $(1+t+\cdots+t^{k-1})$ quantity must be less than or equal to $1$. Adding them all up makes the upper bound of the sum $k$. Using this fact, we have
$$
\begin{align}
  g_k(\lambda) &= (1-t)(1+t+\cdots+t^{k-1})\\
  &= x(1+t+\cdots+t^{k-1}) && \text{($1-t = x$)}\\
  &\leq x \cdot k\\
  &\leq \eta k \lambda.
\end{align}
$$

To prove the lower bound, notice that $$1-x \leq e^{-x} \; \forall x$$ because $e^{-x}$ curves away from $1-x$ at their intersection point $(0,1)$, making the former always greater than or equal to the latter. On $x\in [0,1]$, both functions are nonnegative, so raising both sides of the inequality to the $k$-th power preserves order. Thus, $$(1-x)^k \leq e^{-xk}$$ allowing us to apply this inequality to $g_k$:
$$
\begin{align}
  g_k(\lambda) &= 1-(1-x)^k\\
  &\geq 1-e^{-xk}\\
  &= 1-e^{-\eta k \lambda}.
\end{align}
$$

Now, let's analyze the regimes. Let $s=\eta k\lambda$. The bounds then become $$1-e^{-s} \leq g_k \leq \min \{1, s\}.$$
- $s \ll 1$: Using the Taylor expansion, the lower bound becomes $$1-e^{-s} \approx s- \frac{s^2}{2} \approx s$$ and the upper bound becomes $s$. This means that ${g_k \approx s \approx 0}$. In this regime, the eigenvectors $u_j^T$ are not fit, and the direction is not yet learned.
- $s\gg 1$: The lower bound becomes $$1-e^{-s} \approx 1-0 \approx 1$$ and the upper bound becomes $1$, so $g_x \approx 1$. In this regime, the eigenvectors are almost completely fit.

The transition between regimes occurs at $s\approx 1$.

In Problem 3b, the filter was $b(\lambda) = \frac{\lambda}{\lambda + \alpha}$. Setting $\alpha \approx \frac{1}{\eta k}$, gives $$b(\lambda) = \frac{\lambda}{\frac{1 + \lambda\eta k}{\eta k}} = \frac{\lambda\eta k}{1 + \lambda\eta k} = \frac{s}{1+s}.$$

Similar to the filter from this problem, when $s\ll 1$, $b\approx s$ because the denominator goes to $1$. When $s\gg 1$, $b \approx 1$ because the numerator and denominator go to $s$. Additionally, the regime also changes at $s\approx 1$, so setting $a\approx \frac{1}{\eta k}$ makes the transition scales match.

Intuitively, what this means is that GD with finite time and ridge with $\alpha = \frac{1}{\eta k}$ have similar filters; they exhibit the same behavior as they go to their limits (min/max). However, GD with finite time and ridge with $\alpha = \frac{1}{\eta k}$ are not the same estimator. Estimators are defined by their filters, and the filters of these two methods are still distinct. ${\frac{s}{1+s}}$ has a much more sharp transition between the two regimes, where as ${1-e^{-s}}$ transitions much more smoothly. They also have different values at different values of $s$, so the two estimators cannot be the same.

### (c)

Using the defined GD update from the problem description, we have $$w_{k+1} = w_k - \frac{\eta}{n} X^T r_{k},$$ where $r_k = Xw_k - y$. We can further simplify this down:
$$
\begin{align}
  w_{k+1} &= w_k - \frac{\eta}{n} X^T r_{k}\\
  \Pi_{\text{Ker} X}w_{k+1} &= \Pi_{\text{Ker} X}w_k - \frac{\eta}{n} \Pi_{\text{Ker} X}(X^T r_{k}) && \text{(Projection is linear)}\\
  &= \Pi_{\text{Ker} X}w_k && \text{(Zero-initialized GD stays in $\text{range}(X^T)$)}\\
  &= \Pi_{\text{Ker} X}w_0 && \text{(By induction)}\\
  &= 0. && \text{($w_0=0$)}
\end{align}
$$

Since we have concluded that the kernel portion of $w_{k+1}$ is zero, this means that only the range portion of $w_{k+1}$ matters. Let $\Sigma = \text{diag}(\rho_1, \ldots, \rho_n)$. We have
$$
\begin{align}
  w_{k} &= \Pi_{\text{range} X^T}w_k + \Pi_{\text{Ker} X}w_k\\
  &= \Pi_{\text{range} X^T}w_k\\
  &= X^T (XX^T)^{-1}Xw_k && \text{(Lecture 3 notes)}\\
  &= (V\Sigma U^T)(U\Sigma^{-2}U^T)(U\Sigma V^T)w_k\\
  &= V\Sigma\Sigma^{-2}\Sigma V^Tw_k\\
  &= VV^Tw_k\\
  &= \sum_j (v_j^T w_k)v_j. 
\end{align}
$$

We need to now find a way to express $v_j^T w_k$ in terms of $g_k$ and $\rho_j$. Using $U^T$, we get
$$
\begin{align}
  U^T Xw_k &= U^TU\Sigma V^T w_k\\
  &= \Sigma V^T w_k
\end{align}
$$

This is equivalent to $$u_j^T Xw_k = \rho_j (v_j^T w_k).$$ From part (a), we have $$u_j^T Xw_k g_k(\lambda_j) u_j^Ty = g_k\left(\frac{\rho_j^2}{n}\right) u_j^Ty.$$ Setting this equal to each other and dividing by $\rho_j > 0$ (because $\text{rank}(X) = n$) gives us $$v_j^T w_k = \frac{1}{\rho_j} g_k\left( \frac{\rho_j^2}{n} \right) u_j^Ty.$$

Plugging this into our previous equation gives $$w_{k} = \sum_j \frac{g_k(\rho_j^2/n)}{\rho_j} (u_j^Ty) v_j$$ which is the exact expression we were looking for.

Let $m_j=\frac{g_k(\rho_j^2/n)}{\rho_j}$. From part (a), we know that $g_k \in [0,1]$, and $\rho_j>0$ because $X$ is positive definite. Therefore, $$m_j \geq 0.$$

From the problem description, $\eta \leq \frac{1}{L} = \lambda_\max\left(\frac{1}{n}XX^T\right)$. This means that we also have $0\leq \eta \lambda_j \leq 1$ which is the same as parts (a) and (b). Thus, the upper bound from part (b) applies, and $$g_k(\lambda) \leq \min\{1, \eta k\lambda\}.$$

Since $\lambda= \frac{\rho_j^2}{n}$, the inequality becomes $g_k(\frac{\rho_j^2}{n}) \leq \min\{1, \eta k\frac{\rho_j^2}{n}\}$. Dividing both upper bounds by $\rho_j$ gives us the final upper bound: $$m_j \leq \min\left\{ \frac{1}{\rho_j}, \frac{\eta k\rho_j}{n} \right\}.$$

Thus, $$0 \leq m_j \leq \min\left\{ \frac{1}{\rho_j}, \frac{\eta k\rho_j}{n} \right\}.$$ 

The min-norm interpolator $w^\dagger$ is given in the Lecture 3 notes as $$w^\dagger = X^T(XX^T)^{-1}y.$$ Substituting in $X=U\Sigma V^T$ gives $$w^\dagger = $$
$$
\begin{align}
  w^\dagger &= X^T(XX^T)^{-1}y\\
  &= (V\Sigma U^T)(U\Sigma^{-2}U^T)y\\
  &= V\Sigma^{-1}U^Ty\\
  &= \sum_j \frac{1}{\rho_j} (u_j^Ty)v_j.
\end{align}
$$

The difference between the min-norm interpolator and GD is the $g_k\in [0, 1]$ factor. As shown earlier, $m_j \leq \min\left\{ \frac{1}{\rho_j}, \frac{\eta k\rho_j}{n} \right\}$, so the $g_k$ factor prevents $m_j$ from blowing up as $\rho_j\downarrow 0$ (due to the $\frac{\eta k\rho_j}{n}$ upper bound), whereas the min-norm interpolator blows up.

### (d)

Let us define $t_j = 1-\eta\lambda_j$ and $c_j = u_j^Ts$, similar to what we did in previous problems. From part (a), we also have $g_k(\lambda_j) = 1 - t_j^k$. We will use the following two facts:
- $t_j < 1$ because $\eta > 0$ and $\lambda_j > 0$ from $\text{rank}(X) = n$
- $t_j \geq 0$ because $\eta \leq \frac{1}{L} \rightarrow \eta\lambda_j \leq 1$
This means that $t_j \in [0,1)$.

From part (a), we found that $$Xw_k = B_k y, \; B_k = U \text{diag}(g_k(\lambda_j))U^T.$$ We can use this in our derivation for $f(w_k)$:
$$
\begin{align}
  Xw_k - y &= U \text{diag}(g_k(\lambda_j)-1) U^Ty\\
  \left\lVert Xw_k - y \right\rVert^2 &= \sum_j (1-g_k(\lambda_j))^2 (u_j^Ty)^2 \\
  \frac{1}{2n}\left\lVert Xw_k - y \right\rVert^2 &= \frac{1}{2n}\sum_j (1-g_k(\lambda_j))^2 (u_j^Ty)^2 \\
  &= \frac{1}{2n}\sum_j t_j^{2k} (u_j^Ty)^2.
\end{align}
$$

Problem 3a also gives us $$\mathcal{R}(By) = \frac{1}{n}\sum_j (1-b_j)^2 (u_j^Ts)^2 + \frac{\sigma^2}{n}\sum_j b_j^2.$$ Substituting in $b_j = g_k(\lambda_j) = 1-t_j^k$ and $c_j$ gives $$R_k = \frac{1}{n}\sum_j t_j^{2k}c_j^2 + \frac{\sigma^2}{n} \sum_j (1-t_j^k)^2 .$$

The training loss is the $f(w_k)$ term. Each run adds one to $k$ which thus adds a multiple of $t_j$ after each run. Because $t_j \in [0,1)$, the training loss is nonincreasing; each run contracts the loss by $t_j$.

In $R_k$, the squared bias is the first $\frac{1}{n}\sum_j t_j^{2k}c_j^2$ term while the variance is the $\frac{\sigma^2}{n} \sum_j (1-t_j^k)^2$ term. Using similar logic as with the training loss, each additional run contracts the sum by $t_j$ in the bias, so the squared bias is nonincreasing. For the variance, the $t_j^k$ terms get smaller (or stay the same if $t_j=0$) each iteration, so the difference $1-t_j^k$ is nondecreasing. Thus, the entire sum is nondecreasing.

Using the assumption that $0^0=1$ to find $R_0$, we have $k=0, w_0=0, g_0=0$. Plugging these in shows that the variance is 0 $(\sum_j (1-1)^2 = 0)$ and the squared bias is $\frac{1}{n}\sum_j c_j^2.$ Using the fact that $\sum_j c_j^2 = \left\lVert s \right\rVert^2$, we have $$R_0 = \frac{\left\lVert s \right\rVert^2}{n}.$$ This matches that $\alpha \rightarrow \infty$ of the ridge estimator.

When $k \rightarrow 0$, $t_j^k \rightarrow 0$. Thus, we have $$\lim_{k \rightarrow \infty} R_k = \sigma^2.$$

Training loss measures the distance from $Xw_k$ to $y$, while prediction risk measures the distance from $Xw_k$ to $s$. Note that $y = s + \varepsilon$; thus, the training loss measures the distance from our estimator to the signal PLUS some noise, while the prediction risk measures the distance from our estimator to just the signal. If we overfit our estimator to $y$, then the training loss could continue to decrease, but the distance to the actual signal could increase. Therefore, decreasing training loss does not imply decreasing prediction risk.

Lecture 3 states that GD converges to the minimum-norm interpolator $$w_\infty=X^\dagger = w^\dagger$$ after an infinite number of steps. However, as just stated above, going to the solution with the minimum training loss is not necessarily the best, as later iterates will increase the prediction risk. Thus, early stopping beats the minimum-norm implicit bias for learning the real signal.
