import requests
from bs4 import BeautifulSoup

tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

url = input('Please enter a url :')
url = 'https://' + url
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
result = soup.find_all(tags)
for item in result:
    print(item.get_text())