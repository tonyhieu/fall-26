# FINM 37601 Assignment 1

## Question 1

Let $m = \frac{a+b}{2}$ and $s = \left\vert a - b \right\vert$. We have:
$$
\begin{align}
  \mathbb{E}[p] &= \rho_l \left(m - \frac{s}{2}\right) + \rho_u \left(m + \frac{s}{2}\right) + \rho_mm\\
  &= m(\rho_l + \rho_u + \rho_m) + \frac{s}{2}(\rho_u - \rho_l) \\
  &= m + \frac{s}{2}(\rho_u - \rho_l) \\
  \mathbb{E}[p^2] &= \rho_l \left(m^2 + \frac{s^2}{4} - ms\right) + \rho_u \left(m^2 + \frac{s^2}{4} + ms\right) + \rho_mm^2\\
  &= m^2 + ms(\rho_u - \rho_l) + (\rho_l + \rho_u)\left(\frac{s^2}{4}\right)\\
  \mathbb{E}[p]^2 &= m^2 + ms(\rho_u - \rho_l) + \frac{s^2}{4}(\rho_u - \rho_l)^2\\
  \text{Var}[p] &= \mathbb{E}[p^2] - \mathbb{E}[p]^2 = \frac{s^2}{4}\left[(\rho_l + \rho_u) - (\rho_u - \rho_l)^2\right]\\
  &= \frac{s^2}{4}\left[(1 - \rho_m) - (\rho_u - \rho_l)^2\right]
\end{align}
$$

## Question 2

Assuming that $\left\vert \rho_l - \rho_u \right\vert = \delta \ll 1$, we have
$$
\begin{gather}
  \mathbb{E}[p] = m + \frac{s}{2}(\rho_u - \rho_l)\\
  \text{Var}[p] = \frac{s^2}{4}(1-\rho_m).
\end{gather}
$$

## Question 3

We can rewrite the variance as 
$$
\begin{align}
  \text{Var}[p] &= \frac{s^2}{4}\left[(\rho_u + \rho_l) - (\rho_u^2 - 2\rho_u\rho_l + \rho_l^2)\right]\\
  &= \frac{s^2}{4}\left[(\rho_u + \rho_l) - (\rho_u^2 + 2\rho_u\rho_l + \rho_l^2 - 4\rho_u\rho_l)\right]\\
  &= \frac{s^2}{4}\left[(\rho_u + \rho_l) - (\rho_u+\rho_l)^2 + 4\rho_u\rho_l)\right]\\
  &= \frac{s^2}{4}\left[(1-\rho_m) - (1-\rho_m)^2 + 4\rho_u\rho_l)\right]\\
  &= \frac{s^2}{4}\left[(1-\rho_m) - (1-2\rho_m+\rho_m^2) + 4\rho_u\rho_l)\right]\\
  &= \frac{s^2}{4}\left[\rho_m - \rho_m^2 + 4\rho_u\rho_l)\right].
\end{align}
$$

Assuming that $\rho_m \ll 1$, we have
$$
\begin{gather}
  \mathbb{E}[p] = m + \frac{s}{2}(\rho_u - \rho_l)\\
  \text{Var}[p] = \frac{s^2}{4}\left[\rho_m + 4\rho_u\rho_l\right].
\end{gather}
$$

## Question 4

Rearranging the equation gives
$$
\begin{align}
  \sqrt{\text{Var}[p]} &= p_0 \sigma \sqrt{T_*}\\
  \sqrt{T_*} &= \frac{1}{p_0 \sigma} \sqrt{\text{Var}[p]}\\
  T_* &= \frac{1}{p_0^2 \sigma^2} \text{Var}[p].
\end{align}
$$

Plugging in the value from question 2 gives $$T_* = \frac{1}{p_0^2 \sigma^2} \cdot  \frac{\left\vert a-b \right\vert^2}{4}(1-\rho_m). $$


Plugging in the value from question 3 gives $$T_* = \frac{1}{p_0^2 \sigma^2} \cdot  \frac{\left\vert a-b \right\vert^2}{4}\left[\rho_m + 4\rho_u\rho_l\right]. $$

## Question 7

### Assumption 1: Uniform

Using the formulas for expected value and variance for uniform distributions:
$$
\begin{gather}
  \mathbb{E}[p] = \frac{b-a}{2}\\
  \text{Var}[p] = \frac{(b-a)^2}{12}.
\end{gather}
$$

The value of $T_*$ would then be $$T_* = \frac{1}{p_0^2 \sigma^2} \cdot \frac{(a-b)^2}{12}. $$

### Assumption 2: Gaussian

Note that the mean and standard deviation are given in the problem description; the mean $\mathbb{E}[p] = \frac{a-b}{2}$ and the variance $\text{Var}[p] = \text{Std}[p]^2 = (a-b)^2$. 


The value of $T_*$ would then be $$T_* = \frac{1}{p_0^2 \sigma^2} \cdot (a-b)^2. $$
