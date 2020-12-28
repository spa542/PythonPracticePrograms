# Automation/Testing in Python
from selenium import webdriver

# Currently broken but can mess with later for testing purposes
firefox_browser = webdriver.Firefox('./geckodriver')

firefox_browser.maximize_window()
firefox_browser.get('place url here')

assert 'Selenium Easy EDemo' in firefox_browser.title
show_message_button = firefox_browser.find_element_by_class_name()

assert 'Show Message' in firefox_browser.page_source

user_message = firefox_browser.find_element_by_id('user-message')
user_button2 = firefox_browser.find_element_by_id('#getme')
print(user_button2)
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

show_message_button.click()
output_message = firefox_browser.find_element_by_id('display')

asser 'I AM EXTRA COOOL' in output_message.text

firefox_browser.quit()
