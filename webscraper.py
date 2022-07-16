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
