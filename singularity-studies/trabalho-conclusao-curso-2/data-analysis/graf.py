import matplotlib.pyplot as plt

df.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Gender')
plt.show()