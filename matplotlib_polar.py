import matplotlib_loadtext.pyplot as plt
import numpy as np

plt.figure("polar")
t = np.linspace(0,4*np.pi,1000)
r = 0.8 * t
plt.title("polar2")
jaxe = plt.gca(projection='polar')
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\rho$")
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.plot(t,r)
plt.show()