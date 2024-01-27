from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/path/to/chromedriver')  # Thay thế với đường dẫn đến ChromeDriver

# Điều hướng đến ứng dụng của bạn
driver.get('http://localhost:8080')  # Thay thế với URL của ứng dụng 
# Tìm thẻ input
input_element = driver.find_element_by_id('myInput')

# Nhập công việc mới
input_element.send_keys('New ToDo Item')

# Nhấn nút 'Add'
add_button = driver.find_element_by_xpath('//button[normalize-space()="Add"]')
add_button.click()

# Chờ một chút để công việc được thêm
time.sleep(2)

# Kiểm tra xem có công việc mới không
todos = driver.find_element_by_id('myUL').text
assert 'New ToDo Item' in todos

# Tắt trình duyệt
driver.quit()
