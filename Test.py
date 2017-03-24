from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

#USE THIS TWO LINES TO RUN PYTHON TEST IN HEADLESS MODE(NO BROWSER)

display = Display(visible=0, size=(800, 600))
display.start()

# now Firefox will run in a virtual display.
# you will not see the browser.

wd = webdriver.Firefox(executable_path='./driver/geckodriver')

#wd.implicitly_wait(30)
wait = WebDriverWait(wd,60)
wd.get('https://google.com/')

#USE BELOW CODE TO AUTHENTICATE BASIC HTTP PAGE
#wd.get('http://username:password@somewebsite.com')

#alert = wd.switch_to_alert()
#alert.authenticate('Username','Password')
#time.sleep(3)

#ActionChains(wd).send_keys('username').send_keys(Keys.TAB).send_keys('password').perform()

#time.sleep(3)
#alert.accept()
#time.sleep(3)

#print  wd.find_element_by_id("btntld").get_attribute("value")
wd.quit()
