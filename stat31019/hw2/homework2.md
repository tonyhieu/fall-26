# STAT 31019 Homework 2

AI Usage Disclosure: LLMs were used in order to help when stuck on problems and to reformat this file from Markdown to LaTeX on Overleaf. Answers were NOT copied verbatim.

## Problem 1

### (a)

Using the fact that $f$ is $\mu$-strongly convex, we can use the definition of strong convexity with $x=w^*$ and $y=w_0$:
$$
\begin{align}
  f(w_0) &\geq f(w^*) + \left\langle \nabla f(w^*), w_0 - w^*  \right\rangle + \frac{\mu}{2}\left\lVert w_0 - w^* \right\rVert^2\\
  &\geq f^* + \left\langle 0, w_0 - w^*  \right\rangle + \frac{\mu}{2}\left\lVert w_0 - w^* \right\rVert^2 && \text{(Minimizer must have a gradient equal to 0)}\\
  &\geq f^* + \frac{\mu}{2}\left\lVert w_0 - w^* \right\rVert^2\\
  \frac{2}{\mu}\left(f(w_0) - f^*\right) &\geq \left\lVert w_0 - w^* \right\rVert^2.\\
\end{align}
$$

Plugging this into the lecture rate gives:
$$
\begin{align}
  f(w_k) - f^* &&\leq \frac{2L \left\lVert w_0 - w^* \right\rVert^2}{k^2}\\
\leq \frac{4L \left(f(w_0) - f^*\right)}{\mu k^2}.
\end{align}
$$

Setting the coefficient equal to $\frac{1}{2}$ allows us to solve for $k$:
$$
\begin{align}
  \frac{4L}{\mu k^2} &\leq \frac{1}{2}\\
  \frac{8L}{\mu} &\leq k^2\\
  k &\geq \sqrt{\frac{8L}{\mu}}
\end{align}
$$

Now, we want to find an integer $T^*$ that satisfies $k \geq T^* \geq \sqrt{\frac{8L}{\mu}}$. We can use the fact that $L \geq \mu$ to choose $$T^* = \left\lceil 4\sqrt{\frac{L}{\mu}} \right\rceil$$ as our integer, in line with part (b)'s inequality.

Below is a proof that $L \geq \mu$:
$$
\begin{align}
  f(x) + f(y) &\geq f(x) + f(y) + \left\langle \nabla f(x), y-x \right\rangle + \left\langle \nabla f(y), x-y \right\rangle + \mu \left\lVert x-y \right\rVert^2 && \text{($\mu$-SC)}\\
  \mu \left\lVert x-y \right\rVert^2 &\leq \left\langle \nabla f(x) - \nabla f(y), x-y \right\rangle\\
  &\leq \left\lVert \nabla f(x) - \nabla f(y) \right\rVert \cdot \left\lVert x-y \right\rVert && \text{(Cauchy-Schwarz)}\\
  &\leq L \left\lVert x-y \right\rVert^2 && \text{($L$-Lipschitz)}\\
  \mu &\leq L.
\end{align}
$$

### (b)

Note that $w_k$ and $w_0$ from the inequality in part (a) can be replaced with $z_{i+1}$ and $z_i$, respectively, as $z_i$ is the starting point for each run. Thus, by induction, we have $$f(z_N) - f^* \leq 2^{-N}(f_(z_0) - f^*),$$ where $N$ is the number of iterations. We want the gap $f(z_i) - f^* \leq \varepsilon$. Using the above inequality, the number of iterations can be found:
$$
\begin{align}
  2^{-N}(f_(z_0) - f^*) &\leq \varepsilon\\
  \frac{f_(z_0) - f^*}{\varepsilon} &\leq 2^N\\
  \log_2 \left(\frac{f_(z_0) - f^*}{\varepsilon}\right) &\leq N.
\end{align}
$$

To make $N$ an integer, we can again use the ceiling function. Since we are running the algorithm $T^*$ times with $N$ iterations each time, the total number of iterations is $$\left\lceil 4\sqrt{L/\mu}\right\rceil \cdot \left\lceil \log_2 \left(\frac{f_(z_0) - f^*}{\varepsilon}\right)\right\rceil.$$

