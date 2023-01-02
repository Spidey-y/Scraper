from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains
from .config import set_chrome_options

def scrap_aliexpress(url, perc):
    driver = webdriver.Chrome(options=set_chrome_options())
    driver.get(url)
    language = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(language).click(language).perform()
    sleep(1)
    language = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/span/a')
    language.click()
    sleep(1)
    language = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[2]/div/ul/li[1]/a')
    language.click()
    sleep(1)
    language = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[3]/div/span/a')
    language.click()
    sleep(1)
    language = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[3]/div/ul/li[5]/a')
    language.click()
    sleep(1)
    language = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[4]/button')
    language.click()
    sleep(1)

    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
    sleep(1)
    driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
    sleep(1)
    products = []
    for product in driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/div/a'):
        original_link = product.get_attribute('href')
        photo = product.find_element(By.XPATH, './/div/img').get_attribute('src')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(original_link)
        full_name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/h1').text
        try:
            staff_pick = float(driver.find_element(By.CSS_SELECTOR, '#root > div > div.product-main > div > div.product-info > div.product-reviewer > div > span').text) > 4
        except:
            staff_pick = False
        try:
            price = driver.find_element(By.CSS_SELECTOR, '#root > div > div.product-main > div > div.product-info > div.product-price > div.product-price-current > span').text.split("$")[-1]
        except:
            price = driver.find_element(By.CSS_SELECTOR, '#root > div > div.product-main > div > div.product-info > div.uniform-banner > div.uniform-banner-box > div:nth-child(1) > span.uniform-banner-box-price').text.split("$")[-1]
        price = float("{:.2f}".format(float(price))) * perc
        brand = ""
        description = full_name
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
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
