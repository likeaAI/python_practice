from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

path = 'C:/Users/crid2/driver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

elem = driver.find_element_by_name('q')
elem.send_keys('cass 맥주')
elem.send_keys(Keys.RETURN)
images = driver.find_elements_by_css_selector(' .bRMDJf.islir')

# scroll down function
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")



while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try :
            driver.find_element_by_css_selector('.mye4qd').click()
        except :
            break

    last_height = new_height




# image search and local download
count = 1
for image in images :
    try :
        image.click()
        img_url = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')
        urllib.request.urlretrieve(img_url, str(count) + '.png')
        time.sleep(2)
        count += 1
    except :
        pass

elem.clear()
driver.close()

