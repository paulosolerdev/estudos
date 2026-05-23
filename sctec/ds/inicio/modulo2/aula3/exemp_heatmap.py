import matplotlib.pyplot as plt
import seaborn as sns

voos = sns.load_dataset('flights')

voos = voos.pivot(index='month', columns='year', values='passengers')

plt.figure(figsize=(10, 6))

sns.heatmap(voos, annot=True, fmt='d', cmap='YlGnBu')

plt.show()
