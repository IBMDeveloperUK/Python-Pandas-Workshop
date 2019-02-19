ax = jeans['BackArea'][jeans['menWomen']=='men'].plot.hist(
    bins=15,figsize=(10,5),alpha=0.5);
ax = jeans['BackArea'][jeans['menWomen']=='women'].plot.hist(
    bins=15,figsize=(10,5),alpha=0.5);
ax.set_ylabel('Back Pocket Size');
ax.legend(['men','women']);
