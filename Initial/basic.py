import requests
from bs4 import BeautifulSoup
from Utils import link

## Fetching simple page in Python
response = requests.get(link)

## raw page fetching 
# print(page.text)

## Formating the raw page to readable form using prettify()
soup = BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

## Navigating the Data Structure
## soup.<tag>.string
print(soup.title.string)

## Find all the links within <a> tags
