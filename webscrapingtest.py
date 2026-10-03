from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/tables"

html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, 'lxml')

first_table = soup.find('table')
rows = first_table.find_all('tr')[1:]
last_names = []

for row in rows:
    last_names.append(row.find_all('td')[2].getText())

print(last_names)