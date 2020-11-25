from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome('G:\\D\\PyProject\\Drivers\\chromedriver.exe')
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://automationpractice.com/index.php")

    def login(self, username="Rifleman59@yandex.ru", password="password"):
        wd = self.wd
        wd.find_element_by_link_text("Sign in").click()
        wd.implicitly_wait(10)
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_id("passwd").send_keys(password)
        wd.find_element_by_id("SubmitLogin").click()
        wd.implicitly_wait(10)
        wd.find_element_by_link_text("Sign out")

    def add_to_chart_after_login(self):
        wd = self.wd
        # go to Woman page
        wd.find_element_by_class_name("sf-with-ul").click()
        wd.implicitly_wait(10)
        # change view to "list mode"
        wd.find_element_by_class_name("icon-th-list").click()
        wd.find_element_by_link_text("Add to cart").click()
        wd.implicitly_wait(10)
        wd.find_element_by_link_text("Proceed to checkout").click()

    def destroy(self):
        wd = self.wd
        wd.quit()
