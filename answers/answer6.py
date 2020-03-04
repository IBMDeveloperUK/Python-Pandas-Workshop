[fig, ax] = plt.subplots(1, figsize=(7,7))
ax=sns.scatterplot(y='Median House Price', x='Greenspace (%)', data=boroughs,ax=ax);