## Problem 3

### (a)

We can use $F(w) = \arctan x$. There is one root, $w^*=0$, with a derivative of $F'(w^*) = 1 \neq 0$. Additionally, $F'(w) > 0 \quad \forall x$, so all iterates are well defined. The Newton map is defined as $$g(w) = w - (1+w^2)\arctan w.$$

$\arctan w$ is odd, so $F(-w) = -F(w)$ and $g(-w) = -g(w)$. Define $$h(w) = (1+w^2)\arctan w - w, \quad w>0.$$ In relation to $g$, $g(w) = -h(w)$ for $w>0$ and by oddness, $-g(w) = h(w)$. This means that $$\left\vert g(w) \right\vert = h(\vert w \vert)$$ for all $w\neq 0$. We can thus express the iterates as $$\left\vert w_{k+1} \right\vert = h(\left\vert w_k \right\vert)$$ and measure the magnitude of the iterates.

To measure the magnitude of the *jump* between iterates, express $h(w)$ as $$h(w) = w + d(w), \quad d(w) = (1+x^2)\arctan x - 2x$$ where $d(w)$ represents the jump in magnitude. We can then express the iterates as $$\left\vert w_{k+1} \right\vert = \left\vert w_k \right\vert  + d(\left\vert w_k \right\vert).$$ Divergence occurs if $d(\left\vert w_k \right\vert)$ is greater than or equal to a positive constant.

Now, let us show that $d$ is increasing for $w\geq 1$. Differentiating $d$ with respect to $w$ gives $$d'(w) = 2w \arctan w + 1 - 2 = 2w \arctan w - 1.$$ Since $\arctan x \geq 0$ on $x \geq 0$, $d'(w) \geq 0$ on $w\geq 1$. Therefore, $d$ is nondecreasing on $[1, \infty)$.

We can now use induction to show that divergence occurs. Let $w_0=1.5$ and our positive constant $c = d(1.5)$. Using a calculator, one can confirm that $c=d(1.5) > 0$. We claim that $\left\vert w_k \right\vert \geq 1.5 + kc$ for all $k \geq 0$.
- Base case: $\left\vert w_0 \right\vert = 1.5 \geq 1.5$.
- Inductive step: Since $\left\vert w_k \right\vert \geq 1.5 + kc$, $d(\left\vert w_k \right\vert) \geq d(1.5) = c$ because $d$ is nondencreasing on $[1, \infty)$. Therefore, we have $$\left\vert w_{k+1} \right\vert = \left\vert w_k \right\vert + d(\left\vert w_k \right\vert) \geq 1.5 + kc + c = 1.5 + (k+1)c.$$

Thus, we have shown that the magnitude of the iterates increase by a positive constant $c$, meaning that the iterates diverge to $\infty$.

### (b)

The Newton map for $F$ is given by $$g(w) = w - \frac{w^3 - 2w + 2}{3w^2 + 2}.$$ To find $w_0, w_1$, I used the guess-and-check method. Trying $0$ and $1$ shows that
$$
\begin{align}
  g(0) &= 0 - \frac{0 - 0 + 2}{0 - 2} = 1 \\
  g(1) &= 1 - \frac{1 - 2 + 2}{3 - 2} = 0.
\end{align}
$$

Therefore, $0$ and $1$ are two distinct points such that the Newton iterates cycle between them forever.

### (c)

Watched the video!

### (d)

Let us first start with the chain rule to define $\nabla \psi(z)$ and $\nabla^2 \psi(z)$: $$\nabla \psi(z) = A^T \nabla f (Az), \quad \nabla^2 \psi(z) = A^T \nabla^2 f(Az) A.$$ Note that $\nabla^2 \psi(z)$ is invertible, as $f$ has "invertible Hessians everywhere" and $A$ is given as invertible; thus, $\left[\nabla^2 \psi(z)\right]^{-1}$ is well-defined.

