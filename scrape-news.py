#!/usr/bin/env python3
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
from bs4 import BeautifulSoup as bs
import json
import re

username = "username_here"
password = "password_here"

driver = webdriver.Firefox()

#uncomment these lines if your firefox installation is not standard
#firefox_binary = FirefoxBinary("/path/to/firefox")
#driver = webdriver.Firefox(firefox_binary=firefox_binary)


#Login
driver.get("http://www.myfamily.com/isapi.dll?c=autht&htx=login&onok=http%3A%2F%2Fwww.myfamily.com%2Fisapi.dll%3Fc=site%26htx=Main%26siteid=*&rsn=0")
sleep(2)
while True:
	try:
		driver.get("http://www.myfamily.com/isapi.dll?c=autht&htx=login&onok=http%3A%2F%2Fwww.myfamily.com%2Fisapi.dll%3Fc=site%26htx=Main%26siteid=*&rsn=0")
		sleep(0.5)
		driver.find_element_by_name("username").send_keys(username)
		break
	except selenium.common.exceptions.NoSuchElementException:
		sleep(4)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("submitbtn").click()

sleep(2)

#Click through each news item
pages = dict()
c = 1
stop = False
driver.get("http://www.myfamily.com/isapi.dll?c=content&htx=view&siteid=J9ZfAI&contentid=ZZZZZZZR&contentclass=NEWS&categoryid=0")
while not stop:
	if driver.current_url == "http://export.myfamily.com/notification.aspx":
		sleep(0.3)
		driver.find_element_by_css_selector('#Button1').click()
		sleep(0.3)
		driver.back()
		sleep(0.3)
		driver.back()
		sleep(0.3)
		try:
			driver.find_element_by_link_text('Previous').click()
		except selenium.common.exceptions.NoSuchElementException:
			stop = True
	with open('data/raw-html/news/' + str(c) + '.html', 'w') as f:
		f.write(driver.page_source)
	with open('news-pages.json', 'w') as f:
		pages[c] = driver.current_url
		f.write(json.dumps(pages))
	try:
		driver.find_element_by_link_text('Previous').click()
	except selenium.common.exceptions.NoSuchElementException:
		stop = True
	c += 1

	
	