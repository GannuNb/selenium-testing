import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver =webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-1727491234%3A1690027339963719&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AeDOFXgTkZJvIE0HgnBx92UjVzOuQp8bF34Xs0keO3K_DCnZUZdY3lylPHdDsS-h9yLB0OriWxgsaQ&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.find_element(By.ID,"identifierId").send_keys("ganesh.nallabapineni@maangtechnologies.com")
driver.find_element(By.XPATH,"//button[contains(@class,'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b')]").click()
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("gannumouni@143")
driver.find_element(By.XPATH,"//button[contains(@class,'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b')]").click()
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='T-I T-I-KE L3']")))

element.click()
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[id=':1ij']"))).click()


#driver.find_element(By.CSS_SELECTOR, "div[class='fX aiL']").send_keys("Srinivasulu@maangtechnologies.com")
#driver.find_element(By.CSS_SELECTOR, "span[id=':qx']]").send_keys("linga@maangtechnologies.com")
#driver.find_element(By.CSS_SELECTOR, "span[id=':qx']]").send_keys("hr@maangtechnologies.com")
#driver.find_element(By.CSS_SELECTOR, "input[id=':th']").send_keys("Daily status")
#driver.find_element(By.CSS_SELECTOR, "div[id=':up']").send_keys("hjjfhgfjkdfjbvhdjbfnkldsfkbgdjnkfdjkdfkjb")

#driver.find_element(By.CSS_SELECTOR, "div[id=':t7']]").click()
driver.find_element(By.XPATH,"//span[@id=':lw']").click()
driver.find_element(By.CSS_SELECTOR, "//input[@id=':vn']").send_keys("fjkgbgks")
time.sleep(5)
driver.close()




