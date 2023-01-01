from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json


driver = webdriver.Chrome()
driver.get("https://www.sephora.com/shop/face-serum")
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
sleep(3)
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
sleep(3)
products = []
for product in driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div[2]/div/a'):
    original_link = product.get_attribute('href')
    try:
        photo = product.find_element(By.XPATH, './/picture/img').get_attribute('src')[:-3]+"350"
    except:
        continue
    brand = product.find_element(By.XPATH, './span[1]').text
    full_name = product.find_element(By.XPATH, './span[2]').text
    price = product.find_element(By.XPATH, './/b/span').text.replace('$','').split(' ')[0]
    description = f'{brand}, {full_name}'
    staff_pick = float(product.find_element(By.XPATH, './div[2]/span[1]').get_attribute('aria-label').split(" ")[0]) > 4
    products.append(dict(
        original_link=original_link,
        full_name=full_name,
        photo=photo,
        price=price,
        brand=brand,
        staff_pick=staff_pick,
        description=description,
    ))

f = open('result.json', 'w')
json.dump(products, f)
f.close()