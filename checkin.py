from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import sys

def checkin():
    """自动签到脚本"""
    
    # 初始化Chrome浏览器
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')  # 无头模式（不显示浏览器）
    options.add_argument('--disable-gpu')
    
    driver = None
    
    try:
        print(f"[{datetime.now()}] 正在打开网站...")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        
        driver.get("https://node.miapi.cc/#/checkin")
        
        # 等待页面加载完成
        time.sleep(3)
        
        # 点击签到按钮
        try:
            # 方法1：查找并点击按钮
            checkin_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'el-button')]"))
            )
            checkin_button.click()
            print(f"[{datetime.now()}] ✓ 签到成功！")
            
        except Exception as e1:
            print(f"[{datetime.now()}] 方法1失败: {e1}")
            try:
                # 方法2：通过更精确的选择器
                checkin_button = driver.find_element(
                    By.XPATH, 
                    "//div[@class='card-item']//button"
                )
                checkin_button.click()
                print(f"[{datetime.now()}] ✓ 签到成功！")
            except Exception as e2:
                print(f"[{datetime.now()}] ❌ 签到失败: {e2}")
                print("页面源代码（前2000字符）:")
                print(driver.page_source[:2000])
                sys.exit(1)
        
        # 等待结果显示
        time.sleep(2)
        print(f"[{datetime.now()}] ✓ 任务完成")
        
    except Exception as e:
        print(f"[{datetime.now()}] ❌ 错误: {e}")
        sys.exit(1)
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    checkin()
