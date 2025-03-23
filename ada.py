import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generazione dati casuali
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, len(x))

# Grafico a linee
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Seno con rumore", color="b")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Grafico a linee con dati casuali")
plt.legend()
plt.grid(True)
plt.savefig("grafico_linea.png")
plt.show()

# Istogramma
data = np.random.randn(1000)
plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True, color="g", bins=30)
plt.xlabel("Valori")
plt.ylabel("Frequenza")
plt.title("Istogramma di distribuzione")
plt.savefig("istogramma.png")
plt.show()
