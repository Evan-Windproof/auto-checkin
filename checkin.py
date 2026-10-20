from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# 配置 Chrome 选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 使用 Selenium 内置驱动管理（不用 webdriver-manager）
driver = webdriver.Chrome(options=chrome_options)

try:
    print(f"[{datetime.now()}] 正在打开网站...")
    driver.get('https://node.miapi.cc/#/checkin')
    
    # 等待按钮加载
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'el-button')]"))
    )
    
    print(f"[{datetime.now()}] ✅ 找到按钮，正在点击...")
    button.click()
    
    time.sleep(2)
    print(f"[{datetime.now()}] ✅ 打卡成功！")
    
except Exception as e:
    print(f"[{datetime.now()}] ❌ 错误: {e}")
    
finally:
    driver.quit()
