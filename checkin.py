from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time

# 配置 Chrome 选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

try:
    print(f"[{datetime.now()}] 正在打开网站...")
    driver.get('https://node.miapi.cc/#/checkin')
    
    time.sleep(3)  # 等待页面加载
    
    # 检查是否有滑块验证
    try:
        print(f"[{datetime.now()}] 检查滑块验证...")
        slider_block = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nc_iconfont"))
        )
        
        # 找到滑块和滑块容器
        slider_container = driver.find_element(By.CLASS_NAME, "nc_outer")
        slider_track = driver.find_element(By.CLASS_NAME, "nc_track")
        
        # 获取滑块和轨道的宽度
        track_width = slider_track.size['width']
        block_width = slider_block.size['width']
        distance = track_width - block_width - 10  # 滑动距离
        
        print(f"[{datetime.now()}] 🔄 正在滑动验证条，距离: {distance}px...")
        
        # 执行滑动
        actions = ActionChains(driver)
        actions.click_and_hold(slider_block).move_by_offset(distance, 0).release().perform()
        
        time.sleep(2)
        
        # 检查验证是否通过
        if driver.find_elements(By.CLASS_NAME, "nc_success"):
            print(f"[{datetime.now()}] ✅ 滑块验证通过！")
        else:
            print(f"[{datetime.now()}] ⚠️ 验证可能未通过，继续尝试...")
        
    except Exception as e:
        print(f"[{datetime.now()}] ⚠️ 未检测到滑块验证: {e}")
    
    time.sleep(2)
    
    # 点击签到按钮
    print(f"[{datetime.now()}] 正在点击签到按钮...")
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'el-button')]"))
    )
    button.click()
    
    time.sleep(2)
    print(f"[{datetime.now()}] ✅ 签到成功！")
    
except Exception as e:
    print(f"[{datetime.now()}] ❌ 错误: {e}")
    driver.save_screenshot('/tmp/error_screenshot.png')
    
finally:
    driver.quit()
