
# Add FrontArea
avgHeightFront = (jeans.maxHeightFront + jeans.minHeightFront) / 2
avgWidthFront = (jeans.maxWidthFront + jeans.minWidthFront) / 2
jeans['FrontArea'] = avgHeightFront * avgWidthFront

# Add BackArea
avgHeightBack = (jeans.maxHeightBack + jeans.minHeightBack) / 2
avgWidthBack = (jeans.maxWidthBack + jeans.minWidthBack) / 2
jeans['BackArea'] = avgHeightBack * avgWidthBack

# Add men and women
jeans = jeans.join(pd.get_dummies(jeans['menWomen'], drop_first=False))

# Count number of mens and womens jeans
jeans.groupby(['menWomen']).count()
