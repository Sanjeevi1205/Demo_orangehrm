from behave import given, when, then

from api.employee_api import EmployeeAPI
from pages.employee_page import EmployeePage
from utils.constants import DASHBOARD_URL


@given("User is on the dashboard page")
def step_dashboard(context):

    context.page.goto(
        DASHBOARD_URL
    )

    context.employee_page = EmployeePage(
        context.page
    )


@when("User navigates to the PIM module")
def step_navigate_pim(context):

    context.employee_page.navigate_to_pim()


@when("User clicks the Add Employee button")
def step_click_add_employee(context):

    context.employee_page.click_add_employee()


@when("User enters employee details")
def step_enter_employee_details(context):

    context.employee_page.enter_employee_details()

    employee_data = (
        context.employee_page.get_employee_details()
    )

    context.first_name = (
        employee_data["first_name"]
    )

    context.middle_name = (
        employee_data["middle_name"]
    )

    context.last_name = (
        employee_data["last_name"]
    )

    context.employee_id = (
        employee_data["employee_id"]
    )

    print(
        f"First Name : {context.first_name}"
    )

    print(
        f"Middle Name : {context.middle_name}"
    )

    print(
        f"Last Name : {context.last_name}"
    )

    print(
        f"Employee ID : {context.employee_id}"
    )


@when("User clicks the Save button")
def step_click_save(context):

    context.employee_page.click_save()

@when("User updates personal details")
def step_update_personal_details(context):

    context.employee_page.update_personal_details()

    employee_data = (
        context.employee_page.get_employee_details()
    )

    context.other_id = (
        employee_data["other_id"]
    )

    context.driving_license = (
        employee_data["driving_license"]
    )

    context.nationality = (
        employee_data["nationality"]
    )

    context.marital_status = (
        employee_data["marital_status"]
    )

    context.gender = (
        employee_data["gender"]
    )

    context.license_expiry_date = (
        employee_data["license_expiry_date"]
    )

    print(
        f"Other ID : {context.other_id}"
    )

    print(
        f"Driving License : "
        f"{context.driving_license}"
    )

    print(
        f"License Expiry Date : "
        f"{context.license_expiry_date}"
    )

    print(
        f"Nationality : "
        f"{context.nationality}"
    )

    print(
        f"Marital Status : "
        f"{context.marital_status}"
    )

    print(
        f"Gender : "
        f"{context.gender}"
    )


@then("Employee should be created successfully")
def step_verify_created(context):

    context.employee_page.verify_employee_created()

    context.emp_number = (
        context.employee_page.get_emp_number()
    )

    print(
        f"Emp Number : "
        f"{context.emp_number}"
    )


@then("Personal details should be saved successfully")
def step_verify_personal_details_saved(context):

    context.employee_page.verify_personal_details_saved()


@then("Employee details should be verified through API")
def step_verify_employee_api(context):

    employee_api = EmployeeAPI()

    cookies = context.browser_context.cookies()

    orangehrm_cookie = None

    for cookie in cookies:

        if cookie["name"] == "orangehrm":

            orangehrm_cookie = cookie["value"]

            break

    print(
        "OrangeHRM Cookie :",
        orangehrm_cookie
    )

    print(
        "Emp Number :",
        context.emp_number
    )

    response = employee_api.get_employee_by_number(
        context.emp_number,
        orangehrm_cookie
    )

    print(
        "Status Code :",
        response.status_code
    )

    print(
        "Response :",
        response.text
    )

    assert response.status_code == 200, (
        f"Expected Status Code 200 "
        f"but got {response.status_code}"
    )

    response_json = response.json()

    assert "data" in response_json, (
        "Response does not contain data node"
    )

    employee = response_json["data"]

    assert employee is not None, (
        "Employee data is empty"
    )

    assert (
            str(employee.get("empNumber"))
            == str(context.emp_number)
    ), (
        f"Emp Number Mismatch. "
        f"Expected: {context.emp_number}, "
        f"Actual: {employee.get('empNumber')}"
    )

    assert (
            employee.get("employeeId")
            == context.employee_id
    ), (
        f"Employee ID Mismatch. "
        f"Expected: {context.employee_id}, "
        f"Actual: {employee.get('employeeId')}"
    )

    assert (
            employee.get("firstName")
            == context.first_name
    ), (
        f"First Name Mismatch. "
        f"Expected: {context.first_name}, "
        f"Actual: {employee.get('firstName')}"
    )

    assert (
            employee.get("middleName")
            == context.middle_name
    ), (
        f"Middle Name Mismatch. "
        f"Expected: {context.middle_name}, "
        f"Actual: {employee.get('middleName')}"
    )

    assert (
            employee.get("lastName")
            == context.last_name
    ), (
        f"Last Name Mismatch. "
        f"Expected: {context.last_name}, "
        f"Actual: {employee.get('lastName')}"
    )

    print(
        "Employee Found In API Response"
    )

    print(
        f"Emp Number : "
        f"{employee.get('empNumber')}"
    )

    print(
        f"Employee ID : "
        f"{employee.get('employeeId')}"
    )

    print(
        f"First Name : "
        f"{employee.get('firstName')}"
    )

    print(
        f"Middle Name : "
        f"{employee.get('middleName')}"
    )

    print(
        f"Last Name : "
        f"{employee.get('lastName')}"
    )

    print(
        "UI + API Validation Successful"
    )

