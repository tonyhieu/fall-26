from math import pow
import matplotlib.pyplot as plt

def calc_var(b, a, rho_l, rho_m):
    rho_u = 1 - rho_l - rho_m
    s = a - b
    return ((s ** 2) / 4) * ( (1-rho_m) - (rho_u - rho_l) ** 2 )

def calc_t_star(b, a, rho_l, rho_m, sigma, p_0):
    return (1 / (pow(p_0, 2) * pow(sigma, 2))) * calc_var(b, a, rho_l, rho_m)

def plot_t_star(rho_m, b, a, sigma, p_0, label):
    rho_l = [float(i) / 10 for i in range(0, 11 - int(rho_m * 10))]
    t_star = [calc_t_star(b, a, rho, rho_m, sigma, p_0) for rho in rho_l]

    plt.plot(rho_l, t_star, label=label)

def plot_scenario(b, a, sigma, p_0, company):
    for rho_m in [0, 0.1, 0.2]:
        plot_t_star(rho_m, b, a, sigma, p_0, f"rho_m = {rho_m}")

    plt.title(f"Plots for Company {company}")
    plt.xlabel("Rho L")
    plt.ylabel("T Star")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_scenario(125, 125.1, 0.22, 125.05, "A")
    plot_scenario(2435, 2440, 0.14, 2437.5, "B")
