from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, value):
        self.page.locator(locator).fill(value)

    def wait_for_element(self, locator, timeout=30000):
        self.page.locator(locator).wait_for(
            state="visible",
            timeout=timeout
        )

    def verify_visible(self, locator):
        expect(
            self.page.locator(locator)
        ).to_be_visible()

