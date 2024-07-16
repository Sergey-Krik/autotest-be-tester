#$$$$$$$$$$$$$    Shop: отображение страницы товара
import time

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
# user_name = driver.find_element_by_id("username").send_keys("krikliviy.serg@yandex.ru")
# password_user = driver.find_element_by_id("password").send_keys("tilt729181ss")
# login = driver.find_element_by_name("login").click()
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# HTML5_Forms = driver.find_element_by_css_selector(".post-181 > a > h3").click()
#
# HTML5_Forms_text = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".product_title"),"HTML5 Forms"))
#
# driver.quit()



#######$$$$$$$$$$$$$$$ Shop: количество товаров в категории


# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://practice.automationtesting.in")
#
# My_Account = driver.find_element_by_id("menu-item-50").click()
#
# user_name = driver.find_element_by_id("username").send_keys("krikliviy.serg@yandex.ru")
# password_user = driver.find_element_by_id("password").send_keys("tilt729181ss")
# login = driver.find_element_by_name("login").click()
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# HTML_buton = driver.find_element_by_link_text("HTML").click()
#
# number_book = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(number_book) ==3:
#     print("В разделе три книги")
# else:
#     print("Ошибка.Количество книг в разделе:" + str(len(number_book)))
#
# driver.quit()





# $$$$$$$$$$$$$$$$$$$  Shop: сортировка товаров
# from selenium.webdriver.support.select import (Select)
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://practice.automationtesting.in")
#
# My_Account = driver.find_element_by_id("menu-item-50").click()
#
# user_name = driver.find_element_by_id("username").send_keys("krikliviy.serg@yandex.ru")
# password_user = driver.find_element_by_id("password").send_keys("tilt729181ss")
# login = driver.find_element_by_name("login").click()
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# select_sc = driver.find_element_by_css_selector(".orderby")
# select_default = select_sc.get_attribute("value")
# if select_default == "menu_order":
#     print("Сортировка по умолчанию")
# else:
#     print("Сортирока не по умолчанию")
#
#
# select = Select(select_sc)
# select.select_by_value("price-desc")
#
# select_sc = driver.find_element_by_css_selector(".orderby")
# select_sorting = select_sc.get_attribute("value")
# if select_sorting == "price-desc":
#     print("Сортировка по убыванию")
# else:
#     print("Сортировка не по убыванию")
#
# driver.quit()




# $$$$$$$$$$$$$$$$$$$$$$Shop: отображение, скидка товара

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://practice.automationtesting.in")
#
# My_Account = driver.find_element_by_id("menu-item-50").click()
#
# user_name = driver.find_element_by_id("username").send_keys("krikliviy.serg@yandex.ru")
# password_user = driver.find_element_by_id("password").send_keys("tilt729181ss")
# login = driver.find_element_by_name("login").click()
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# Android_book = driver.find_element_by_partial_link_text("Android Quick Start Guide").click()
#
# old_price = driver.find_element_by_css_selector("p > del > span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
#
# new_price = driver.find_element_by_css_selector("p > ins > span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
#
# book_cover = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".images > a"))).click()
#
# close_book_cover = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close"))).click()
#
# driver.quit()



#$$$$$$$$$$$$$$$$$$$$$$ Shop: проверка цены в корзине

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://practice.automationtesting.in")
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# HTML5_WebApp_Develpment_book = driver.find_element_by_css_selector(".post-182 .ajax_add_to_cart").click()
#
# time.sleep(5)
# product = driver.find_element_by_css_selector(".cartcontents")
# product_text= product.text
# assert product_text == "1 Item", "Ошибка в количестве товара"
#
# price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# price_text = price.text
# assert price_text == "₹180.00", "Ошибка в цене товара"
#
# basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
#
# subtotal_price = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cart-subtotal .woocommerce-Price-amount"),"₹180.00"))
#
# total_price = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".order-total .woocommerce-Price-amount "),"₹183.60"))
#
# driver.quit()




# $$$$$$$$$$$$$$$$$ Shop: работа в корзине


# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://practice.automationtesting.in")
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# driver.execute_script("window. scrollBy(0,300)")
#
# HTML5_WebApp_Develpment_book = driver.find_element_by_css_selector(".post-182 .ajax_add_to_cart").click()
# time.sleep(5)
# js_book = driver.find_element_by_css_selector(".post-180 .ajax_add_to_cart").click()
#
# basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
# time.sleep(5)
#
# remove = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .remove").click()
#
# undo = driver.find_element_by_link_text("Undo?").click()
#
# quantity = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
# quantity.clear()
# quantity.send_keys("3")
#
# update_basket = driver.find_element_by_name("update_cart").click()
#
# quantity_value = quantity.get_attribute("value")
# assert quantity_value == "3", "Ошибка в количестве книг"
# time.sleep(5)
#
# apply_coupon = driver.find_element_by_css_selector(".coupon .button").click()
#
# coupon_code = driver.find_element_by_css_selector(".woocommerce-error")
# coupon_code_text = coupon_code.text
# assert coupon_code_text == "Please enter a coupon code."
#
# driver.quit()



#$$$$$$$$$$$$$$ Shop: покупка товара


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(20)
# driver.get("https://practice.automationtesting.in")
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window. scrollBy(0,300)")
#
# HTML5_WebApp_Develpment_book = driver.find_element_by_css_selector(".post-182 .ajax_add_to_cart").click()
# time.sleep(5)
# basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
#
# proceed_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".checkout-button")))
# proceed_btn.click()
#
# first_name = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"billing_first_name")))
# first_name.send_keys("Jon")
#
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("jones")
#
# email=driver.find_element_by_id("billing_email").send_keys("jon@yandex.ru")
# phone = driver.find_element_by_id("billing_phone").send_keys("89009009090")
#
# country_selector = driver.find_element_by_id("s2id_billing_country").click()
# country_search = driver.find_element_by_id("s2id_autogen1_search").send_keys("american ")
# country = driver.find_element_by_css_selector(".select2-match").click()
#
# driver.execute_script("window. scrollBy(0,300)")
#
# address = driver.find_element_by_id("billing_address_1").send_keys("LINCOLN AVE")
# city = driver.find_element_by_id("billing_city").send_keys("Pago Pago")
#
# zip = driver.find_element_by_id("billing_postcode").send_keys("96799")
# state = driver.find_element_by_id("billing_state").send_keys("Pago Pago")
#
# driver.execute_script("window. scrollBy(0,1100)")
# time.sleep(3)
#
# check_payments = driver.find_element_by_id("payment_method_cheque").click()
#
# place_order_btn = driver.find_element_by_id("place_order").click()
#
# order_text = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
# payment_method = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"tfoot > tr:nth-child(3) > td"),"Check Payments"))
#
# driver.quit()


#7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep --- у меня не выидны элементы поэтому пришлось 2 раза проскроливать страницу


