from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


topic_search = "JPMorgan Chase"
year_search = "2023"
topic_search = topic_search.replace(" ", "+")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)

for i in range(1):
    elements = browser.get(
        'https://www.google.com/search?q=' + topic_search + '+annual+report+' + year_search + '+filetype:pdf' + '&start=' + str(
            i))

list = [
    "JPMorgan Chase",
    "Saudi Arabian Oil Company (Saudi Aramco)",
    "ICBC",
    "China Construction Bank",
    "Agricultural Bank of China"
]
# Очікування появи посилання
first_result_link = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g:nth-child(1) a'))
)

# Клік на посилання
first_result_link.click()

# Перехід на нову вкладку
time.sleep(8)
browser.switch_to.window(browser.window_handles[-1])

pdf_link = browser.current_url  # Отримати поточну URL-адресу вікна з PDF-файлом

print(pdf_link)

response = requests.get(pdf_link)
if response.status_code == 200:
    with open('annual_report_2023.pdf', 'wb') as pdf_file:
        pdf_file.write(response.content)
    print("PDF-файл завантажено успішно.")
else:
    print("Помилка завантаження PDF-файлу.")