Let $g = \nabla f(Az)$ and $H = \nabla^2 f(Az)$. Substituting in these values, we get
$$
\begin{align}
  z_{k+1} &= z_k - \left[\nabla^2 \psi(z_k)\right]^{-1} \nabla \psi (z_k)\\
  &= z_k - A^{-1} H^{-1} \left[A^T\right]^{-1} A^T g\\
  &= z_k - A^{-1} H^{-1} g\\
  (1^*) \quad Az_{k+1} &= Az_k - H^{-1} g.\\
\end{align}
$$

Now, we can use induction to show that $w_k = Az_k$ for every $k$.
- Base case: We are given that $w_0 = Az_0$.
- Inductive step: Using $(1^*)$, and substituting in $w_k=Az_k$, $$Az_{k+1} = Az_k - H^{-1} g = w_k - \left[\nabla^2 f(w_k)\right]^{-1} \nabla f(w_k) = w_{k+1}.$$

Therefore, $w_k = Az_k$ for every $k$.

## Problem 4

### (a)

Let us start with Taylor's theorem, slightly modified from the one in Lecture 2: $$\left\vert f(w + s) - f(w) - \langle \nabla f(w), s \rangle \right\vert \leq \frac{L}{2} \left\lVert s \right\rVert^2.$$ Let $s=\eta_k p_k= -\eta_k H_k g_k$. Using this with Taylor's theorem, we can derive 
$$
\begin{align}
  \left\vert f(w_k + \eta_k p_k) - f(w_k) - \langle \nabla f(w_k), \eta_k p_k \rangle \right\vert &\leq \frac{L}{2} \left\lVert \eta_k p_k \right\rVert^2\\
  \left\vert f(w_{k+1}) - f(w_k) - \langle g_k, \eta_k p_k \rangle \right\vert &\leq \frac{L\eta_k^2}{2} \left\lVert p_k \right\rVert^2\\
  f(w_{k+1})  &\leq f(w_k) + \langle g_k, \eta_k p_k \rangle + \frac{L\eta_k^2}{2} \left\lVert p_k \right\rVert^2\\
  &= f(w_k) - \eta_k g_k^T H_k g_k + \frac{L\eta_k^2}{2} \left\lVert H_k g_k \right\rVert^2\\
  &= f(w_k) - \eta_k \left\lVert g_k \right\rVert^2_{H_k} + \frac{L\eta_k^2}{2} \left\lVert H_k^{1/2}(H_k^{1/2}g_k) \right\rVert^2 && \text{(Mahalanobis norm)}\\
  &\leq f(w_k) - \eta_k \left\lVert g_k \right\rVert^2_{H_k} + \frac{L\eta_k^2}{2} \left\lVert H_k^{1/2} \right\rVert_\text{op}^2 \cdot \left\lVert H_k^{1/2}g_k \right\rVert^2 \\
  &= f(w_k) - \eta_k \left\lVert g_k \right\rVert^2_{H_k} + \frac{L\eta_k^2}{2} \lambda_\max (H_k) \cdot g_k^THg_k && \text{$H_k^{1/2}$ is symmetric PSD because $B_k \succ 0$}\\
  &= f(w_k) - \left(\eta_k  - \frac{L\eta_k^2}{2} \lambda_\max (H_k)\right) \left\lVert g_k \right\rVert^2_{H_k}\\
  &= f(w_k) - \left(\eta_k  - \frac{L\eta_k^2}{2\lambda_\min (B_k)} \right) \left\lVert g_k \right\rVert^2_{B_k^{-1}} && \text{$H_k = B_k^{-1}$}.
\end{align}
$$

Thus, we have proven this lemma from Lecture 7. To guarantee strict decrease, we need $$\eta_k \left(1 - \frac{L\eta_k^2}{2\lambda_\min (B_k)}\right) < 0 \iff 0 < \eta_k < \frac{2\lambda_\min(B_k)}{L}.$$ Since $g_k \neq 0$ and $B_k^{-1} \succ 0$, the entire term subtracted is positive, so we have strict decrease.

### (b)

