from selenium import webdriver


wd = webdriver.Chrome('G:\\D\\PyProject\\Drivers\\chromedriver.exe')


def open_home_page():
    wd.get("http://automationpractice.com/index.php")
#wd.set_window_size(1920, 1080)
open_home_page()

def login():
    wd.find_element_by_link_text("Sign in").click()
    wd.implicitly_wait(10)
    wd.find_element_by_name("email").send_keys("Rifleman59@yandex.ru")
    wd.find_element_by_id("passwd").send_keys("password")
    wd.find_element_by_id("SubmitLogin").click()
    wd.implicitly_wait(10)
    wd.find_element_by_link_text("Sign out")
login()

def add_to_chart_after_login():
    #go to Woman page
    wd.find_element_by_class_name("sf-with-ul").click()
    wd.implicitly_wait(10)
    #change view to "list mode"
    wd.find_element_by_class_name("icon-th-list").click()

    def list_of_goods():
        find_list_of_goods = wd.find_elements_by_tag_name("data-id-product")
        #dress_list = ["find_list_of_goods"]
        print(find_list_of_goods)
    list_of_goods()

add_to_chart_after_login()