from selenium import webdriver

wd = webdriver.Chrome('G:\\D\\PyProject\\Drivers\\chromedriver.exe')


def open_home_page():
    wd.get("http://automationpractice.com/index.php")


# wd.set_window_size(1920, 1080)
open_home_page()


def login(username="Rifleman59@yandex.ru", password="password"):
    wd.find_element_by_link_text("Sign in").click()
    wd.implicitly_wait(10)
    wd.find_element_by_name("email").send_keys(username)
    wd.find_element_by_id("passwd").send_keys(password)
    wd.find_element_by_id("SubmitLogin").click()
    wd.implicitly_wait(10)
    wd.find_element_by_link_text("Sign out")


login()


def add_to_chart_after_login():
    # go to Woman page
    wd.find_element_by_class_name("sf-with-ul").click()
    wd.implicitly_wait(10)
    # change view to "list mode"
    wd.find_element_by_class_name("icon-th-list").click()
    wd.find_element_by_link_text("Add to cart").click()
    wd.implicitly_wait(10)
    wd.find_element_by_link_text("Proceed to checkout").click()


add_to_chart_after_login()


def delete_goods_from_chart():
    wd.implicitly_wait(10)
    wd.find_element_by_class_name("cart_quantity_delete").click()


delete_goods_from_chart()

# def list_of_goods():
# find_list_of_goods = wd.find_element_by_link_text("Add to cart")
# dress_list = [find_list_of_goods]
# print(dress_list)
# list_of_goods()
wd.quit()
