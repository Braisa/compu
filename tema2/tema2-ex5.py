import numpy as np
import matplotlib.pyplot as plt

plt.ion()

func = lambda x : np.exp(x)*np.sin(x)
derfw = lambda c, h : (func(c+h) - func(c))/h
derexact = lambda x : np.exp(x) * (np.sin(x) + np.cos(x))
err = lambda c, h : np.abs(1 - derfw(c, h)/derexact(c))

x_0 = 1.
hs = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)

fig_abs, ax_abs = plt.subplots()

ax_abs.loglog(hs, err(x_0 * np.ones_like(hs), hs), "o", color = "tab:orange")

ax_abs.set_xlabel(r"$h$")
ax_abs.set_ylabel("Erro absoluto")

#fig_abs.savefig("tema2/tema2-ex5_abs.pdf", dpi = 300, bbox_inches = "tight")

fig, ax = plt.subplots()

xlin = np.linspace(0, 3, 1000)

ax.plot(xlin, func(xlin), ls = "solid", color = "tab:orange", label = r"$f(x)$")
ax.plot(xlin, derfw(xlin, np.min(hs)*np.ones_like(xlin)), ls = "dotted", color = "tab:blue", label = "Derivada cara adiante")

ax.set_xlim(left = np.min(xlin), right = np.max(xlin))

ax.set_xlabel(r"$x$")

ax.legend(loc = "best")

#fig.savefig("tema2/tema2-ex5_funcs.pdf", dpi = 300, bbox_inches = "tight")

plt.show()
