from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pickle

with open('founderDetails.pickle', 'rb') as founderDetails:
    b = pickle.load(founderDetails)

# WebDriver driver = new HtmlUnitDriver(true);
# driver.get(url);
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://www.crunchbase.com/person/jiby-thomas')
# driver.get('https://www.crunchbase.com/person/pranay-chulet')
# driver.close()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
# user_agentLinux = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'


# options = webdriver.ChromeOptions()
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument("javascript.enabled", True)
# # options.add_argument("--enable-javascript")
# driver = webdriver.Chrome(chrome_options=options)
# driver.get("http://www.guidestar.org")
# the path of the folder containing the html pages of the desired search sheet, 1-50 rows, then 51-100 rows and so on
path  = 'ecommerce/'

import glob, os
files = glob.glob("ecommerce/*.htm") + glob.glob("ecommerce/*.html")
founderRows = []
founderRowsHeading = [['founderName','companyName', 'companyWebsite', 'founderTitle', 'foundersLocation', 'linkedinLink', 'facebookLink', 'twitterLink']]

counter = 0
for file in sorted(files)[0:1]:
	print(file, '   file in the process....\n\n')
	f = open(file, "r").read()
	soup = BeautifulSoup(f, 'html.parser')
	companyRows = soup.find_all('grid-row', class_='ng-star-inserted')
	for companyRow in companyRows[b['totalRowsExtracted']:]:
		counter+=1
		print('\nCounter : {} \n'.format(counter))
		try:
			companyName = companyRow.find('grid-cell', class_='column-id-identifier ng-star-inserted').find('div', class_='flex-no-grow cb-overflow-ellipsis identifier-label').text
			print('companyName : ', companyName, '\n')
		except:
			print('companyName not found')
		try:
			companyWebsite = companyRow.find('grid-cell', class_='column-id-website ng-star-inserted').find('a', class_='cb-link component--field-formatter field-type-link layout-row layout-align-start-end ng-star-inserted')['href']
			print('companyWebsite : ', companyWebsite, '\n')
		except:
			print('companyWebsite not found')
		foundersLinks = companyRow.find('grid-cell', class_="column-id-founder_identifiers ng-star-inserted")
		# print('companys founders crunch links : ',foundersLinks, '\n')
		if foundersLinks:
			foundersLinks = foundersLinks.find_all('a', class_='cb-link ng-star-inserted')
		if len(foundersLinks) != 0:
			print('total number of founders : {}'.format(len(foundersLinks)))
			# foundersLink.append([a['href'] for a in a])
			founderRowsTemp = []
			for foundersLink in foundersLinks:
				driver = webdriver.Chrome(ChromeDriverManager().install())
				print('\ncrunch people link : {}'.format(foundersLink['href']))

				# options = webdriver.ChromeOptions()
				# options.add_argument(f'user-agent={user_agent}')
				# # options.add_argument("javascript.enabled", True)
				# options.add_argument("--enable-javascript")
				# driver = webdriver.Chrome(chrome_options=options)
				driver.delete_all_cookies()
				driver.get(foundersLink['href'])
				bs = BeautifulSoup(driver.page_source,"html.parser")
				driver.close()
				try:
					founderName = bs.find('image-with-fields-card').find('span', class_='ng-star-inserted').text
				except:
					
				# if type(founderName) != str:
					print('Automation Detected. Execution Halted at Row no. : {}'.format(companyRows.index(companyRow)))
					break

				try:
					founderTitle = bs.find('image-with-fields-card').find('span', class_='component--field-formatter field-type-text_short ng-star-inserted').text
				except:
					print('founderTitle not found\n')
					founderTitle = 'NA'
				else:
					print("Nothing went wrong founderTitle : ", founderTitle)
				try:
					foundersLocation = bs.find('span', class_='component--field-formatter field-type-identifier-multi').find_all('a')
					foundersLocation = (', ').join([a.text for a in foundersLocation])
				except:
					print('Location not found\n\n')
					foundersLocation = 'NA'
				else:
					print("Nothing went wrong foundersLocation : ", foundersLocation)
				links = bs.find_all('a', class_="cb-link component--field-formatter field-type-link layout-row layout-align-start-end ng-star-inserted")
				# founderTitle = bs.find_all('span', class_='component--field-formatter field-type-text_short ng-star-inserted')
				# foundersLocation = bs.find_all('span', class_='component--field-formatter field-type-identifier-multi')
				linkedinLink = 'NA'
				facebookLink = 'NA'
				twitterLink = 'NA'
				for l in links:
					if 'linkedin.com' in l['href']:
						print('link in for loop : ',l['href'])
						linkedinLink = l['href']
					if 'facebook.com' in l['href']:
						print('link in for loop : ',l['href'])
						facebookLink = l['href']
					if 'twitter.com' in l['href']:
						print('link in for loop : ',l['href'])
						twitterLink = l['href']
				
				founderDetailRow = [founderName, companyName, companyWebsite, founderTitle, foundersLocation, linkedinLink, facebookLink, twitterLink] 
				print(founderDetailRow, '\n')
				founderRowsTemp.append(founderDetailRow) 
			if len(foundersLinks) == len(founderRowsTemp):
				founderRows = founderRows + founderRowsTemp
		else:
			print('foundersLinks  is empty???')
			founderRows.append([companyRows.index(companyRow),'Row - No Founders','NA','NA','NA','NA','NA','NA']) 
founderRowsHeading = founderRowsHeading + founderRows

import pickle

b = {'data': b['data'] + founderRows  ,
'totalRowsExtracted' : companyRows.index(companyRow)}

with open('founderDetails.pickle', 'wb') as founderDetails:
    pickle.dump(b, founderDetails, protocol=pickle.HIGHEST_PROTOCOL)




# import pandas as pd
# df = pandas.read_csv('hrdata.csv', 
#             index_col='Employee', 
#             parse_dates=['Hired'],
#             header=0, 
#             names=['Employee', 'Hired', 'Salary', 'Sick Days'])
# df.to_csv('hrdata_modified.csv')
# df = pd.DataFrame(founderRowsHeading)
# df.to_excel("foundersDetails.xlsx") 
# 	l = soup.find_all('grid-cell', class_="column-id-founder_identifiers ng-star-inserted")