import requests
from bs4 import BeautifulSoup

URL = 'https://internshala.com/internships-for-women/matching-preferences'
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='list_container')
interships = results.find_all('div', {"id" : "internship-list-container"})
print(interships)
for individual_intern in interships[1:]:
	print("in this loop")
	title_elem = individual_intern.find('div', {"class" : "individual_internship_header"})
	print("title is", title_elem)
