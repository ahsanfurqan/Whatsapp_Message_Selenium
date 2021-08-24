import sys,time
from flask import jsonify
from datetime import date,datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pywhatkit
# current=datetime.now()
# hour=int(current.strftime("%H"))
# minute=int(current.strftime('%M'))
msg='Hello from bot made by ahsan'
#number={'+923362394601'}
# pywhatkit.sendwhatmsg('+923362394601',msg,hour,minute+1)
options=webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\AALIYAN'Z COMPUTER\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument('--profile-directory=Default')

chrome_browser=webdriver.Chrome(executable_path=r'D:\Whatsapp_api\chromedriver_win32\chromedriver.exe',options=options)
chrome_browser.get('https://web.whatsapp.com/')
# chrome_browser.get('https://wa.me/923363017073/?text=hello&app_absent=0')
time.sleep(5)
# messagebox=chrome_browser.find_element_by_xpath('//a[@class="_36or _2y_c _2z0c _2z07"]')
# messagebox.click()
# time.sleep(5)
# messagebox=chrome_browser.find_element_by_xpath('//a[@class="_36or"]')
# messagebox.click()
# time.sleep(10)
user_name_list=['Daim Boss']

for user_name in user_name_list:
    try:
        user=chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        pass
    time.sleep(2)
    message_box=chrome_browser.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"][@data-tab="6"]')
    time.sleep(2)
    message_box.send_keys(msg)
    time.sleep(1)
    message_box = chrome_browser.find_element_by_xpath('//button[@class="_4sWnG"]')
    message_box.click()
    time.sleep(2)
