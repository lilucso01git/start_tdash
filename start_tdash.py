from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(r'C:\Apps\ChromeDriver\chromedriver.exe')

# テストプロジェクト画面を開く
driver.get('http://localhost:8686/#/dice1/testlist')
sleep(5)

# ［テスト実行］ボタンをクリックする
ele = driver.find_element(By.XPATH, "//*[@data-valtes='scenario-item-quickrun']")
ele.click()

# ［続行する］ボタンをクリックする（筆者の現在の環境では、「無料プラン」で広告ダイアログが出てしまうため。）
sleep(2)
ele2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/section/main/section/section/section/main/div[2]/div/div/div/div/div/span/button')
ele2.click()

# テストの実行完了まで待機する
sleep(15)

# 終了する
driver.quit