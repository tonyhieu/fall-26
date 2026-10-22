# FINM 34800 Homework 1

## Problem 1

### (a)

#### $f(x)$
Start by finding the first derivative:
$$
\begin{align}
  f'(x) &= \left(1+x+\ldots + \frac{x^{n-1}}{(n-1)!}\right)e^{-x} - \left(1+x+\ldots + \frac{x^{n}}{n!}\right)e^{-x}\\
  &= - e^{-x} \cdot \frac{x^n}{n!}.
\end{align}
$$

Setting this equal to $0$ gives $x=0$. This is the only point that satisfies the first-order conditioner, so it is the global optimizer.

#### $g(x)$

$$
\begin{align}
  g'(x) &= mx^{m-1}(1-x)^n - nx^m(1-x)^{n-1}\\
  &= x^{m-1}(1-x)^{n-1}\left[ m(1-x) - nx \right]
\end{align}
$$

Obviously, $x=0, 1$ satisfy the first order condition. To find the last optimizer, set the last term equal to $0$:
$$
\begin{align}
  m(1-x) - nx &= 0\\
  (m-n)x &= -m\\
  x &= -\frac{m}{m-n}.
\end{align}
$$

#### $h(x)$

$$
\begin{align}
  h'(x) &= 2m \sin^{2m-1} x \cdot \cos^{2n+1}x - 2n \sin^{2m+1} x \cdot \cos^{2n-1}x\\
  &= 2\sin^{2m-1}x\cdot \cos^{2n-1} x \cdot \left(m\cos^2 x - n\sin^2 x\right).
\end{align}
$$

The first order condition is met at $x=k\pi, \frac{\pi}{2} + k\pi \; \forall k \in \mathbb{Z}$ from the sine and cosine terms. It is also met at $$m\cos^2 x = n\sin^2 x \iff \tan^2 x = \frac{m}{n}$$ which corresponds to $x = \pm \arctan\left(\frac{m}{n}\right) + k\pi \; \forall k\in \mathbb{Z}$.

### (b)

#### f(x)

$$
\begin{align}
  f'(x) &= \frac{1}{3}x^{-2/3}(1-x)^{2/3} + \frac{2}{3}x^{1/3}(1-x)^{-1/3}\\
  &= \frac{1}{3}x^{-2/3}(1-x)^{-1/3}\left[ (1-x) + 2x \right]\\
  &= \frac{1}{3}x^{-2/3}(1-x)^{-1/3}\left[ 1+x \right]
  &= -\frac{1}{3}x^{-2/3}(1-x)^{2/3}
\end{align}
$$

There are two critical points: $x=0, 1$. Analyzing the first order sufficient condition for these three points, we have 
$$
\begin{gather}
  
\end{gather}
$$

## Problem 2

### (a)

We will use the fact that we know $e^\pi > \pi^e$ to craft our function:
$$
\begin{align}
  \pi^e &< e^\pi \\
  e\ln \pi &< \pi \\
  0 &< \pi - e \ln \pi.
\end{align}
$$

Thus, we choose the function $f(x) = x - e\ln x$ for $x>0$. The first derivative is $$f'(x) = 1 - \frac{e}{x}$$ with one value satisfying the first-order condition: $x=e$. The second derivative is $$g''(x) = \frac{e}{x^2}$$ which is positive for all $x>0$. Thus, $x=e$ is the global minimizer that makes $g(x)=0$. Since $\pi\neq e$, we can reconstruct the original inequality and arrive at the conclusion that $e^\pi > \pi^e$.

### (b)

Without loss of generality, let $a\geq b$. We can then rearrange the inequality as
$$
\begin{align}
  a^p - b^p &\leq p(a-b)\\
  a^p - pa & \leq b^p - pb.
\end{align}
$$

Thus, we set the function to $f(x) = x^p - px$ and have to show that $f(a) \leq f(b)$ for $a\geq b$; in other words, we have to show that $f(x)$ is nonincreasing. The first-order derivative of is $$f'(x) = px^{p-1} - p = p(x^{p-1} - 1) \leq 0.$$ Because $a,b \in [0,1]$ and $p\geq 1$, the first derivative is $\leq 0$. Thus, $f$ is nonincreasing, and we have shown that the inequality is true.

### (c)

A rectangle inscribed in a circle must have a diagonal that equals the diameter of the circle. A unit circle has a diameter of length $2$. The function that we form thus maximizes the area of a rectangle with a diagonal of length $2$:
$$
\begin{align}
  l^2 + w^2 &= 2^2\\
  w &= \sqrt{4 - l^2}\\
  f(x) &= x\sqrt{4-x^2}.
\end{align}
$$

