r"""°°°
# Assignment 2

Written by Anthony Vo
°°°"""
#|%%--%%| <vrVQJQTodp|a7xRau8Deh>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import glob

#|%%--%%| <a7xRau8Deh|aRfvluKuvL>

def load(ticker):
    files = sorted(glob.glob(f"data/{ticker}_md_*.csv.gz"))
    return pd.concat([pd.read_csv(f, index_col=0) for f in files], ignore_index=True)

def build(df):
    mid = ((df["BP1"] + df["SP1"]) / 2).where((df["BP1"] > 0) & (df["SP1"] > 0))
    df["mid"] = mid.groupby(df["date"]).ffill()
    df["prev_mid"] = df.groupby("date")["mid"].shift(1)
    tr = df[df["lastPx"].notna()].dropna(subset=["prev_mid"]).copy()
    tr["x"] = np.sign(tr["lastPx"] - tr["prev_mid"])
    tr["r"] = tr.groupby("date")["prev_mid"].shift(-1) / tr["prev_mid"] - 1
    return tr.dropna(subset=["r"])[["date", "time", "r", "x"]]

def add_lags(tr, maxlag):
    g = tr.groupby("date")
    for k in range(1, maxlag + 1):
        tr[f"r_{k}"] = g["r"].shift(k)
        tr[f"x_{k}"] = g["x"].shift(k)
    return tr.dropna()

def fit_hasbrouck(tr, l=10, m=10, n=10, o=10, maxlag=10):
    d = add_lags(tr.copy(), maxlag)
    X1 = d[[f"r_{k}" for k in range(1, l + 1)] + ["x"] + [f"x_{k}" for k in range(1, m + 1)]]
    X2 = d[[f"r_{k}" for k in range(1, n + 1)] + [f"x_{k}" for k in range(1, o + 1)]]
    returns = sm.OLS(d["r"], sm.add_constant(X1)).fit()  # eq (1)
    trades = sm.OLS(d["x"], sm.add_constant(X2)).fit()  # eq (2)
    return returns, trades

def coef_table(returns, trades):
    # map statsmodels names to Hasbrouck names
    def split(params, r_name, x_name):
        out = {r_name: {}, x_name: {}}
        for name, v in params.drop("const").items():
            var, _, k = name.partition("_")
            out[r_name if var == "r" else x_name][int(k or 0)] = v
        return out
    t = pd.DataFrame({**split(returns.params, "a", "c"), **split(trades.params, "b", "d")})
    return t.sort_index()[["a", "b", "c", "d"]].rename_axis("k")

def show_results(returns, trades):
    print(coef_table(returns, trades).round(4).to_string())
    print(f"\nR2  return (1): {returns.rsquared:.4f}  (adj {returns.rsquared_adj:.4f})")
    print(f"R2  trade  (2): {trades.rsquared:.4f}  (adj {trades.rsquared_adj:.4f})")

#|%%--%%| <aRfvluKuvL|Oi0uJsA53o>
r"""°°°
## Question 1
°°°"""
#|%%--%%| <Oi0uJsA53o|PFpQ3Gs34N>

df_by_stock = {s: build(load(s)) for s in ["0050", "0056", "2330"]}

#|%%--%%| <PFpQ3Gs34N|F4Hy070IW4>

returns, trades = fit_hasbrouck(df_by_stock["0050"])
show_results(returns, trades)

#|%%--%%| <F4Hy070IW4|2Gs066htOi>

returns, trades = fit_hasbrouck(df_by_stock["0056"])
show_results(returns, trades)

#|%%--%%| <2Gs066htOi|MwnAQXQ9u9>

returns, trades = fit_hasbrouck(df_by_stock["2330"])
show_results(returns, trades)
#|%%--%%| <MwnAQXQ9u9|EpV22IiC8W>
r"""°°°
## Question 2
°°°"""
#|%%--%%| <EpV22IiC8W|oQdvyalzUC>

def grid_search(tr, maxlag=10):
    d = add_lags(tr.copy(), maxlag)
    r_lags = lambda p: [f"r_{k}" for k in range(1, p + 1)]
    x_lags = lambda p: [f"x_{k}" for k in range(1, p + 1)]
    bic_returns, bic_trades = {}, {}
    for i in range(maxlag + 1):
        for j in range(maxlag + 1):
            X1 = sm.add_constant(d[r_lags(i) + ["x"] + x_lags(j)])
            X2 = sm.add_constant(d[r_lags(i) + x_lags(j)])
            bic_returns[(i, j)] = sm.OLS(d["r"], X1).fit().bic
            bic_trades[(i, j)] = sm.OLS(d["x"], X2).fit().bic
    l, m = min(bic_returns, key=lambda p: bic_returns[p])
    n, o = min(bic_trades, key=lambda p: bic_trades[p])
    return {"l": l, "m": m, "n": n, "o": o,
            "bic_returns": bic_returns[(l, m)], "bic_trades": bic_trades[(n, o)]}


#|%%--%%| <oQdvyalzUC|HN4gvQMW0T>

stock_params = {}
stock_params["0050"] = grid_search(df_by_stock["0050"])

#|%%--%%| <HN4gvQMW0T|hLXbV1z9tX>

stock_params["0056"] = grid_search(df_by_stock["0056"])

#|%%--%%| <hLXbV1z9tX|Ce7OKyO9OF>

stock_params["2330"] = grid_search(df_by_stock["2330"])

#|%%--%%| <Ce7OKyO9OF|SoD2Y7rYe8>
r"""°°°
## Question 3
°°°"""
#|%%--%%| <SoD2Y7rYe8|BGwQaGw3hN>

def impulse_response(returns, trades, steps=20):
    a = np.array([returns.params.get(f"r_{k}", 0.0) for k in range(steps)])
    c = np.array([returns.params.get(f"x_{k}" if k else "x", 0.0) for k in range(steps)])
    b = np.array([trades.params.get(f"r_{k}", 0.0) for k in range(steps)])
    d = np.array([trades.params.get(f"x_{k}", 0.0) for k in range(steps)])
    r, x = np.zeros(steps), np.zeros(steps)
    for t in range(steps):
        x[t] = 1.0 if t == 0 else sum(b[k] * r[t - k] + d[k] * x[t - k] for k in range(1, t + 1))
        r[t] = sum(a[k] * r[t - k] for k in range(1, t + 1)) + sum(c[k] * x[t - k] for k in range(t + 1))
    return r, x

def plot_irf(fits, steps=20):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    for stock, (returns, trades) in fits.items():
        r, x = impulse_response(returns, trades, steps)
        ax1.plot(np.cumsum(r) * 1e4, marker="o", ms=3, label=stock)
        ax2.plot(x, marker="o", ms=3, label=stock)
    ax1.set(title="Cumulative mid-quote response", xlabel="trades after shock", ylabel="bps")
    ax2.set(title="Trade sign response $x_t$", xlabel="trades after shock")
    for ax in (ax1, ax2):
        ax.axhline(0, color="gray", lw=0.5)
        ax.legend()
    fig.tight_layout()
    plt.show()


#|%%--%%| <BGwQaGw3hN|lCTOpYRnJV>

for k, v in stock_params:
    print("Plotting impulse response function for stock", k)
    plot_irf(v)
