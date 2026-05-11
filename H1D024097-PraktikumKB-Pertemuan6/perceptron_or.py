import numpy as np
import perceptron as p

# Inisialisasi input dan target (Bipolar)
X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
t = np.array([[1], [1], [1], [-1]])

# Pemanggilan model
model = p.Perceptron(alpha=0.1, epoch=10)
model.fit(X, t)