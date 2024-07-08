from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_add_employee():
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  driver.get('https://opensource-demo.orangehrmlive.com/')
  driver.maximize_window()
  
  # Login
  driver.find_element(By.NAME, 'username').send_keys('Admin')
  driver.find_element(By.NAME, 'password').send_keys('admin123')
  sleep(3)

  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
  sleep(4)

  # Click PIM Menu
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
  sleep(1.5)

  # Click Add Employee
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
  sleep(3.5)

  # Input Employee Details
  driver.find_element(By.NAME, 'firstName').send_keys('Test Fname')
  driver.find_element(By.NAME, 'middleName').send_keys('Test Mname')
  driver.find_element(By.NAME, 'lastName').send_keys('Test Lname')
  sleep(2.3)

  # Click Save
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
  sleep(10)

  driver.quit()

test_add_employee()