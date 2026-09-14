from playwright.sync_api import sync_playwright
import os


def before_scenario(context, scenario):

    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(
        headless=True,
        slow_mo=500
    )

    if os.path.exists("state.json"):

        context.browser_context = (
            context.browser.new_context(
                storage_state="state.json",
                viewport={
                    "width": 1920,
                    "height": 1080
                }
            )
        )

    else:

        context.browser_context = (
            context.browser.new_context(
                viewport={
                    "width": 1920,
                    "height": 1080
                }
            )
        )

    context.page = context.browser_context.new_page()

    context.page.set_default_timeout(60000)
    context.page.set_default_navigation_timeout(60000)


def after_scenario(context, scenario):

    if scenario.status == "failed":

        os.makedirs(
            "screenshots",
            exist_ok=True
        )

        screenshot_name = (
            f"{scenario.name}_{scenario.status}"
            .replace(" ", "_")
            .replace("/", "_")
        )

        if hasattr(context, "page"):

            print(
                f"Failed URL: {context.page.url}"
            )

            screenshot_path = (
                f"screenshots/{screenshot_name}.png"
            )

            context.page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(
                f"Screenshot saved: {screenshot_path}"
            )

    if hasattr(context, "browser_context"):
        context.browser_context.close()

    if hasattr(context, "browser"):
        context.browser.close()

    if hasattr(context, "playwright"):
        context.playwright.stop()