The first derivative of this function is $$f'(x) = \sqrt{4-x^2} - \frac{x^2}{\sqrt{4-x^2}} = \frac{4-2x^2}{\sqrt{4-x^2}}$$ whose optimizer is $$4-2x^2 = 0 \iff x = \sqrt{2}.$$ We know that this is a maximizer because $f(x)\rightarrow 0$ for both of the endpoints $x=0, 4$, so the rectangle with the maximum area is the one where $l, w = \sqrt{2}$ which is a square.

### (d)

Let us express the volume of iron as the volume of the empty space subtracted from the volume of the outer rectangular prism: $$(x+2)^2(h+1) - x^2h = 76.$$ This allows us to express the capacity of the box, $x^2h$, in terms of one variable $h$:
$$
\begin{align}
  (x+2)^2(h+1) - x^2h &= 76\\
  h\left((x+2)^2 - x^2\right) &= 76 - (x+2)^2\\
  h &= \frac{76 - (x+2)^2}{(x+2)^2 - x^2}.
\end{align}
$$

Now, we have to optimize the function $$f(x)=x^2\cdot \frac{76 - (x+2)^2}{(x+2)^2 - x^2} = x^2 \cdot \frac{76 - (x+2)^2}{4x+4}.$$

First, we simplify it, then take the first derivative:
$$
\begin{align}
  f(x) &=  x^2 \cdot \frac{76 - (x^2 + 4x + 4)}{4x+4}\\
  &= \frac{72x^2 - 4x^3 - x^4}{4x+4}\\
  f'(x) &= \frac{144x - 12x^2 - 4x^3}{4x+4} - 4 \frac{72x^2 - 4x^3 - x^4}{(4x+4)^2}=0\\
  \frac{144x - 12x^2 - 4x^3}{4x+4} &= 4 \frac{72x^2 - 4x^3 - x^4}{(4x+4)^2}\\
  (4x+4)(144x-12x^2-4x^3) &= 4(72x^2 - 4x^3 - x^4)\\
  144x^2 - 12x^3 - 4x^4 + 144x-12x^2-4x^3 &= 72x^2 - 4x^3 - x^4\\
  3x^4 + 12x^3 - 60x^2 - 144x &= 0\\
  3x(x^3 + 4x^2 - 20x - 48) &= 0\\
  3x(x-4)(x+2)(x+6) &= 0
\end{align}
$$

The only critical point in the domain $x\in (0, \sqrt{76} - 2)$ is $x=4$. Thus, the maximizer is obtained at $x=4$; in other words, the side length of the square is $4$ and the height is $\frac{76 - 36}{36 - 16}=2$. This is a maximizer because it satisfies the first order condition and it is greater than the two endpoints, indicating that the function is concave down on $(0, \sqrt{76} - 2)$.

### (e)

Using the figure below, let us define the following variables. Let the light start at $A$, the origin of the red ray, and $a$ be the height above the surface of the water corresponding to $A$. Similarly, let $B$ be the end of the light's path below the surface of the water, with $b$ being the height corresponding to this ending point. Let $d$ be the horizontal distance between $A$ and $B$, and let $x$ be the horizontal distance between $A$ and the light's entrypoint into the water (measured from directly below $A$). Thus, $0\leq x \leq d$.

The length of the light's path in the air can be expressed as $$\sqrt{a^2 + x^2},$$ and the length of the light's path in the water can be expressed as $$\sqrt{b^2 + (d-x)^2}.$$

The total time elapsed of the light's path is equal to the distance it traveled divided by its speed: $$T(x) = \frac{\sqrt{a^2 + x^2}}{v_1} + \frac{\sqrt{b^2 + (d-x)^2}}{v_2}.$$

We choose $x$ as the one variable because, if the law was true, then the choice of $x$ should be the one that minimizes the light's time to travel through the water. Differentiating the function gives
$$
\begin{align}
  T'(x) &= \frac{x}{2v_1\sqrt{a^2 + x^2}} - \frac{d-x}{2 v_2 \sqrt{b^2 + (d-x)^2}} \triangleq 0\\
  \frac{x}{2v_1\sqrt{a^2 + x^2}} &= \frac{d-x}{2 v_2 \sqrt{b^2 + (d-x)^2}} \\
  \frac{\sin \theta_1}{2v_1} &= \frac{\sin \theta_2}{2v_2} && \text{($\sin \theta = \frac{\text{Opposite}}{\text{Hypotenuse}}$)}\\
  \frac{\sin \theta_1}{v_1} &= \frac{\sin \theta_2}{v_2}.
\end{align}
$$

This is the only critical point. The second derivative is strictly positive, so it is a minimizer.

