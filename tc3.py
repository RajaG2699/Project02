import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver_path = r"C:\Users\Raja\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
username = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
username.click()
time.sleep(2)
username.send_keys("Admin")
time.sleep(2)
passw=driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
passw.click()
time.sleep(2)
passw.send_keys("admin123")
time.sleep(2)
logc= driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
logc.click()
time.sleep(2)
adminc=driver.find_element(By.LINK_TEXT,"Admin")
adminc.click()
time.sleep(2)
original_title=driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li')
panel_title=["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard","Directory","Maintenance","Buzz"]
for i in original_title:
    if i.text in panel_title:
        print("In the panel")
    else:
        print("missing in panel")

driver.quit()