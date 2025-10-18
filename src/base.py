import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# ブラウザのオプション
options = Options()
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
# options.add_argument("--headless")  # ブラウザを非表示で起動する
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("useAutomationExtension", False)

# ブラウザ起動
service = ChromeService(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# 要素が見つかるまで10秒待つ
driver.implicitly_wait(10)

# URLにアクセス
url = "https://www.google.com/"
driver.get(url)
time.sleep(1)

# 検索フォームを探す
input_tag = driver.find_element(By.NAME, "q")

# 検索フォームに文字を入力
input_tag.send_keys("Qiita 面白い記事")

# 検索ボタンをクリック
driver.find_element(By.NAME, "btnK").click()

# ブラウザのHTMLを取得
soup = BeautifulSoup(driver.page_source, features="html.parser")

# 検索結果１つ目のタイトルをターミナルに表示
print(soup.select_one("h3").text)

