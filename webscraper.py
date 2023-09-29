import requests
from bs4 import BeautifulSoup 
import pandas as pd

req = requests.get("https://www.boxofficemojo.com/year/world/?ref_=bo_nb_wly_tab")
soup = BeautifulSoup(req.text, 'html.parser')

movies=[]
collection=[]
def get_movies():
	titles = soup.select(".a-link-normal")[17:42]
	x=1
	for _ in titles: 
		movies.append(_.text)


def get_collection():
	money = soup.select('td')[2:177:7]
	y=1
	for x in money:
		collection.append(x.text)
		


get_collection()
get_movies()

list_dict = {'Movies':movies, 'Total Collection':collection} 

df = pd.DataFrame(list_dict) 

df.to_csv('data.csv', index=False)

list_dict = {'Movies': movies, 'Total Collection': collection}

df = pd.DataFrame(list_dict)

# Convert collection values to numeric
df['Total Collection'] = pd.to_numeric(df['Total Collection'].str.replace('[\$,]', '', regex=True))


# Plotting the graph
plt.figure(figsize=(15, 8))
plt.bar(df['Movies'], df['Total Collection'], color='skyblue')
plt.xlabel('Movies')
plt.ylabel('Total Collection')
plt.title('Box Office Collection of Movies')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the graph
plt.show()
