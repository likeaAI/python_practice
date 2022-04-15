from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)

url =''
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

elem = driver.find_element_by_name('q')
elem.send_keys('nude women')
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(' .bRMDJf.islir')[0].click()
time.sleep(3)
print(driver.find_element_by_css_selector('.n3VNCb').get_attribute('src'))

# elem.clear()
# driver.close()

