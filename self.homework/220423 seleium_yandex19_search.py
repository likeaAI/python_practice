from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
path = 'C:/Users/crid2/driver/chromedriver.exe'

# url =''
# driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# mail_address = 'crid2450@gmail.com'
# password = 'g5y013650e!'

driver = webdriver.Chrome(path)
# keyword = input(' yandex에서 검색할 keyword를 입력하세요 : ')
driver.get('https://yandex.com/images/search' + '?text=' + 'gundam')

#
# # scroll down function
#
# SCROLL_PAUSE_TIME = 1.5
# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try :
#             driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/a').click()
#         except :
#             break
#
#     last_height = new_height

# # image search and local download
all_images = driver.find_element_by_css_selector('.')



# count = 1
# for image in images :
#     try :
#         image.click()
#         img_url = driver.find_element_by_css_selector('.n3VNCb').get_attribute('src')
#         urllib.request.urlretrieve(img_url, str(count) + '.jpg')
#         time.sleep(1)
#         count += 1
#     except :
#         pass
#
# elem.clear()
# driver.close()
#
