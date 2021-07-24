from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from html.parser import HTMLParser

email = "enter email here"
password = "Enter Password Here"

driver = webdriver.Chrome()

driver.get("https://parler.com/login.php")

time.sleep(3)

driver.find_element_by_xpath("//input[@type='email']").send_keys(email)

driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
print("You must fill in the Captcha Manually, Sorry :(")

time.sleep(10)

#class MyHTMLParser(HTMLParser):

#    def handle_starttag(self, tag, attrs):
#        print("Encountered a start tag:", tag)

#    def handle_endtag(self, tag):
#        print("Encountered an end tag :", tag)

#    def handle_data(self, data):
#        print("Encountered some data  :", data)
#        if data==user:
#            print("Got here 1")
class MyHTMLParser(HTMLParser):

   #Initializing lists
   lsStartTags = list()
   lsEndTags = list()
   lsStartEndTags = list()
   lsComments = list()

   #HTML Parser Methods
   def handle_starttag(self, startTag, attrs):
       self.lsStartTags.append(startTag)

   def handle_endtag(self, endTag):
       self.lsEndTags.append(endTag)

   def handle_startendtag(self,startendTag, attrs):
       self.lsStartEndTags.append(startendTag)

   def handle_comment(self,data):
       self.lsComments.append(data)


parser = MyHTMLParser()

driver.find_element_by_xpath("//button[@type='submit']").click()

time.sleep(5)

userstoscrape=["Enter userstoscrape here"]

alldata=''

posts=1000

for user in userstoscrape:
    q=0
    driver.find_element_by_xpath("//input[@id='header-search']").send_keys(user)
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 0);")
    str69lol=str('//*[@id="search-results"]/div[2]/div/ul/li[1]/div/a[2]/h3')
    element=driver.find_element_by_xpath(str69lol)
    element.click()
    time.sleep(5)
    for i in range(posts):
        a = driver.find_elements_by_class_name("post__content")
        links = [elem.get_attribute('outerHTML') for elem in a]
        print(a)
        print(i)
        tempnum=1000*i
        driver.execute_script("window.scrollTo(0, "+str(tempnum)+");")
    print(links)
    for parley in links:
        m = re.search("<p>(.+?)</p>", parley)
        if m:
            found=m.group(1)
            print(found)
    time.sleep(7)
    driver.find_element_by_xpath("//input[@id='header-search']").clear()


    #print(driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[3]/div/div[2]/div/ul/li[1]/div').get_attribute('href')) #used to have /p at the end and 'a[2]'


driver.quit()

    #print(driver.find_element_by_xpath("//*[@id=" +user+ "]/div[2]/div/ul/li[1]/div/a[2]/p"))
    #a=driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    #soup = BeautifulSoup(a, 'html.parser')

    #print(soup.prettify())
    #for link in soup.find_all('a'):
    #    if q==0:
    #        if str("/search?type=hashtag&s="+user) in str(link.get('href')):
    #            q=1
    #    elif q==1:
    #        print(link.get("href")[6:])
    #        nameofuser=link.get("href")[6:]
    #        link.get("href").click()
    #        q=0
    #driver.find_element_by_xpath(".//a").click()
    #link="https://parler.com/#/user/"+nameofuser
    #driver.get(str(link))
    #print("GOT HERE")
    #parser.feed(a)
    #print(lsComments)
