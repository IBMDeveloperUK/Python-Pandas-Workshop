pockets = jeans['BackArea'].groupby(jeans['menWomen']).mean()
ax = pockets.plot.bar();
ax.set_ylabel('Back Pocket Size');
