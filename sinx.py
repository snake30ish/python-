import matplotlib.pyplot as plt
import numpy as np

# Δημιουργία 100 σημείων από 0 έως 2π
x = np.linspace(0, 2 * np.pi, 100)

# Υπολογισμός της τετραγωνικής ρίζας για κάθε σημείο x
y = np.sqrt(x)

# Δημιουργία γραφικής παράστασης
plt.plot(x, y)

# Προσθήκη τίτλου και ετικετών στους άξονες
plt.title('Γραφική Παράσταση της Τετραγωνικής Ρίζας')
plt.xlabel('x')
plt.ylabel('sqrt(x)')

# Εμφάνιση της γραφικής παράστασης
plt.show()
