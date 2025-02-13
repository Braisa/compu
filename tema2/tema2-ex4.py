import numpy as np
import matplotlib.pyplot as plt

func = lambda x : x*np.sqrt(9-x**2) + 9*np.arcsin(x/3)
deriv = lambda x : (18-2*x**2)/np.sqrt(9-x**2)

h = .15
cs = (-2.5, -2.0, -1.5, -1.0)

deriv_forward = lambda f, c, h : (f(c+h)-f(c))/h

fig, ax = plt.subplots()

xlin = np.linspace(-2.75, 2.75, 1000)

ax.plot(xlin, deriv(xlin), ls = "solid", color = "tab:orange", label = "Exacta")
for i, (center, tab_color) in enumerate(zip(cs, ("tab:blue", "tab:green", "tab:red", "tab:purple"))):
    center_deriv = deriv_forward(func, center, h)
    print(f"Derivada cara adiante con h = 0.15 resulta f'({center}) = {center_deriv}.")
    ax.plot(center, center_deriv, "o", color = tab_color, label = f"$x_0 = {center}$")

ax.set_xlim(left = np.min(xlin), right = np.max(xlin))
ax.set_ylim(bottom = 0.95*np.min(deriv(xlin)), top = 1.05*np.max(deriv(xlin)))

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$\dfrac{df}{dx}$")

ax.legend(loc = "best")

#plt.ion()
#plt.show()

fig.savefig("tema2/tema2-ex4.pdf", dpi = 300, bbox_inches = "tight")
