import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chromepath = "/Users/sdesai/Desktop/selenium/chromedriver"
import time
import requests
import bs4
from bs4 import BeautifulSoup

import lxml

url  = "https://www.zillow.com/toronto-on/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.77051922962714%2C%22east%22%3A-78.98225018665839%2C%22south%22%3A43.57640738664757%2C%22north%22%3A43.83947561739885%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {""}
#get your headers from http://myhttpheader.com

res = requests.get(url, headers=headers)


url2 = "https://www.zillow.com/toronto-on/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.77051922962714%2C%22east%22%3A-78.98225018665839%2C%22south%22%3A43.393568616256196%2C%22north%22%3A44.020961305917474%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url3 = "https://www.zillow.com/toronto-on/3_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A3%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.77051922962714%2C%22east%22%3A-78.98225018665839%2C%22south%22%3A43.393568616256196%2C%22north%22%3A44.020961305917474%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url4 = "https://www.zillow.com/toronto-on/4_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A4%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url5 = "https://www.zillow.com/toronto-on/5_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A5%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url6= "https://www.zillow.com/toronto-on/6_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A6%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url7= "https://www.zillow.com/toronto-on/7_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A7%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url8="https://www.zillow.com/toronto-on/8_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A8%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url9="https://www.zillow.com/toronto-on/9_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A9%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url10="https://www.zillow.com/toronto-on/10_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A10%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url11="https://www.zillow.com/toronto-on/11_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A11%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url12="https://www.zillow.com/toronto-on/12_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A12%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url13="https://www.zillow.com/toronto-on/13_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A13%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url14="https://www.zillow.com/toronto-on/14_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A14%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url15="https://www.zillow.com/toronto-on/15_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A15%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url16="https://www.zillow.com/toronto-on/16_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A16%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url17="https://www.zillow.com/toronto-on/17_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A17%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url18="https://www.zillow.com/toronto-on/18_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A18%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url19="https://www.zillow.com/toronto-on/19_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A19%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url20="https://www.zillow.com/toronto-on/20_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A20%7D%2C%22usersSearchTerm%22%3A%22Toronto%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.85017010853339%2C%22east%22%3A-78.90259930775214%2C%22south%22%3A43.35863189874156%2C%22north%22%3A44.05551421479119%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D"
url21="https://www.zillow.com/brampton-on/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Brampton%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.99646320237221%2C%22east%22%3A-79.52267780198159%2C%22south%22%3A43.55067614242394%2C%22north%22%3A43.899018514819204%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
url22= "https://www.zillow.com/brampton-on/2_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Brampton%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.99646320237221%2C%22east%22%3A-79.52267780198159%2C%22south%22%3A43.55067614242394%2C%22north%22%3A43.899018514819204%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%22currentPage%22%3A2%7D%7D"
url23="https://www.zillow.com/brampton-on/3_p/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Brampton%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.99646320237221%2C%22east%22%3A-79.52267780198159%2C%22south%22%3A43.55067614242394%2C%22north%22%3A43.899018514819204%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792682%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22pagination%22%3A%7B%22currentPage%22%3A3%7D%7D"
url24="https://www.zillow.com/mississauga-on/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.90349887633437%2C%22east%22%3A-79.42971347594374%2C%22south%22%3A43.431493613186845%2C%22north%22%3A43.78052627192224%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792679%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
url25="https://www.zillow.com/mississauga-on/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Mississauga%2C%20ON%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.90349887633437%2C%22east%22%3A-79.42971347594374%2C%22south%22%3A43.431493613186845%2C%22north%22%3A43.78052627192224%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792679%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"



urllist = [url,url2,url3,url4,url5,url6,url7,url8,url9,url10,url11,url12,url13,url14,url15,url16,url17,url18
           ,url19,url20,url21,url22,url23,url24,url25]
testpricelist = []
testaddylist = []

for url in urllist:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    priceresult = soup.select("div .list-card-heading")
    addyresult = soup.select("address, .list-card-addr")


    for houses in priceresult:
        for wrapper in houses.find_all('div', {"class": "list-card-price"}):
            num = wrapper.text[2:]
            finalnum = (num.replace(",", ""))
            testnum = float(finalnum.replace("+", ""))
            testpricelist.append(testnum)

    for addy in addyresult:
        testaddylist.append(addy.text)




s=Service(chromepath)
browser = webdriver.Chrome(service=s)

url = "https://forms.gle/5zNXhdspwpNCYe777"
#change this with your own forms URL


datalist = list(zip(testpricelist, testaddylist))

for data in datalist:
    url = "https://forms.gle/5zNXhdspwpNCYe777"
    #change this with your own forms URL
    browser.get(url)
    time.sleep(2)
    addressinput = browser.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    priceinput = browser.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submitbutton = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


    addressinput.send_keys(data[1])
    priceinput.send_keys(data[0])

    submitbutton.click()