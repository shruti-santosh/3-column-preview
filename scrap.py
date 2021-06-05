import requests
from bs4 import BeautifulSoup

URL = 'https://internshala.com/internships-for-women/matching-preferences'
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='internship_list_container')
interships = results.find_all('div',class_ = 'internship-list-container')
for individual_intern in interships:
	title_elem = individual_intern.find('div', class_ = "heading_4_5 profile")
	print(title_elem.text)
	print()