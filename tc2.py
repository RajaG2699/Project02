import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

title_name="OrangeHRM"
window_title=driver.title
if title_name in window_title:
    print("Validate")
else:
    print("No Validate")
menu_title= driver.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li')
expected_title =["User Management","Job","Organization","Qualifications","Nationalities","Corporate Banking","Configuration"]
for i in menu_title:
    if i.text in expected_title:
        print("In menu titles")
    else:
        print("missing menu titles")

driver.quit()