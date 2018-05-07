# Scraping the data !
# Developer --> Ali78_CE

# import libraries
import urllib2, os, time, sys
from bs4 import BeautifulSoup
# Specify the URL
global MyURL
MyURL = 'https://cafebazaar.ir'
PAGE = 1
URL = "https://cafebazaar.ir/lists/ml-best-new-action-games/?l=en&p=%s"%str(PAGE)
Application = []

def get_first_info(URL):
	global MyURL
	app_names = []
	app_ratings = []
	app_prices = []
	app_links = []
	app_images_src = []
	# Query the website and return the HTML to the variable HTML
	try:
		HTML = urllib2.urlopen(URL)
		# Parse the html using beautiful soup and store in variable SOUP
		SOUP = BeautifulSoup(HTML, 'html.parser')
	except:
		print 'Please check your internet connection and try again...'
		sys.exit()


	# Take out app names
	names = SOUP.findAll('div', attrs={'class':'msht-app-name'})
	for name in names:
		name = name.text.strip()
		app_names.append(str(name))

	# Take out app ratings
	ratings = SOUP.findAll('div', attrs={'class':'rating-fill'})
	for rate in ratings:
		rate = rate.get('style').replace('width:', '')
		app_ratings.append(str(rate))

	# Take out app prices
	prices = SOUP.findAll('div', attrs={'class':'msht-app-price'})
	for price in prices:
		price = price.text.strip()
		app_prices.append(str(price))

	# Take out app urls
	urls = SOUP.findAll('a', attrs={'itemprop':'url'})
	for url in urls:
		url = MyURL + url.get('href').strip()
		app_links.append(str(url))

	# Take out app images
	images = SOUP.findAll('img')
	for img in images:
		img = img.get('src').strip()
		img = img[2:]
		if '128x128' in img:
			app_images_src.append(str(img))
	return app_names, app_prices, app_links, app_ratings, app_images_src


def print_(list_):
	for i in list_:
		print i
		print '\n'

'''
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
'''
APPURL = 'https://cafebazaar.ir/app/com.craneballs.flingfighters/?l=en'

def get_second_info(AppUrl):
	DetailsList = []
	TestList = []
	AppDetails = {}
	# Query the website and return the HTML to the variable HTML
	HTML = urllib2.urlopen(AppUrl)
	# Parse the html using beautiful soup and store in variable SOUP
	SOUP = BeautifulSoup(HTML, 'html.parser')

	details = SOUP.findAll('span', attrs={'class':'pull-right'})

	for detail in details:
		element = str(detail.text.strip())
		DetailsList.append(element)

	for element in range(len(DetailsList)):
		if '+' in DetailsList[element]:
			TestList.append(DetailsList[element-1])
			TestList.append(DetailsList[element])
			TestList.append(DetailsList[element+1])
			TestList.append(DetailsList[element+2])
			break

	AppDetails['category'] = TestList[0]
	AppDetails['active_installs'] = TestList[1]
	AppDetails['size'] = TestList[2]
	AppDetails['version'] = TestList[3]

	return AppDetails

#print(get_second_info(APPURL))

app_names, app_prices, app_links, app_ratings, app_images_src = get_first_info(URL)
#print_(app_links)
print '[Page :%s] loading... \n'%str(PAGE)
for i in range(24):
	print 'geting Application [%s] data'%i
	dic1 = {'app_name':app_names[i], 'app_price':app_prices[i],'app_rating':app_ratings[i], 'app_image_src':app_images_src[i], 'app_link':app_links[i]}
	dic2 = get_second_info(app_links[i])
	dic1.update(dic2)
	Application.append(dic1)
os.system('cls')
print_(Application)
