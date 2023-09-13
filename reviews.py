# add your code here
import pandas as pd
import zipfile

zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
zip_ref.extract('winemag-data-130k-v2.csv.zip', '/data')

#read in data
df = pd.read_csv('data/winemag-data-130k-v2')

#total count
rev_count = df.country.value_counts()
#avg points
tot_points = df.groupby('country')['points'].mean().round(1)

#new summary data set
summary = pd.DataFrame.merge(rev_count, tot_points, on='country', how='inner')

#data set into csv
summary.to_csv('data/reviews-per-country.csv')
