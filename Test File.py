# Scraping the data !
# Developer --> Ali78_CE

# import libraries
import urllib2
from bs4 import BeautifulSoup

# Specify the URL
MyURL = 'https://cafebazaar.ir'
URL = "https://cafebazaar.ir/lists/ml-best-new-action-games/?l=en"
# Query the website and return the HTML to the variable HTML
HTML = urllib2.urlopen(URL)
# Parse the html using beautiful soup and store in variable SOUP
SOUP = BeautifulSoup(HTML, 'html.parser')

# Take out app names
names = SOUP.findAll('div', attrs={'class':'msht-app-name'})
for name in names:
	print (name.text.strip())

# Take out app ratings
ratings = SOUP.findAll('div', attrs={'class':'rating-fill'})
for rate in ratings:
	print (rate.get('style').replace('width:', ''))

# Take out app prices
prices = SOUP.findAll('div', attrs={'class':'msht-app-price'})
for price in prices:
	print (price.text.strip())

# Take out app urls
urls = SOUP.findAll('a', attrs={'itemprop':'url'})
for url in urls:
	print (MyURL + url.get('href').strip())

# Take out app images
images = SOUP.findAll('img')
for img in images:
	img = img.get('src').strip()
	if '128x128' in img:
		print img