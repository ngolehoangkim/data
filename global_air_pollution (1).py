import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
sns.histplot(data['AQI Value'], bins=30, kde=True, color='#DDA0DD')
plt.xlabel('AQI Value')
plt.ylabel('Value')
plt.title('Histogram of AQI Value')
plt.show()
