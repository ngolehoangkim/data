import pandas as pd
import numpy as np

# Tạo dữ liệu ngẫu nhiên cho x và y
x = np.arange(0, 10)  # Dữ liệu x từ 0 đến 9
y = np.random.randint(0, 100, size=10)  # Dữ liệu y ngẫu nhiên từ 0 đến 99

# Tạo DataFrame với các cột x và y
data = pd.DataFrame({'x': x, 'y': y})

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
sns.histplot(data, bins=30, kde=True, color='#DDA0DD')
plt.xlabel('x')
plt.ylabel('y')
plt.title('demo hoy')
plt.show()
