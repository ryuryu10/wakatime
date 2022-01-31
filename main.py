from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

_URL = "https://wakatime.com/dashboard"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(_URL)
driver.implicitly_wait(10)
print("로그인 대기")
p_tag = WebDriverWait(driver,timeout=999).until(EC.presence_of_element_located((By.CLASS_NAME, "bb-chart")))
print("로그인 감지됨")
driver.quit()