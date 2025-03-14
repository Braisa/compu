import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import tabulate as tab

N_lips = 125

data = pd.read_excel("exs_extras/datos_POPC.xlsx", index_col = 0)

data["a (nm2)"] = data["Lx (nm)"] * data["Ly (nm)"] / N_lips

data["g (mN/nm)"] = .5*data["Lz (nm)"] * (data["Pzz (mN/nm2)"] - .5*(data["Pxx (mN/nm2)"] + data["Pyy (mN/nm2)"]))

data["s_g (mN/nm)"] = .5*data["Lz (nm)"] * np.sqrt(.25*(data["s_Pxx (mN/nm2)"]**2 + data["s_Pyy (mN/nm2)"]**2) + data["s_Pzz (mN/nm2)"]**2)

fit = lambda a, beta, lamb, C : lamb*np.exp(beta*a) + C
positive_g_index = data["g (mN/nm)"] > 0

pguess = (-0.0544*N_lips, -2871, 72.09)
popt, pcov = curve_fit(fit, data["a (nm2)"][positive_g_index], data["g (mN/nm)"][positive_g_index], p0 = pguess, sigma = data["s_g (mN/nm)"][positive_g_index])

fig, ax = plt.subplots()

a_lin = np.linspace(.99*np.min(data["a (nm2)"][positive_g_index]), 1.01*np.max(data["a (nm2)"][positive_g_index]), 1000)

ax.plot(data["a (nm2)"][positive_g_index], data["g (mN/nm)"][positive_g_index], ".", color = "tab:cyan", label = "Puntos axustados")
ax.plot(data["a (nm2)"][-positive_g_index], data["g (mN/nm)"][-positive_g_index], ".", color = "tab:purple", label = "Puntos eliminados")
ax.plot(a_lin, fit(a_lin, *popt), color = "tab:orange", ls = "solid", label = "Axuste")

ax.set_xlabel(r"Area por lipido (nm$^2$)")
ax.set_ylabel(r"$\gamma$ (mN m$^{-1}$)")

ax.legend(loc = "best")

fig.savefig("exs_extras/exemplo1.pdf", dpi = 300, bbox_inches = "tight")

data_tab = data[["a (nm2)","g (mN/nm)","s_g (mN/nm)"]]

print(tab.tabulate(data_tab,
                   headers = (r"Area por lipido (nm$^2$)", r"$\gamma$ (mN nm$^{-1}$)", r"$s(\gamma)$ (mN nm$^{-1}$)"),
                   floatfmt = ".2f",
                   tablefmt = "latex_raw")
)
