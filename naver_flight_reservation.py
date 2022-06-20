from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹 페이지 대기 하는 함수 만들기
def wait_until(xpath_str):
    # driver가 xpath_str을 60초 동안 못 찾을시 기다린다.
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_str)))

driver = webdriver.Chrome(r"C:\Users\rladl\Jupyter.study\driver\chromedriver.exe")
driver.get("https://flight.naver.com")
# 2초 대기
time.sleep(2)

# 가는 날 고르기
begin_date = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')
begin_date.click()
wait_until('//b[text() = "13"]')

# 2022.12.13
day13 = driver.find_elements(By.XPATH, '//b[text() = "13"]')
day13[6].click()
wait_until('//b[text() = "3"]')

# 2023.1.3
day3 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[9]/table/tbody/tr[1]/td[3]/button/b')
day3.click()
wait_until('//b[text() = "도착"]')

# 도착지 고르기
arrival = driver.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()
wait_until('//button[text() = "미주"]')

# 미주지역에서 고르기
usa = driver.find_element(By.XPATH, '//button[text() = "미주"]')
usa.click()
wait_until('//i[contains(text(), "로스앤젤레스국제공항")]')

# 미주 지역 공항 고르기
airport = driver.find_element(By.XPATH, '//i[text() = "로스앤젤레스국제공항"]')
airport.click()
wait_until('//span[contains(text(), "항공권 검색")]')

# 검색 버튼 누르기
search = driver.find_element(By.XPATH, '//span[text() = "항공권 검색"]')
search.click()
wait_until('//span[text() = "직항/경유 "]')

# 직항/경유 버튼 누르기
direct_flight = driver.find_element(By.XPATH, '//span[text() = "직항/경유 "]')
direct_flight.click()
wait_until('//i[text() = "직항"]')

# 직항 선택
direct = driver.find_element(By.XPATH, '//i[text() = "직항"]')
direct.click()
wait_until('//button[text() = "적용"]')

# 선택 후 적용하기
confirm = driver.find_element(By.XPATH, '//button[text() = "적용"]')
confirm.click()

# 검색한 결과 elems에 저장하기
elems = driver.find_elements(By.XPATH, '//div[@class="concurrent_ConcurrentItemContainer__2lQVG result"]')

for i, elem in enumerate(elems):
    print(f'{i+1}번째 항공권 : {elem.text}')
    print('-------------------------------------------------')
    if i == 2:
        break
