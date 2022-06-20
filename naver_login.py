from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip

driver = webdriver.Chrome(r"C:\Users\rladl\Jupyter.study\driver\chromedriver.exe")
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
driver.implicitly_wait(5) # 웹 페이지가 로딩 될 때까지 5초 대기

# ID 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy("********")
pyautogui.hotkey("ctrl", "v")
# id.send_keys("********")
time.sleep(2)

# Password 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("********")
pyautogui.hotkey("ctrl", "v")
# pw.send_keys("********")
time.sleep(2)

# Login 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()