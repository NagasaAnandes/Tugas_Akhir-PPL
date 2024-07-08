from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_add_claim_req():
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

  # Click Claim Menu
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a').click()
  sleep(1.5)
  
  # Click Submit Claim
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a').click()
  sleep(1.5)

  # Input Claim Request Details
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i').click()
  sleep(1.5)
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[3]').click()
  sleep(2.0)
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').click()
  sleep(1.5)
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/div[3]').click()
  sleep(2.0)
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea').send_keys('Trip To Bali')
  sleep(1.5)
  
  # Click Create
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
  sleep(10)

  # Click Submit
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[9]/button[3]').click()
  sleep(10)
  
  # Click Back
  driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[9]/button[1]').click()
  sleep(10)

  driver.quit()

test_add_claim_req()