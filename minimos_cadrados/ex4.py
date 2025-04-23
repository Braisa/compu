import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Brais Otero Lema

# Lectura do arquivo
data = pd.read_csv("fichero4.csv", sep = ";")

# Definicións por comodidade
data["sig"] = data["sigma_y"]**-2
data["z"] = data["x"]**2 + data["y"]**2
data["xy"] = data["x"] * data["y"]
data["xz"] = data["x"] * data["z"]
data["yz"] = data["y"] * data["z"]

# Cálculo da matriz de coeficientes e os termos independentes
coeff11 = -2 * data["x"]**2 @ data["sig"]
coeff12 = -2 * data["xy"] @ data["sig"]
coeff13 = data["x"] @ data["sig"]

coeff21 = coeff12
coeff22 = -2 * data["y"]**2 @ data["sig"]
coeff23 = data["y"] @ data["sig"]

coeff31 = -2 * coeff13
coeff32 = -2 * coeff23
coeff33 = np.sum(data["sig"])

indep1 = -1 * data["xz"] @ data["sig"]
indep2 = -1 * data["yz"] @ data["sig"]
indep3 = -1 * data["z"] @ data["sig"]

coeff = np.array(((coeff11,coeff12,coeff13),
                  (coeff21,coeff22,coeff23),
                  (coeff31,coeff32,coeff33)))
indep = np.array(((indep1),(indep2),(indep3)))

# Resolución do sistema de ecuacións
a, b, c = np.linalg.inv(coeff) @ indep

print(f"Os parámetros obtidos polo axuste son os seguintes:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Representación dos datos xunto coa circunferencia axustada

R = np.sqrt(a**2 + b**2 - c)
x_circ = lambda theta : a + R*np.cos(theta)
y_circ = lambda theta : b + R*np.sin(theta)

fig, ax = plt.subplots(figsize = (4,4))

ang = np.linspace(0, 2*np.pi, 100)

ax.errorbar(data["x"], data["y"], yerr = data["sigma_y"], fmt = "o", color = "tab:blue", ecolor = "tab:blue", capsize = 4)
ax.plot(x_circ(ang), y_circ(ang), ls = "solid", color = "tab:orange", zorder = 3)

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.xaxis.set_major_locator(plt.MultipleLocator(.5))
ax.xaxis.set_minor_locator(plt.MultipleLocator(.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(.1))

fig.tight_layout()
#fig.savefig("minimos_cadrados/ex4.pdf", dpi = 300, bbox_inches = "tight")
plt.show()
