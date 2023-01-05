from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def scrap_sephora(url, perc):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
    sleep(3)
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
    sleep(3)
    products = []
    for product in driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/main/div[2]/div[2]/div/a'):
        original_link = product.get_attribute('href')
        try:
            photo = product.find_element(By.XPATH, './/picture/img').get_attribute('src')
        except:
            continue
        brand = product.find_element(By.XPATH, './span[1]').text
        full_name = product.find_element(By.XPATH, './span[2]').text
        price = float(product.find_element(By.XPATH, './/b/span').text.replace('$','').split(' ')[0]) * perc
        staff_pick = float(product.find_element(By.XPATH, './div[2]/span[1]').get_attribute('aria-label').split(" ")[0]) > 4
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(original_link)
        description = []
        for i in driver.find_elements(By.XPATH, '/html/body/div[2]/main/div[1]/div[6]/div[2]/div/div'):
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
            description="".join(description),
        ))

    return products
