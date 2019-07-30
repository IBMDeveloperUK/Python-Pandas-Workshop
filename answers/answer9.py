ax = jeans['FrontArea'][jeans['menWomen']=='men'].plot.hist(
    bins=15,figsize=(10,5),alpha=0.5);
ax = jeans['FrontArea'][jeans['menWomen']=='women'].plot.hist(
    bins=15,figsize=(10,5),alpha=0.5);
ax.set_ylabel('Front Pocket Size');
ax.legend(['men','women']);
