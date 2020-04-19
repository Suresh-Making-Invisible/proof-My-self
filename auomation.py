from  selenium import  webdriver
import  time

username = 'sk864735@gmail.com'
password = 'tamilansuresh'
url = 'https://www.facebook.com/'

driver = webdriver.Chrome("E:\download\chromedriver_win32\chromedriver")
driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
time.sleep(2)
driver.find_element_by_id('loginbutton').click()