# Update scenario

@when('User searches the employee "{employee_name}"')
def step_search_employee(
        context,
        employee_name
):

    context.employee_name = employee_name

    context.employee_page.search_employee(
        employee_name
    )

@when("User updates employee details")
def step_update_employee_details(context):

    context.emp_number = (
        context.employee_page.get_emp_number()
    )

    context.employee_page.update_employee_details()

    employee_data = (
        context.employee_page.get_updated_employee_details()
    )

    context.updated_dob = (
        employee_data["date_of_birth"]
    )

    context.updated_nationality = (
        employee_data["nationality"]
    )

    context.updated_marital_status = (
        employee_data["marital_status"]
    )

@then("Employee details should be updated successfully")
def step_verify_employee_updated(context):

    context.employee_page.verify_personal_details_saved()


@then("Updated employee details should be verified through API")
def step_verify_updated_employee_api(context):

    employee_api = EmployeeAPI()

    cookies = context.browser_context.cookies()

    orangehrm_cookie = None

    for cookie in cookies:

        if cookie["name"] == "orangehrm":

            orangehrm_cookie = (
                cookie["value"]
            )

            break

    response = (
        employee_api.get_employee_by_number(
            context.emp_number,
            orangehrm_cookie
        )
    )

    print(
        "Status Code :",
        response.status_code
    )

    assert response.status_code == 200

    employee = (
        response.json()["data"]
    )

    print(
        "Updated Employee Verified "
        "Through API"
    )

    print(
        f"Emp Number : "
        f"{employee.get('empNumber')}"
    )

    print(
        f"Employee ID : "
        f"{employee.get('employeeId')}"
    )

    print(
        f"First Name : "
        f"{employee.get('firstName')}"
    )

    print(
        f"Middle Name : "
        f"{employee.get('middleName')}"
    )

    print(
        f"Last Name : "
        f"{employee.get('lastName')}"
    )

# Delete Scenario

@when("User selects the employee record")
def step_select_employee_record(context):

    context.employee_page.select_employee_record()



@when("User clicks the Delete button")
def step_click_delete_button(context):

    context.employee_page.click_delete_button()


@when("User confirms the employee deletion")
def step_confirm_employee_deletion(context):

    context.employee_page.confirm_delete()


@then("Employee should be deleted successfully")
def step_verify_employee_deleted(context):

    context.employee_page.verify_employee_deleted()


@then("Deleted employee should not be available through API")
def step_verify_deleted_employee_api(context):

    employee_api = EmployeeAPI()

    cookies = context.browser_context.cookies()

    orangehrm_cookie = None

    for cookie in cookies:

        if cookie["name"] == "orangehrm":

            orangehrm_cookie = cookie["value"]

            break

    response = employee_api.get_employee_by_number(
        context.emp_number,
        orangehrm_cookie
    )

    print(
        f"Status Code : {response.status_code}"
    )

    print(
        f"Response : {response.text}"
    )

    assert response.status_code != 200, (
        f"Employee still exists in the system. "
        f"Status Code : {response.status_code}"
    )

    print(
        "Deleted Employee Not Available Through API"
    )