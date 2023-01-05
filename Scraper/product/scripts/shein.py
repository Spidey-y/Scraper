from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def scrap_shein(url, perc):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
    sleep(1)
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
    sleep(1)
    products = []
    for product in driver.find_elements(By.XPATH, '//*[@id="product-list-v2"]/div/div[2]/div[2]/section/div[1]/section'):
        original_link = product.find_element(By.XPATH, './/div[2]/div[1]/a').get_attribute('href')
        full_name = product.find_element(By.XPATH, './/a').get_attribute("aria-label")
        photo = "https://" + product.find_element(By.XPATH, './/img').get_attribute('data-src')[2::]
        price = float(product.find_element(By.XPATH, './div[2]/div[2]/section/div[1]/span').get_attribute('aria-label')[5:-1].replace(',', '.')) * perc
        brand = "Shein"
        staff_pick = True
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(original_link)
        description = []
        for i in driver.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/div/div/div[3]/div'):
            description.append("".join(i.get_attribute("innerText")))
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        products.append(dict(
            original_link=original_link,
            full_name=full_name,
            photo=photo,
            price=price,
            brand=brand,
            staff_pick=staff_pick,
            description="\n".join(description),
        ))
        print(products[-1])
    return products