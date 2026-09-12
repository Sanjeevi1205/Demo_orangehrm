class WaitHelper:

    DEFAULT_TIMEOUT = 60000

    @staticmethod
    def wait_for_visible(
            page,
            locator,
            timeout=DEFAULT_TIMEOUT
    ):

        page.locator(locator).wait_for(
            state="visible",
            timeout=timeout
        )

    @staticmethod
    def wait_for_hidden(
            page,
            locator,
            timeout=DEFAULT_TIMEOUT
    ):

        page.locator(locator).wait_for(
            state="hidden",
            timeout=timeout
        )

    @staticmethod
    def wait_for_url(
            page,
            url,
            timeout=DEFAULT_TIMEOUT
    ):

        page.wait_for_url(
            url,
            timeout=timeout
        )

    @staticmethod
    def wait_for_load(page):

        page.wait_for_load_state(
            "networkidle"
        )

