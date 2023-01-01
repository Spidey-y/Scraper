from selenium import webdriver
from selenium.webdriver.common.by import By
import json


driver = webdriver.Chrome()
driver.get(
    "https://eur.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?ici=CCCSN%3DWomenHomePage_ON%3DBanner_OI%3D1_CN%3Dcate_TI%3D50001_aod%3D0_PS%3DHZ-7-3_ABT%3D0&adp=11177686&scici=WomenHomePage~~ON_Banner%2CCN_cate%2CHZ_1%2CHI_hotZonebtzg3of2qhv~~7_3~~real_1766~~~~&srctype=homepage&userpath=-WomenHomePage-Women-Tops%2C-Blouses-Tee&src_module=WomenHomePage&src_identifier=on%3DBanner%60cn%3Dcate%60hz%3D1%60ps%3D7_3%60jc%3Dreal_1766&src_tab_page_id=page_home1672552259631&sort=10")
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
products = []
for product in driver.find_elements(By.XPATH, '//*[@id="product-list-v2"]/div/div[2]/div[2]/section/div[1]/section'):
    original_link = product.find_element(By.XPATH, './/div[2]/div[1]/a').get_attribute('href')
    full_name = product.find_element(By.XPATH, './/a').get_attribute("aria-label")
    photo = product.find_element(By.XPATH, './/img').get_attribute('data-src')
    price = product.find_element(By.XPATH, './div[2]/div[2]/section/div[1]/span').get_attribute('aria-label')[5:-1].replace(',', '.')
    brand = "Shein"
    staff_pick = True
    description = full_name
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