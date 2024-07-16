#####################################Registration_login: регистрация аккаунта


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in")
#
# My_Account = driver.find_element_by_id("menu-item-50").click()
#
# email_reg = driver.find_element_by_id("reg_email").send_keys("krikliviy.serg@yandex.ru")
# password_reg = driver.find_element_by_id("reg_password").send_keys("tilt729181ss")
#
# text = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".strong"),"Strong"))
#
#
# register = driver.find_element_by_name("register").click()




################################## Registration_login: логин в систему


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in")
#
# My_Account = driver.find_element_by_id("menu-item-50").click()
#
# user_name = driver.find_element_by_id("username").send_keys("krikliviy.serg@yandex.ru")
#
# password_user = driver.find_element_by_id("password").send_keys("tilt729181ss")
#
# login = driver.find_element_by_name("login").click()
#
# driver.find_element_by_link_text("Logout")
#
# driver.quit()