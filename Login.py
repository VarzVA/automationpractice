from selenium import webdriver


wd = webdriver.Chrome('G:\\D\\PyProject\\Drivers\\chromedriver.exe')
#wd.set_window_size(1920, 1080)
wd.get("http://automationpractice.com/index.php")
wd.find_element_by_link_text("Sign in").click()
wd.implicitly_wait(10)
wd.find_element_by_name("email").send_keys("Rifleman59@yandex.ru")
wd.find_element_by_id("passwd").send_keys("password")
wd.find_element_by_id("SubmitLogin").click()
wd.implicitly_wait(10)
wd.implicitly_wait(10)