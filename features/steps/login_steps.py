from behave import given, when, then

from pages.login_page import LoginPage
from utils.constants import (
    BASE_URL,
    USERNAME,
    PASSWORD
)


@given("User navigates to OrangeHRM login page")
def step_navigate_to_login_page(context):

    context.page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60000
    )

    context.login_page = LoginPage(
        context.page
    )


@when("User logs in with valid credentials")
def step_login(context):

    context.login_page.login(
        USERNAME,
        PASSWORD
    )


@then("User should be redirected to the Dashboard")
def step_verify_dashboard(context):

    context.login_page.verify_login_successful()

    context.browser_context.storage_state(
        path="state.json"
    )