[fig, ax] = plt.subplots(1, figsize=(7,7))
sns.barplot(x='Median House Price', y='Name', data=boroughs, ax=ax);
