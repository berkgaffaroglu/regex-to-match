from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import re

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get('')
page_source = browser.page_source
allowed_list = ['button','a','input']
tags = [f"<{x}[^>]*>" for x in allowed_list]
regex_code = fr"{'|'.join(tags)}"
matches = re.findall(regex_code, page_source)
final_html = "\n".join(matches)
with open("allowed_elements.html", "w", encoding="utf-8") as file:
    file.write(final_html)
browser.quit()