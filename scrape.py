from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://quotes.toscrape.com/page/1/")
driver.maximize_window()


def scrap():
    data = []
    names = []
    quotes = driver.find_elements_by_xpath("//span[@class='text']")
    authors = driver.find_elements_by_xpath("//small[@class='author']")
    for quote in quotes:
        data.append(quote.text)

    for author in authors:
        names.append(author.text)



    for i in range(len(data)):
        print(data[i] + " --- " + names[i])

scrap()
