from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert "Selenium Easy Demo" in chrome_browser.title
# if it return false, it will error out
# we will not be able to use .body to search but we can use selector

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))
# You can read innerHTML attribute to get source of the content of the element

assert 'Show Message' in chrome_browser.page_source
# page source is the html version of the entire html source code

# grab the input
user_messgae = chrome_browser.find_element_by_id('user-message')
user_messgae.clear()
user_messgae.send_keys('i am extra cool')
# send_keys: in the user_message send this keystrokes as if a user is typing
show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'testing testing' in output_message.text

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
# the class
# #get-input > .btn : id(get-input).btn

chrome_browser.close()
chrome_browser.quit()
