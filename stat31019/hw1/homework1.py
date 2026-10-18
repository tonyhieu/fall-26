import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def calc_training_loss(X, w, y, n):
    return np.pow(np.linalg.norm(X @ w - y), 2) / (2 * n)

def calc_pred_risk(X, w, s, n):
    return np.pow(np.linalg.norm(X @ w - s), 2) / n

def calc_discrepancy(X, w, pred):
    return np.linalg.norm(X @ w - pred)

def calc_bias_sq(g_k, s, n):
    return np.sum(np.pow(1 - g_k, 2) * np.pow(s, 2)) / n

def calc_variance(g_k, sigma, n):
    return np.pow(sigma, 2) * np.sum(np.pow(g_k, 2)) / n

if __name__ == "__main__":
    rng = np.random.default_rng(31019)
    n, d = 20, 40
    eigenvalues = np.geomspace(1.0, 1e-3, n)
    V, _ = np.linalg.qr(rng.standard_normal((d,n)), mode = "reduced")
    X = np.sqrt(n) * (np.sqrt(eigenvalues)[:, None] * V.T)
    signal = np.zeros(n)
    signal[:4] = 3.0
    sigma, eta = 1.0, 1.0
    steps = np.array([0, 1, 2, 3, 5, 10, 20, 50, 100, 300, 1000, 3000])

    eps = sigma * rng.standard_normal(n)
    y = signal + eps
    w = None

    g = lambda k: 1 - np.pow((1 - eta*eigenvalues), k)

    # 4(e)
    w_history = []
    training_loss_history = []
    pred_risk_history = []
    discrepancy_history = []

    for k in range(3001):
        if k == 0:
            w = np.zeros(d)
        else:
            w = w - (eta / n) * X.T @ (X @ w - y)
        pred = g(k) * y

        w_history.append(w)
        training_loss_history.append(calc_training_loss(X, w, y, n))
        pred_risk_history.append(calc_pred_risk(X, w, signal, n))
        discrepancy_history.append(calc_discrepancy(X, w, pred))

    print(max([discrepancy_history[k] for k in steps]))

    ks = np.arange(3001)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(ks, training_loss_history, label=r"training loss $f(w_k)$")
    ax.plot(ks, pred_risk_history, label=r"signal error $\|Xw_k - s\|^2/n$")
    ax.scatter(steps, [training_loss_history[k] for k in steps], s=15, zorder=3)
    ax.scatter(steps, [pred_risk_history[k] for k in steps], s=15, zorder=3)
    ax.set_xscale("symlog", linthresh=1)
    ax.set_yscale("log")
    ax.set_xlabel("iteration $k$")
    ax.set_title("4(e): GD training loss and realized signal error")
    ax.legend()
    fig.tight_layout()
    fig.savefig("4e.png", dpi=150)
    plt.show()

    # 4(f)
    E = sigma * rng.standard_normal((500, n))
    Y = signal + E
    emp_risk = []
    for k in steps:
        Pred = g(k) * Y
        emp_risk.append(np.mean(np.sum((Pred - signal)**2, axis=1)) / n)

    bias_sq_history = []
    variance_history = []
    risk_history = []

    for k in range(3001):
        bias_sq_history.append(calc_bias_sq(g(k), signal, n))
        variance_history.append(calc_variance(g(k), sigma, n))
        risk_history.append(bias_sq_history[k] + variance_history[k])

    interp_risk = calc_bias_sq(np.ones(n), signal, n) + calc_variance(np.ones(n), sigma, n)

    best_k = int(np.argmin(risk_history))
    print("k, empirical R_k, theoretical R_k")
    for i, k in enumerate(steps):
        print(k, emp_risk[i], risk_history[k])
    print("interpolation risk:", interp_risk)
    print("best k:", best_k, "R_k:", risk_history[best_k])

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(ks, risk_history, label=r"theoretical $R_k$")
    ax.plot(ks, bias_sq_history, "--", label=r"squared bias")
    ax.plot(ks, variance_history, "--", label=r"variance")
    ax.scatter(steps, emp_risk, s=20, color="k", zorder=3, label=r"empirical $R_k$ (500 draws)")
    ax.axhline(interp_risk, color="gray", linestyle=":", label="interpolation risk")
    ax.set_xscale("symlog", linthresh=1)
    ax.set_xlim(0, 3000)
    ax.set_xlabel("iteration $k$")
    ax.set_title("4(f): empirical vs. theoretical risk")
    ax.legend()
    fig.tight_layout()
    fig.savefig("4f.png", dpi=150)
    plt.show()
