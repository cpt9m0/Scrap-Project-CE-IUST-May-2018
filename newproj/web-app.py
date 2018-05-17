from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

try:
        conn = sqlite3.connect('AppDetails.db')
except Error as e:
        print(e)
global cur

cur = conn.cursor()

def all_apps():
	# global cur, Applications
	Applications = []
	AppNames = []
	AppSizes = []
	AppPrices = []
	AppRates = []
	AppVersions = []
	AppCategories = []
	AppActiveInstalls = []

	cur.execute("SELECT AppName FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppNames.append(str(row[0]))

	cur.execute("SELECT AppSize FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppSizes.append(str(row[0]))

	cur.execute("SELECT AppPrice FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppPrices.append(str(row[0]))

	cur.execute("SELECT AppRate FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppRates.append(int(row[0]))

	cur.execute("SELECT AppVersion FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppVersions.append(str(row[0]))

	cur.execute("SELECT AppCategory FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppCategories.append(str(row[0]))

	cur.execute("SELECT AppActiveInstalls FROM Applications") 
	rows = cur.fetchall()
	for row in rows:
		AppActiveInstalls.append(str(row[0]))

	for i in range(len(AppNames)):
		app = [AppNames[i], AppSizes[i], AppPrices[i], AppRates[i], AppVersions[i], AppCategories[i], AppActiveInstalls[i]]
		Applications.append(app)

	return Applications

def sort_apps_by_rate():
	
	Applications = all_apps()
	Applications = sorted(Applications,key=lambda l:l[3])

	return Applications

def sort_apps_by_size():
	Applications = all_apps()
	for app in Applications:
		app[1] = float(app[1].replace('MB', ''))
	Applications = sorted(Applications,key=lambda l:l[1])
	return Applications


global list01, list02, list03
list01 = all_apps()
list02 = sort_apps_by_rate()
list03 = sort_apps_by_size()
app = Flask(__name__)

@app.route("/")
def welcome():
   return render_template("welcome-page.html")

@app.route('/show-all')
def show_all():
	return render_template("result.html",Apps = list01)

@app.route('/sort-by-rate')
def sort_by_rate():
	return render_template("result.html", Apps = list02)

@app.route('/sort-by-size')
def sort_by_size():
	return render_template("result.html", Apps = list03)

@app.route('/search-name', methods = ['POST', 'GET'])
def search_name():
	if request.method == 'POST':
		result = request.form
		searched = str(result['search by name'])
		print '--------------'+searched+'--------------'
		test = []
		for app in list01:
			if searched in app[0].lower():
				if not (app in test):
					test.append(app)

		return render_template("result.html", Apps = test)

@app.route('/search-category', methods = ['POST', 'GET'])
def search_category():
	if request.method == 'POST':
		result = request.form
		searched = str(result['search by cat'])
		print '--------------'+searched+'--------------'
		test = []
		for app in list01:
			if searched in app[5].lower():
				if not(app in test):
					test.append(app)
		return render_template("result.html", Apps = test)


if __name__ == '__main__':
   app.run(debug = True)

