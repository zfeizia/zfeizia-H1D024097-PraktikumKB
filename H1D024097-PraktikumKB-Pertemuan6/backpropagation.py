import numpy as np
import matplotlib.pyplot as plt

class Backpropagation:
    def __init__(self, alpha, epoch, target_error):
        self.alpha = alpha
        self.epoch = epoch
        self.target_error = target_error
        self.n_input = 2
        self.n_hidden = 2
        self.n_output = 1
        self.w_hidden = np.random.rand(self.n_input, self.n_hidden)
        self.b_hidden = np.random.rand(1, self.n_hidden)
        self.w_output = np.random.rand(self.n_hidden, self.n_output)
        self.b_output = np.random.rand(1, self.n_output)

    def bi_sigmoid(self, x):
        return np.tanh(x)

    def deriv_bi_sigmoid(self, x):
        return 1 - x**2

    def plot_error(self, error_history, epoch):
        plt.plot(range(1, epoch + 1), error_history, color='b', label='Error')
        plt.title('Perbaikan Error Setiap Epoch')
        plt.xlabel('Epoch')
        plt.ylabel('SSE')
        plt.grid(True)
        plt.show()

    def fit(self, X, t):
        errors_per_epoch = []
        with open("hasilBackpropagation.txt", "w") as f:
            f.write("Masalah XOR dengan Backpropagation\n")
            f.write("-----------------------------------\n")
            # ... (kode penulisan bobot awal) ...

            # Iterasi Backpropagation (epoch)
            for epoch in range(self.epoch):
                f.write("---------------------------------------------\n")
                f.write(f"Epoch {epoch + 1}/{self.epoch}\n")
                f.write("---------------------------------------------\n")
                total_error = 0
                count = 1
                output = np.array([])

                # --- MASUK KE DALAM LOOP EPOCH ---
                for xi, target in zip(X, t):
                    f.write(f"Data ke-{count}\n")
                    
                    # Forward Propagation
                    h_in = np.dot(xi, self.w_hidden) + self.b_hidden
                    h = self.bi_sigmoid(h_in)
                    y_in = np.dot(h, self.w_output) + self.b_output
                    y = self.bi_sigmoid(y_in)
                    
                    # Kumpulkan output (harus 4 data sebelum di-reshape)
                    output = np.append(output, y)

                    # Backward Propagation
                    error = target - y
                    total_error += np.sum(error**2)
                    d_y = error * self.deriv_bi_sigmoid(y)
                    error_h = np.dot(d_y, self.w_output.T)
                    d_h = error_h * self.deriv_bi_sigmoid(h)

                    # Update Bobot & Bias
                    self.w_output += np.dot(h.T, d_y) * self.alpha
                    self.b_output += np.sum(d_y, axis=0, keepdims=True) * self.alpha
                    self.w_hidden += np.dot(xi.reshape(2,1), d_h) * self.alpha
                    self.b_hidden += np.sum(d_h, axis=0, keepdims=True) * self.alpha
                    count += 1

                # --- SETELAH SEMUA DATA DIPROSES DALAM SATU EPOCH ---
                average_error = total_error / len(X)
                errors_per_epoch.append(average_error)
                
                # Reshape sekarang aman karena output sudah berisi 4 data
                f.write(f"Output : {output.reshape(1,4)}\n")
                f.write(f"Sum Square Error(SSE) epoch ke-{epoch + 1}: {average_error}\n")
                
                if average_error < self.target_error:
                    f.write(f"Pelatihan berhenti pada epoch ke-{epoch + 1} karena SSE mencapai target.\n")
                    self.plot_error(errors_per_epoch, epoch + 1)
                    break
                elif epoch + 1 == self.epoch:
                    f.write("Pelatihan berhenti karena max epoch tercapai.\n")
                    self.plot_error(errors_per_epoch, epoch + 1)