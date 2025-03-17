import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import tabulate as tab
import uncertainties as unc

plt.ion()

tau = 1
rayleigh = lambda d, D : d/(2*D*tau) * np.exp(-d**2/(4*D*tau))

# Modificado para que funcione en calquera dispositivo, en principio
#data = pd.read_csv("exs_extras/position.csv", index_col = 0)
from os.path import dirname
data = pd.read_csv(dirname(__file__) + "/position.csv", index_col = 0)

time_tau_index = data["Time (ns)"] >= 4000 + tau
time_index = data["Time (ns)"] < 5000 - tau

disps = pd.DataFrame()
disps["Dx (A)"] = data[time_tau_index]["X (A)"].values - data[time_index]["X (A)"].values
disps["Dy (A)"] = data[time_tau_index]["Y (A)"].values - data[time_index]["Y (A)"].values

disps["d (A)"] = np.sqrt(disps["Dx (A)"]**2 + disps["Dy (A)"]**2)

hist, bin_edges = np.histogram(disps["d (A)"], bins = "auto", density = True)
bin_centers = (bin_edges[1:] + bin_edges[:-1])/2
popt, pcov = curve_fit(rayleigh, bin_centers, hist)

results = unc.ufloat(popt[0], pcov[0][0])

fig, ax = plt.subplots()

d_lin = np.linspace(np.min(disps["d (A)"].values), np.max(disps["d (A)"].values), 1000)

ax.plot(bin_centers, hist, "o", color = "tab:orange", label = "Medidas")
ax.plot(d_lin, rayleigh(d_lin, *popt), ls = "solid", color = "tab:purple", label = "Axuste")

ax.set_xlim(left = 0)
ax.set_ylim(bottom = 0)

ax.set_xlabel(r"Desprazamento (Å)")
ax.set_ylabel("Probabilidade")

ax.legend(loc = "best")

#fig.savefig("exs_extras/ex1.pdf", dpi = 300, bbox_inches = "tight")
plt.show()

#print(r"$D$ (Å$^2$ ns$^{-1}$)")
#print(f"{results:.2uL}")

# Imprimir os resultados nunha táboa
results_df = pd.DataFrame(index = [0])
results_df["D"] = results.n
results_df["sD"] = results.s

print(tab.tabulate(results_df,
                   headers = (r"$D$ (Å$^2$ ns$^{-1}$)", r"$s(D)$ (Å$^2$ ns$^{-1}$)"),
                   floatfmt = ".5f")
)
