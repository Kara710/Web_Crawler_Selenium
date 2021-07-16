from selenium import webdriver
from bs4 import BeautifulSoup

#The login page 
url = 'https://www.supersaas.com/schedule/login/Greek_Embassy_London/Greek_Passports' 
# The page you want to grab 
urlneed = "https://www.supersaas.com/schedule/Greek_Embassy_London/Greek_Passports?view=free" 

driver =webdriver.PhantomJS()  #This option will not open a broswer 
#driver =webdriver.Firefox()
#driver =webdriver.Chrome()

#Pass the login form
driver.get (url)
driver.find_element_by_name("name").send_keys('YOUR EMAIL')
driver.find_element_by_name('password').send_keys('YOUR PASSWORD')
driver.find_element_by_name('button').click()

#Grap the page with all executed javascript
driver.get (urlneed)


page=driver.page_source

soup = BeautifulSoup(page, 'html.parser')
title_tag = soup.find("h2", {"class":"cc3"})
tabe_tag = soup.find("table", {"class":"table"})

print(title_tag.text)
for row in tabe_tag.select('tbody tr'):
    row_text = [x.text for x in row.find_all('td')]
    print(' '.join(row_text))        
    

driver.close()

