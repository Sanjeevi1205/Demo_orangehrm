import time
from playwright.sync_api import expect


class LibGlobal:

    def __init__(self, page):
        self.page = page

    # Navigation
    def navigate(self, url):
        self.page.goto(url)

    # Click
    def click(self, locator):
        self.page.locator(locator).click()

    # Retry Click
    def retry_click(
            self,
            locator,
            retry_count=3,
            delay=2
    ):

        attempt = 0

        while attempt < retry_count:

            try:

                self.page.locator(locator).click(
                    timeout=60000,
                    no_wait_after=True
                )

                return

            except Exception as e:

                attempt += 1

                print(
                    f"Click attempt {attempt} failed: {e}"
                )

                if attempt >= retry_count:
                    raise

                time.sleep(delay)

    # Enter Text
    def enter_text(self, locator, value):
        self.page.locator(locator).fill(value)

    # Retry Enter Text
    def retry_enter_text(
            self,
            locator,
            value,
            retry_count=3,
            delay=2
    ):

        attempt = 0

        while attempt < retry_count:

            try:

                self.page.locator(locator).fill(
                    value,
                    timeout=60000
                )

                return

            except Exception as e:

                attempt += 1

                print(
                    f"Fill attempt {attempt} failed: {e}"
                )

                if attempt >= retry_count:
                    raise

                time.sleep(delay)

    # Get Text
    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    # Wait Visible
    def wait_for_element(
            self,
            locator,
            timeout=30000
    ):

        self.page.locator(locator).wait_for(
            state="visible",
            timeout=timeout
        )

    # Wait Hidden
    def wait_for_hidden(
            self,
            locator
    ):

        self.page.locator(locator).wait_for(
            state="hidden"
        )

    # Visibility
    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    # Verify Visible
    def verify_visible(self, locator):

        expect(
            self.page.locator(locator)
        ).to_be_visible()

    # Verify Text
    def verify_text(
            self,
            locator,
            expected_text
    ):

        expect(
            self.page.locator(locator)
        ).to_have_text(expected_text)

    # URL Validation
    def verify_url_contains(self, value):

        assert value in self.page.url

    # Current URL
    def get_current_url(self):

        return self.page.url

    # Page Title
    def get_title(self):

        return self.page.title()

    # Wait for Page Load
    def wait_for_page_load(self):

        self.page.wait_for_load_state(
            "networkidle"
        )

    # Scroll Element
    def scroll_to_element(self, locator):

        self.page.locator(
            locator
        ).scroll_into_view_if_needed()

    # Hover
    def hover(self, locator):

        self.page.locator(locator).hover()

    # Double Click
    def double_click(self, locator):

        self.page.locator(locator).dblclick()

    # Keyboard Action
    def press_key(
            self,
            locator,
            key
    ):

        self.page.locator(locator).press(key)

    # Dropdown
    def select_option(
            self,
            locator,
            value
    ):

        self.page.locator(locator).select_option(
            value
        )

    # Checkbox Check
    def check(self, locator):

        self.page.locator(locator).check()

    # Checkbox Uncheck
    def uncheck(self, locator):

        self.page.locator(locator).uncheck()

    # Frame Handling
    def switch_to_frame(
            self,
            frame_name
    ):

        return self.page.frame(
            name=frame_name
        )

    # JavaScript Click
    def js_click(self, locator):

        self.page.locator(locator).evaluate(
            "element => element.click()"
        )

    # JavaScript Scroll Bottom
    def js_scroll_bottom(self):

        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    # Screenshot
    def take_screenshot(
            self,
            file_name
    ):

        self.page.screenshot(
            path=f"screenshots/{file_name}.png"
        )