Let $H=H_k$, $s = s_k$, $y = y_k$, $\rho = \rho_k$, and $V= I - \rho s y^T$, meaning that $V^T = I - \rho y s^T$. The update becomes $$H_{k+1} = V H V^T + \rho s s^T.$$
$H_{k+1}$ is symmetric because H is symmetric: $$(VHV^T)^T = (V^T)^T H^T V^T = VHV^T.$$ Also, $\rho s s^T$ is symmetric: $$(\rho s s^T) = \rho (s^T)^T s^T = \rho s s ^T$$ because $s$ is a scalar.

To show that $H_{k+1} \succ 0$, we use a proof similar to the one from Lecture 7. Take $v \in \mathbb{R}^d \backslash \{0\}$: $$v^T H_{k+1}v = (V^Tv)^T H (V^Tv) + \rho (s^Tv)^2.$$ Both terms are semipositive definite, as $H\succ 0$ and $\rho \succ 0$. To make the sum 0, both terms need to vanish:
- If $\rho (s^Tv)^2 = 0$, then $s^Tv = 0$.
- If $s^Tv = 0$, then $V^Tv = v - \rho y s^T v = v$, so the term becomes $v^T H v$ which must be positive because $v\neq 0$ and $H \succ 0$.

Therefore, both terms cannot vanish, meaning that $v^T H_{k+1} v \succ 0$ for every $v\neq 0$, implying that $H_{k+1} \succ 0$.

To show that $H_{k+1}$ satisfies the secant equation, multiply both sides by $y$:
$$
\begin{align}
  H_{k+1}y &= V H V^Ty + \rho s s^Ty\\
  &= V H (y - \rho y s^T y) + \rho s s^Ty\\
  &= V H (y - y) + s && \text{($\rho s^T y = \rho y^T s= 1$)}\\
  &= s
\end{align}
$$

A descent direction for $f$ is defined as a vector $p$ such that $\langle \nabla f, p \rangle < 0$. In our case, we have $g = \nabla f$ and $p = -Hg$. Therefore, we have $$\langle g_{k+1}, p_{k+1} \rangle = -g_{k+1}^T H_{k+1}g_{k+1} < 0$$ whenever $g_{k+1}$ because $H_{k+1} \succ 0$. This means that moving along $p$ decreases $f$, making it a descent direction. When $g_{k+1} = 0$, then you're at a critical point and $p_{k+1}=0$.

The main term causing the number of operations to be $O(d^3)$ is the $VHV^T$ term. Expanding it gives $$VHV^T = H - \rho sy^T H - \rho H y s^T + \rho H s y s^T + \rho^2 (y^T H y) s s ^T.$$ Let $u=Hy$; since $H$ is symmetric, $u^T = y^TH$. Using the expansion with the original $\rho ss^T$ term gives $$H_{k+1} = H - \rho (su^T - us^T) + (\rho + \rho^2y^Tu) ss^T.$$

The number of operations for each part of the update is:
- $O(d^2)$ for the matrix-vector product $u=Hy$
- $O(d)$ for the inner products $y^Tu$ and $\rho = (y^Ts)^{-1}$
- $O(d^2)$ for the outer products $su^T$, $us^T$, and $ss^T$

Therefore, the number of operations is $O(d^2)$.

### (c)

Using the hint, we have $\phi(\eta) = f(w + \eta p)$. Taking the first derivative, we have $$\phi'(\eta) = \nabla f(w + \eta p)^T p \iff \phi'(0) = \nabla f(w)^T p.$$ We also know that $\phi'(0) < 0$ because $p$ is a descent direction. Substituting $\phi$ into the two Wolfe conditions gives
$$
\begin{align}
  \text{(W1)} &\quad \phi(\eta) \leq \phi(0) + c_1 \eta \phi'(0)\\
  \text{(W2)} &\quad \phi'(\eta) \geq c_2 \phi'(0).
\end{align}
$$

