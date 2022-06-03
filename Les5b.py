from pprint import pprint
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time

s = Service('./msedgedriver.exe')
options = Options()
options.add_argument('start-maximized')

driver = webdriver.Edge(service=s, options=options)
driver.get('https://account.mail.ru/login')

input = driver.find_element(By.NAME, 'username')
input.send_keys('study.ai_172@mail.ru', Keys.ENTER)


#input_p = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
# не понял как заставить WebDriverWait ждать до нужного момента, поэтому time.sleep

input_p = driver.find_element(By.NAME, 'password')
time.sleep(1)
input_p.send_keys('NextPassword172#')
input_p = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button [@data-test-id="submit-button"]'))).click()
#input_p.click()
#send_keys(Keys.ENTER)

time.sleep(3)

one_letter = driver.find_element(By.XPATH, '//a[@class="llc llc_normal llc_new llc_new-selection js-letter-list-item js-tooltip-direction_letter-bottom"]').click()

letter_list = []

q = 0
#while True
while q < 2:
    try:
        letter_data = {}

        time.sleep(1)

        sender = driver.find_element(By.XPATH, '//span[@class="letter-contact"]').text
        date = driver.find_element(By.XPATH, '//div[@class="letter__date"]').text
        topic = driver.find_element(By.XPATH, '//h2[@class="thread-subject"]').text
        text = driver.find_element(By.XPATH, '//div[@class="letter-body"]').text

        letter_data['1.Sender'] = sender
        letter_data['2.Date'] = date
        letter_data['3.Topic'] = topic
        letter_data['4.Text'] = text

        letter_list.append(letter_data)

        time.sleep(1)

        next_page = driver.find_element(By.XPATH, '//div[contains(@class, "portal-menu-element portal-menu-element_next portal-menu-element_expanded portal-menu-element_not-touch")]').click()

        q += 1
    except:
        break

'''letters = driver.find_elements(By.XPATH, '//a[@class="llc llc_normal llc_new llc_new-selection js-letter-list-item js-tooltip-direction_letter-bottom"]')

letters_collection = set()

action = ActionChains(driver)

q = 0
while q < 40:

    for letter in letters:
        let = letter.get_attribute('href')
        letters_collection.add(let)

    lett = driver
    lett.get('https://e.mail.ru/inbox/?authid=l3ybkzxg.hxs&back=1%2C1&dwhsplit=s10273.b1ss12743s&from=login&x-login-auth=1&afterReload=1')
    lett.execute_script("window.scrollBy(0,2000)","")
    q += 1

print(letters_collection)
print(len(letters_collection))'''

pprint(letter_list)
driver.close