from selenium import webdriver
from selenium.webdriver.common.by import By


def scrap_shein(url, perc):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    products = []
    for product in driver.find_elements(By.XPATH, '//*[@id="product-list-v2"]/div/div[2]/div[2]/section/div[1]/section'):
        original_link = product.find_element(By.XPATH, './/div[2]/div[1]/a').get_attribute('href')
        full_name = product.find_element(By.XPATH, './/a').get_attribute("aria-label")
        photo = "https://" + product.find_element(By.XPATH, './/img').get_attribute('data-src')[2::]
        price = float(product.find_element(By.XPATH, './div[2]/div[2]/section/div[1]/span').get_attribute('aria-label')[5:-1].replace(',', '.')) * perc
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
    return products