Let $g(\eta) = \phi(0) + c_1\eta \phi'(0)$. We can relate this to $\phi$ using a first-order Taylor's approximation around $0$: $$\phi(\eta) = \phi(0) + \eta \phi'(0) + o(\eta).$$ Subtracting $g(n)$ from both sides gives $$\phi(\eta) - g(\eta) = \phi(0) + \eta\phi'(0) + o(\eta) - \phi(0) - c_1\eta\phi'(0)= (1-c_1)\eta \phi'(0) + o(\eta).$$ Since we know that $c_1 < 1$ and $\phi'(0) < 0$, the main leading term must be negative, implying that $\phi(\eta) < g(\eta)$ for small $\eta>0$ such that $o(\eta)$ does not affect the right side.

However, we know that $\phi$ does go above $g$ eventually, as $\phi$ bounds $f$ below as stated in the problem description while $g \rightarrow -\infty$ as $\eta \rightarrow \infty$. More specifically, $\phi(\eta) > g(\eta)$ when $\eta$ is large enough such that $o(\eta)$ overrides $(1-c_1)\eta \phi'(0)$. Thus, we must find the intersection point.

Let $S = \{\eta > 0: \phi(\eta) = g(\eta)\}$; in other words, $S$ is the set of $\eta > 0$ such that $\phi(\eta)$ intersects with $g(\eta)$. Because $\phi - g$ is continuous, negative after 0, and positive for large $\eta$, we know that $S$ must be nonempty by the intermediate value theorem. Additionally, because $S$ is closed in $(0,\infty)$ and is bounded away from $0$, as shown by the first-order Taylor expansion analysis, it must have a smallest element $\eta^* > 0$.

Therefore, we have $\phi(\eta) < g(\eta)$ for all $\eta < \eta^*$ and $\phi(\eta^*) = g(\eta^*)$. Because $g(\eta) = \phi(0) + c_1\eta\phi'(0)$, we have shown that there exists $\eta \in (0, \eta^*]$ that satisfies (W1).

At $\eta^*$, the following holds: $$\phi(\eta^*) - \phi(0) = c_1\eta^*\phi'(0).$$ By the mean value thorem, there exists some $\eta^{**} \in (0, \eta^*)$ such that $$\phi'(\eta^{**}) = \frac{\phi(\eta^*) - \phi(0)}{\eta^*} = c_1\phi'(0).$$

Since $\phi'(0) < 0$ and $c_1 < c_2$, $c_1\phi'(0) > c_2\phi'(0)$ must hold. Therefore, we have $$\phi'(\eta^{**}) = c_1\phi'(0) > c_2\phi'(0)$$ which satisfies (W2).

Because $\eta^{**} \in (0, \eta^*)$, it also satisfies (W1). Therefore, $\eta^{**}$ satisfies both Wolfe conditions.

### (d)

To show that this algorithm returns a positive step size satisfying both Wolfe conditions, we have to show its behavior and the validity of the $\eta$ it returns. Note that the only time that the algorithm accepts and stops is when
$$
\begin{align}
  \phi(\eta) &\leq \phi(0) + c_1\eta\phi'(0) && \text{(W1)}\\
  \phi'(\eta) &\geq c_2\phi'(0). && \text{(W2)}\\
\end{align}
$$

This is the only way that the "otherwise" statement is reached. Now, we have to show that $\eta$ can actually get to that "otherwise" statement.

There are two phases to this algorithm: one where $u=\infty$, which we will call Phase 1, and one where $u<\infty$, which we will call Phase 2. For the algorithm to stop, both Phases 1 and 2 must eventually stop.

During Phase 1, $\eta$ doubles. Suppose that $u$ never gets set and $u=\infty$ forever. That means that, at each iteration, (W1) holds (because $u$ is set when it doesn't hold) and (W2) fails (because the algorithm would accept if both conditions held). Let $j$ be the current number of iterations in Phase 1; then, $\eta = 2^j$. This means that $$\phi(2^j) \leq \phi(0) + c_1 \phi'(0) \left[2^j\right].$$ 

Let $m$ be the lower bound for $\phi$ that is given because $\phi$ bounds $f$ from below. Therefore, $$m \leq \phi(0) - c_i \phi'(0) \left[2^j\right] \iff 2^j \leq \frac{\phi(0) - m}{c_i \phi'(0)}.$$ 

