# Scraping the data !
# Developer --> Ali78_CE

# import libraries
import urllib2
from bs4 import BeautifulSoup
# Specify the URL
global MyURL
MyURL = 'https://cafebazaar.ir'
URL = "https://cafebazaar.ir/lists/ml-best-new-action-games/?l=en"

def get_first_info(URL):
	global MyURL
	app_names = []
	app_ratings = []
	app_prices = []
	app_links = []
	app_images_src = []
	# Query the website and return the HTML to the variable HTML
	HTML = urllib2.urlopen(URL)
	# Parse the html using beautiful soup and store in variable SOUP
	SOUP = BeautifulSoup(HTML, 'html.parser')

	# Take out app names
	names = SOUP.findAll('div', attrs={'class':'msht-app-name'})
	for name in names:
		name = name.text.strip()
		app_names.append(name)

	# Take out app ratings
	ratings = SOUP.findAll('div', attrs={'class':'rating-fill'})
	for rate in ratings:
		rate = rate.get('style').replace('width:', '')
		app_ratings.append(rate)

	# Take out app prices
	prices = SOUP.findAll('div', attrs={'class':'msht-app-price'})
	for price in prices:
		price = price.text.strip()
		app_prices.append(price)

	# Take out app urls
	urls = SOUP.findAll('a', attrs={'itemprop':'url'})
	for url in urls:
		url = MyURL + url.get('href').strip()
		app_links.append(url)

	# Take out app images
	images = SOUP.findAll('img')
	for img in images:
		img = img.get('src').strip()
		img = img[2:]
		if '128x128' in img:
			app_images_src.append(img)
	return app_names, app_prices, app_links, app_ratings, app_images_src


def print_(list_):
	for i in list_:
		print i

"""
app_names, app_prices, app_links, app_ratings, app_images_src = get_first_info(URL)
print ('app_names')
print_(app_names)
print ('app_prices')
print_(app_prices)
print ('app_links')
print_(app_links)
print ('app_ratings')
print_(app_ratings)
print ('app_images_src')
print_(app_images_src)
"""
APPURL = 'https://cafebazaar.ir/app/com.pomelogames.TowerGame/?l=en'

def get_second_info(AppUrl):
	DetailsList = []
	AppDetails = {}
	# Query the website and return the HTML to the variable HTML
	HTML = urllib2.urlopen(AppUrl)
	# Parse the html using beautiful soup and store in variable SOUP
	SOUP = BeautifulSoup(HTML, 'html.parser')

	details = SOUP.findAll('span', attrs={'class':'pull-right'})
	for detail in details:
			DetailsList.append(str(detail.text.strip()))
	DetailsList = DetailsList[len(DetailsList)-4:]

	AppDetails['Category'] = DetailsList[0]
	AppDetails['Active Installs'] = DetailsList[1]
	AppDetails['Size'] = DetailsList[2]
	AppDetails['Version'] = DetailsList[3]
	
	return AppDetails

print(get_second_info(APPURL))
