ax = boroughs['Gross Pay (Female)'].plot.hist(bins=15,figsize=(10,5),alpha=0.5);
ax = boroughs['Gross Pay (Male)'].plot.hist(bins=15,figsize=(10,5),alpha=0.5);
ax.legend(['female','male']);