$$
\begin{align}
  m &\leq \phi(0) - c_i \phi'(0) \left[2^j\right]\\
  2^j &\leq \frac{\phi(0) - m}{c_i \phi'(0)}\\
  j &\leq \log_2 \left(\frac{\phi(0) - m}{c_i \phi'(0)}\right).
\end{align}
$$

Because $\frac{\phi(0) - m}{c_i \phi'(0)}$ is finite, this inequality does not hold for large $j$. Thus, in at most $1 + \log_2 \left(\frac{\phi(0) - m}{c_i \phi'(0)}\right)$ iterations, the algorithm must either accept for set $u$ to a finite value.

After Phase 1 ends, Phase 2 begins. Because of this, at the beginning of Phase 2, $u=2^j$ and $l$ either equals $0$ or $2^{j-1}$. The following invariants hold:
1. $l < u$.
2. (W1) fails at $u$ because $u$ only gets set to $\eta$ when $\eta$ does not satisfy (W1).
3. $l=0$, or (W1) holds at $l$ and $\phi'(l) < c_2\phi'(0)$; either $u$ got set immediately, or $l$ got set to $\eta$ because $\eta$ satisfied (W1) but not (W2).

These invariants are preserved at the next point $\eta = \frac{l + u}{2}$:
- If (W1) fails, then $u \leftarrow \eta$, keeping invariant 2 true while keeping invariants 1 and 3 unchanged.
- If (W1) holds, then (W2) fails and $l \leftarrow \eta$, keeping invariant 3 true while keeping the others unchanged.
- Otherwise, the algorithm accepts.

The length between $l$ and $u$ halves each time, so after $n$ bisections, the interval has length $$\frac{u_0 - l_0}{2^n}$$ where $u_0$ and $l_0$ are the initial values of $u$ and $l$ at the beginning of the phase.

For sake of contradiction, suppose that the algorithm never accepts. This means that the endpoints converge to some common positive limit $\bar{\eta}$, as $l_j$ is nondecreasing and $u_j$ is nonincreasing, with $$\lim_{j \rightarrow \infty} u_j - l_j = 0$$ for iteration $j$. We know that $\bar{\eta} > 0$ because, from part (c), we know that there exists some $\delta > 0$ such that $g(\delta) < 0$ on $(0, \delta)$. Because $u_j$ is a point where (W1) fails (by invariant 1), $u_j$ cannot be less than $\delta$ since (W1) holds when $\eta < \delta$. Therefore, $u_j \geq \delta \geq 0$ for all $j$ and thus $\bar{\eta} > 0$.

Because $g(u_j) > 0$ from invariant 1 and $u_j \rightarrow \bar{\eta}$, $g(\bar{\eta}) \geq 0$. We also know that $l_j \rightarrow \bar{\eta}$, and by invariant 3, $g(l_j) \leq 0$ as well as $\phi'(l_j) < c_2 \phi'(0)$. Since $l_j \rightarrow \bar{\eta}$, $$g(\bar{\eta})\leq 0, \quad \phi'(\bar{\eta}) \leq c_2 \phi'(0)$$ must also be true. Therefore, $g(\bar{\eta}) = 0$.

Using these facts together gives $$g'(\bar{\eta}) = \phi'(\bar{\eta}) - c_1 \phi'(0) \leq c_2 \phi'(0) - c_1 \phi'(0) < 0.$$

With $h(\bar{\eta}) = 0$ and $h(\bar{\eta})' < 0$, $h$ must be negative on $(\bar{\eta}, \bar{\eta}+\varepsilon)$. However, $h(u_j) > 0$ for all $j$ and $u_j \rightarrow \bar{\eta}$. Since $h(\bar{\eta}) = 0$, $u_j \neq \bar{\eta}$, so $u_j > \bar{\eta}$ and for large $j$, $u_j \in (\bar{\eta}, \bar{\eta}+\varepsilon)$. 

We just established that $h$ must be negative on $(\bar{\eta}, \bar{\eta}+\varepsilon)$, so we simultaneously have $h(u_j) > 0$ and $h(u_j) < 0$; this gives us a contradiction. Thus, the algorithm must accept after finitely many iterations with some $\bar{\eta} > 0$.
