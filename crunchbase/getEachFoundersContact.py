# to install SSL on Mac
# https://medium.com/@katopz/how-to-upgrade-openssl-8d005554401
# pip install selenium

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
bs = BeautifulSoup(driver.page_source,"html.parser")
links = bs.find_all('a', class_="cb-link component--field-formatter field-type-link layout-row layout-align-start-end ng-star-inserted")
for l in links:
    if 'linkedin.com' in l['href']:
        linkedinLink = l['href']
        break
    else:
        linkedinLink = 'not found'
print(linkedinLink)
# from fake_useragent import UserAgent
# import requests


# ua = UserAgent()
# print(ua.chrome)
# header = {'User-Agent':str(ua.chrome), 'Content-Type': 'application/json'}
# print(header)

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# url = 'https://www.crunchbase.com/person/pascal-lorne'

# htmlContent = requests.get(url, headers=header)
# print(htmlContent)


# with open('gh.html', 'w') as f:
#     f.write(str(htmlContent.content,'utf-8')) 

