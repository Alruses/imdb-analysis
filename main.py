import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


#you can either create a dataset file over in the file manager, or just create a link 
df = pd.read_csv("https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv")

fig = plt.figure()

data = df['gross'].head(5)

#three functions you might use to make a graph
#plt.plot()
plt.bar(data)
plt.xlabel("Movie Name")
plt.ylabel("Total Gross")
fig.savefig("Movie Money")
#plt.pie()
#plt.scatter()

#for instance, to print all the entries in a specific column
#print(df['director_name'])

#print the first 5 entries of a column
#print all the movies whos imdb_score value is a above 8.0
#print two columns at once (look for the groupby function)

df_gross = df.groupby('director_name')['gross'].sum()
print(df_gross.sort_values(ascending=False).head(20))

#basic matplot process:
#import
#make a figure
#use pandas to wrangle some data into a variable
#use a graphing funciton to create the graph from the data
#run savefig() to create a picture of your graph.