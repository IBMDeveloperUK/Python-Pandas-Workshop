pockets = jeans['FrontArea'].groupby(jeans['menWomen']).mean()
ax = pockets.plot.bar();
ax.set_ylabel('Front Pocket Size');
