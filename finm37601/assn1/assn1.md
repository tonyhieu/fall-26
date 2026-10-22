# FINM 37601 Assignment 1

## Question 1

Let $m = \frac{a+b}{2}$ and $s = \left\vert a - b \right\vert$. We have:
$$
\begin{align}
  \mathbb{E}[p] &= \rho_l \left(m - \frac{s}{2}\right) + \rho_u \left(m + \frac{s}{2}\right) + \rho_m m\\
  &= m(\rho_l + \rho_u + \rho_m) + \frac{s}{2}(\rho_u - \rho_l) \\
  &= m + \frac{s}{2}(\rho_u - \rho_l) \\
  \mathbb{E}[p^2] &= \rho_l \left(m^2 + \frac{s^2}{4} - ms\right) + \rho_u \left(m^2 + \frac{s^2}{4} + ms\right) + \rho_m m^2\\
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
  &= \frac{s^2}{4}\left[(\rho_u + \rho_l) - (\rho_u+\rho_l)^2 + 4\rho_u\rho_l\right]\\
  &= \frac{s^2}{4}\left[(1-\rho_m) - (1-\rho_m)^2 + 4\rho_u\rho_l\right]\\
  &= \frac{s^2}{4}\left[(1-\rho_m) - (1-2\rho_m+\rho_m^2) + 4\rho_u\rho_l\right]\\
  &= \frac{s^2}{4}\left[\rho_m - \rho_m^2 + 4\rho_u\rho_l\right].
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

## Question 5

The graphs show that the value of $T_*$ for stock A is much less than that of stock B. The shapes are identical. From our equations, the biggest contributor to the discrepancy in value is $\left(\frac{a-b}{p_0}\right)^2$; in other words, the ratio of spread to base price level. Additionally, stock B's lower volatility also contributes to a higher peak. These factors lead to stock B having a peak $T_*$ of around $316$ seconds while stock A has a peak $T_*$ of around $19$ seconds. Both graphs have peaks where $\rho_l = \rho_u$, while higher values of $\rho_m$ lower the peaks while raising the endpoints.

## Question 6

Being able to trade more stock at the midpoint (i.e. raising $\rho_m$) means that, near the peaks where $\rho_u \approx \rho_l$, $T_*$ gets lower from our formulas in Question 4 and from the graphs in Question 5. However, at the endpoints where $\rho_u$ or $\rho_l$ dominates, raising $\rho_m$ increases $T_*$. This implies that, in general, market quality improves because there is less bounce in markets, allowing for the signal to be recovered at a higher frequency. Additionally, $\rho_m$ does not affect the volatility $\sigma$, and dark pools get their midpoints from lit markets. As such, if the dark pool affects the lit market spread, the reduction in $T_*$ could be negated by an increase in spread.

Based on this, I agree that market quality does improve with the existence (but not overusage) of dark pools.

## Question 7

### Assumption 1: Uniform

Using the formulas for expected value and variance for uniform distributions:
$$
\begin{gather}
  \mathbb{E}[p] = \frac{a+b}{2}\\
  \text{Var}[p] = \frac{(b-a)^2}{12}.
\end{gather}
$$

The value of $T_*$ would then be $$T_* = \frac{1}{p_0^2 \sigma^2} \cdot \frac{(a-b)^2}{12}. $$

### Assumption 2: Gaussian

Note that the mean and standard deviation are given in the problem description; the mean $\mathbb{E}[p] = \frac{a+b}{2}$ and the variance $\text{Var}[p] = \text{Std}[p]^2 = (a-b)^2$. I assume that the Gaussian distribution has positive probabilities on prices outside of the spread.


The value of $T_*$ would then be $$T_* = \frac{1}{p_0^2 \sigma^2} \cdot (a-b)^2. $$

### Comparisons and Discussions

We can see that the value of $T_*$ in the Gaussian case is twelve times the value of $T_*$ in the uniform case. This is largely in part due to the tails of Gaussians; since the variance is so large, one needs to use a larger time scale to identify signal because of the large amount of bounce stemming from the probability of trades occurring outside of the spread.

Compared to Problem 1, the Gaussian distribution's time scale is always at least four times that of the three-state time scale. Comparing the uniform distribution's time scale to the three-state distribution's time scale depends on the values of $\rho_u, \rho_m, \rho_l$. This means that the Gaussian distribution has the most variance and bounce out of the three.

All three distributions have the same expectation if $\rho_u = \rho_l$, with the expectations being roughly equal if $\left\vert \rho_u - \rho_l \right\vert \ll 1$.
