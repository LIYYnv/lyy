import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactsPage(BaseAction):
    add_name = By.XPATH, "//*[@text='姓名']"
    add_phone = By.XPATH, "//*[@text='电话']"

    @allure.step(title="输入姓名")
    def input_name(self, text):
        allure.attach("输入", text, allure.attach_type.TEXT)
        self.input(self.add_name, text)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="输入号码")
    def input_phone(self, phone):
        allure.attach("输入", phone, allure.attach_type.TEXT)
        self.input(self.add_phone, phone)
        allure.attach("截图：", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)