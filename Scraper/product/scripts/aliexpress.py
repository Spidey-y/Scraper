from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains
from .add_prodcut import AddProduct



def scrap_aliexpress(url, perc, store, cate, maxVal, more, less):
    driver = webdriver.Chrome()
    driver.get(url)
    language = driver.find_element(By.CSS_SELECTOR, '#switcher-info')
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(language).click(language).perform()
    sleep(1)
    language = driver.find_element(By.CSS_SELECTOR, '#nav-global > div.ng-item-wrap.ng-item.ng-switcher.active > div > div > div > div.switcher-language.item.util-clearfix > div > span')
    language.click()
    sleep(1)
    language = driver.find_element(By.CSS_SELECTOR, '#nav-global > div.ng-item-wrap.ng-item.ng-switcher.active > div > div > div > div.switcher-language.item.util-clearfix > div > ul > li:nth-child(5) > a')
    language.click()
    sleep(1)
    language = driver.find_element(By.CSS_SELECTOR, '#nav-global > div.ng-item-wrap.ng-item.ng-switcher.active > div > div > div > div.switcher-currency.item.util-clearfix > div > span')
    language.click()
    sleep(1)
    language = driver.find_element(By.CSS_SELECTOR, '#nav-global > div.ng-item-wrap.ng-item.ng-switcher.active > div > div > div > div.switcher-currency.item.util-clearfix > div > ul > li:nth-child(5) > a')
    language.click()
    sleep(1)
    language = driver.find_element(By.CSS_SELECTOR, '#nav-global > div.ng-item-wrap.ng-item.ng-switcher.active > div > div > div > div.switcher-btn.item.util-clearfix > button')
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
        AddProduct(dict(
            original_link=original_link,
            full_name=full_name,
            photo=photo,
            price=price,
            brand=brand,
            staff_pick=staff_pick,
            description=description,
        ), store, cate, maxVal, more, less)
        

