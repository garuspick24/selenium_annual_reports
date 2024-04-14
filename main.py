import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)


def download_pdf(company_name: str, rank: str, year: int = 2023):
    name_for_url = company_name.replace(" ", "+")
    elements = browser.get(f"https://www.google.com/search?q={name_for_url}+annual+report+{year}+filetype:pdf+&start=0")

    first_result_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g:nth-child(1) a'))
    )

    first_result_link.click()
    time.sleep(4)

    pdf_link = browser.current_url  # Отримати поточну URL-адресу вікна з PDF-файлом

    response = requests.get(pdf_link)
    if response.status_code == 200:
        with open(f'reports/{rank}. {company_name}_{year}.pdf', 'wb') as pdf_file:
            pdf_file.write(response.content)
        print("PDF-файл завантажено успішно.")
    else:
        print("Помилка завантаження PDF-файлу.")
    time.sleep(10)


def download_multiple_pdfs(file_name: str):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        for element in data:
            try:
                download_pdf(element['name'], element['rank'])
                print(f"Завантажено {element['rank']}. {element['name']}")
                time.sleep(10)
            except Exception as e:
                with open("errors.txt", "a") as errors_file:
                    errors_file.write(f"{element['rank']}. {element['name']}: {str(e)}\n")
                print(f"Помилка завантаження {element['rank']}. {element['name']}: {str(e)}")


download_multiple_pdfs("forbes.json")
