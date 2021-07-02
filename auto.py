from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\Python\chromedriver')

driver.get('https://www.gorgany.com/')
driver.maximize_window()
time.sleep(1)

login_button = driver.find_element_by_css_selector("button[class='user hidden-xs hidden-sm hidden-md login']")
login_button.click()
driver.implicitly_wait(10)

email_field = driver.find_element_by_css_selector("input[placeholder='Ваша e-mail адреса']")
driver.execute_script("arguments[0].click();", email_field)
email_field.send_keys("mr.kutovyi@gmail.com")

pass_field = driver.find_element_by_css_selector("input[placeholder='Ваш пароль']")
driver.execute_script("arguments[0].click();", pass_field)
pass_field.send_keys("ab63cbee6a")
driver.implicitly_wait(10)

login = driver.find_element_by_css_selector("button[id='button-login']")
login.click()
driver.implicitly_wait(10)



unlogin_button = driver.find_element_by_css_selector ("button[class='user hidden-xs hidden-sm hidden-md login']")
unlogin_button.click()
driver.implicitly_wait(10)
# driver.quit()
