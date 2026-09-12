from Base_class.Lib_global import LibGlobal
from locators.login_locators import LoginLocators
from utils.wait_helper import WaitHelper


class LoginPage(LibGlobal):

    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):

        self.retry_enter_text(
            LoginLocators.USERNAME,
            username
        )

        self.retry_enter_text(
            LoginLocators.PASSWORD,
            password
        )

        self.retry_click(
            LoginLocators.LOGIN_BUTTON
        )

    def verify_login_successful(self):

        WaitHelper.wait_for_visible(
            self.page,
            LoginLocators.PROFILE_MENU
        )

        self.verify_visible(
            LoginLocators.PROFILE_MENU
        )