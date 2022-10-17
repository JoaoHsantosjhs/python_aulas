from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

chromedriver_pah = '/home/joao/PycharmProjects/pythonProject2/aulas aleatorias/chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_pah)
sleep(5)
webdriver.get('https://news.ycombinator.com/submit')
sleep(5)
usuario = webdriver.find_element(By.NAME, 'acct')
usuario.send_keys('jhonxx')
senha = webdriver.find_element(By.NAME, 'pw')
senha.send_keys('jhonxx06')

button_login = webdriver.find_element(By.CSS_SELECTOR, 'body > form:nth-child(4) > input[type=submit]:nth-child(4)')
button_login.click()
sleep(5)
url = 'https://news.ycombinator.com/news'
webdriver.get(url)
rank=webdriver.find_element(By.CLASS_NAME,'titlelink')
rank.click()
sleep(5)