from pprint import pprint
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

s = Service('./msedgedriver.exe')
options = Options()
options.add_argument('start-maximized')

driver = webdriver.Edge(service=s, options=options)
driver.get('https://www.mvideo.ru/')

anchor = driver.find_element(By.XPATH, '//body')
anchor.send_keys(Keys.PAGE_DOWN)

while True:
    try:
        button = driver.find_element(By.XPATH, '//span[contains(text(), "В тренде")]')
        button.click()
        break
    except:
        anchor.send_keys(Keys.PAGE_DOWN)

#button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "В тренде")]')))
#button = driver.find_element(By.XPATH, '//span[contains(text(), "В тренде")]')
#button.click()

item_list = []

while True:
    item_dict = {}
    #//mvid-shelf-group//div[@class="title"].text

    name = driver.find_element(By.XPATH, '//mvid-shelf-group//div[@class="title"]').text
    price = driver.find_element(By.XPATH, '//mvid-shelf-group//span[@class="price__main-value"]').text

    item_dict['1.Name'] = name
    item_dict['2.Price'] = price

    item_list.append(item_dict)


pprint(item_list)
driver.close()