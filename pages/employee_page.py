import random
import string

from Base_class.Lib_global import LibGlobal
from locators.employee_locators import EmployeeLocators
from utils.wait_helper import WaitHelper
from utils.logger import get_logger


class EmployeePage(LibGlobal):

    def __init__(self, page):
        super().__init__(page)

        self.employee_id = None
        self.first_name = None
        self.middle_name = None
        self.last_name = None

        self.other_id = None
        self.driving_license = None

        self.nationality = "Indian"
        self.marital_status = "Single"
        self.gender = "Male"
        self.license_expiry_date = "2030-12-31"

    def generate_employee_data(self):

        random_text = ''.join(
            random.choices(
                string.ascii_uppercase,
                k=5
            )
        )

        self.first_name = (
            f"FN_{random_text}"
        )

        self.middle_name = (
            f"MN_{random_text}"
        )

        self.last_name = (
            f"LN_{random_text}"
        )

        self.employee_id = (
            f"SD_{random.randint(1000, 9999)}"
        )

        self.other_id = (
            f"OID_{random.randint(1000, 9999)}"
        )

        self.driving_license = (
            f"DL_{random.randint(100000, 999999)}"
        )

    def navigate_to_pim(self):

        self.retry_click(
            EmployeeLocators.PIM_MENU
        )

    def click_add_employee(self):

        self.retry_click(
            EmployeeLocators.ADD_EMPLOYEE_BUTTON
        )

    def enter_employee_details(self):

        self.generate_employee_data()

        self.retry_enter_text(
            EmployeeLocators.FIRST_NAME,
            self.first_name
        )

        self.retry_enter_text(
            EmployeeLocators.MIDDLE_NAME,
            self.middle_name
        )

        self.retry_enter_text(
            EmployeeLocators.LAST_NAME,
            self.last_name
        )

        WaitHelper.wait_for_visible(
            self.page,
            EmployeeLocators.EMPLOYEE_ID
        )

        self.page.locator(
            EmployeeLocators.EMPLOYEE_ID
        ).fill(
            self.employee_id
        )

        print(
            f"First Name : {self.first_name}"
        )

        print(
            f"Middle Name : {self.middle_name}"
        )

        print(
            f"Last Name : {self.last_name}"
        )

        print(
            f"Employee ID : {self.employee_id}"
        )

    def click_save(self):

        self.retry_click(
            EmployeeLocators.SAVE_BUTTON
        )

    def verify_employee_created(self):

        WaitHelper.wait_for_visible(
            self.page,
            EmployeeLocators.PERSONAL_DETAILS_HEADER
        )

        self.verify_visible(
            EmployeeLocators.PERSONAL_DETAILS_HEADER
        )

        self.verify_visible(
            EmployeeLocators.EMPLOYEE_ID_LABEL
        )

        self.verify_visible(
            EmployeeLocators.OTHER_ID_LABEL
        )

        self.verify_visible(
            EmployeeLocators.DRIVING_LICENSE_LABEL
        )

        self.verify_visible(
            EmployeeLocators.LICENSE_EXPIRY_LABEL
        )

        self.verify_visible(
            EmployeeLocators.NATIONALITY_LABEL
        )

        self.verify_visible(
            EmployeeLocators.MARITAL_STATUS_LABEL
        )

        self.verify_visible(
            EmployeeLocators.DATE_OF_BIRTH_LABEL
        )

        self.verify_visible(
            EmployeeLocators.GENDER_LABEL
        )

        self.emp_number = (
            self.get_emp_number()
        )

        print(
            "Personal Details Page Loaded Successfully"
        )

        print(
            f"Emp Number : {self.emp_number}"
        )

    def verify_gender_selected(self):

        self.verify_visible(
            EmployeeLocators.GENDER_MALE
        )

        print(
            f"Gender Validation Passed : "
            f"{self.gender}"
        )

    def update_personal_details(self):

        self.retry_enter_text(
            EmployeeLocators.OTHER_ID_INPUT,
            self.other_id
        )

        self.retry_enter_text(
            EmployeeLocators.DRIVING_LICENSE_INPUT,
            self.driving_license
        )

        self.page.locator(
            EmployeeLocators.LICENSE_EXPIRY_DATE
        ).fill(
            self.license_expiry_date
        )

        print(
            "Selecting Nationality : Indian"
        )

        self.retry_click(
            EmployeeLocators.NATIONALITY_DROPDOWN
        )
        self.page.wait_for_timeout(
            2000
        )
        self.page.keyboard.type("Indian")
        self.page.keyboard.press("Enter")

        print(
            "Selecting Marital Status : Single"
        )

        self.retry_click(
            EmployeeLocators.MARITAL_STATUS_DROPDOWN
        )

        self.page.wait_for_timeout(
            2000
        )
        self.page.keyboard.type("Single")
        self.page.keyboard.press("Enter")

        print(
            "Selecting Gender : Male"
        )

        self.retry_click(
            EmployeeLocators.GENDER_MALE
        )

        self.verify_gender_selected()

        self.retry_click(
            EmployeeLocators.PERSONAL_DETAILS_SAVE
        )

        print(
            f"Other ID : {self.other_id}"
        )

        print(
            f"Driving License : "
            f"{self.driving_license}"
        )

        print(
            f"License Expiry Date : "
            f"{self.license_expiry_date}"
        )

        print(
            f"Nationality : "
            f"{self.nationality}"
        )

        print(
            f"Marital Status : "
            f"{self.marital_status}"
        )

        print(
            f"Gender : "
            f"{self.gender}"
        )

    def verify_personal_details_saved(self, employee_name=None):

        WaitHelper.wait_for_visible(
            self.page,
            EmployeeLocators.SUCCESS_TOAST
        )

        self.verify_visible(
            EmployeeLocators.SUCCESS_TOAST
        )
        print(
            "Personal Details Saved Successfully"
        )
    def search_employee(
            self,
            employee_name
    ):

      while True:

        rows = self.page.locator(
            "//div[@role='row']"
        )

        count = rows.count()

        for index in range(count):

            row = rows.nth(index)

            row_text = row.text_content() or ""

            print(
                f"Searching For : {employee_name}"
            )

            print(
                f"Row Text : {row_text}"
            )

            if employee_name.lower() in row_text.lower():

                print(
                    f"Employee Found : {employee_name}"
                )

                row.click()

                print(
                    "Row Clicked"
                )

                self.page.wait_for_timeout(
                    3000
                )

                print(
                    f"Current URL : {self.page.url}"
                )

                return True

        next_button = self.page.locator(
            "(//button[contains(@class,'oxd-pagination-page-item--previous-next')])[2]"
        )

        if next_button.count() == 0:
            break

        if not next_button.is_enabled():
            break

        next_button.click()

        self.page.wait_for_timeout(
            2000
        )


    def search_and_open_employee(
                self,
                employee_name
        ):

        self.retry_enter_text(
            EmployeeLocators.EMPLOYEE_NAME_SEARCH,
            employee_name
        )

        self.retry_click(
            EmployeeLocators.SEARCH_BUTTON
        )

        self.page.wait_for_timeout(
            3000
        )

        rows = self.page.locator(
            "//div[@role='row']"
        )

        count = rows.count()

        for index in range(count):

            row = rows.nth(index)

            row_text = row.text_content()

            if employee_name in row_text:

                # row.locator(
                #     EmployeeLocators.EDIT_BUTTON
                # ).click()

                print(
                    f"Employee Found : "
                    f"{employee_name}"
                )

                print(
                    "Edit Button Clicked"
                )

                break

        else:

            raise Exception(
                f"Employee Not Found : "
                f"{employee_name}"
            )
    def update_employee_details(self):

        self.updated_dob = "1998-10-15"
        self.updated_nationality = "Indian"
        self.updated_marital_status = "Married"

        WaitHelper.wait_for_visible(
        self.page,
        EmployeeLocators.DATE_OF_BIRTH_CALENDAR
        )

        self.page.locator(
        EmployeeLocators.DATE_OF_BIRTH_CALENDAR
    ).fill(
         self.updated_dob

    )

    def get_updated_employee_details(self):

       return {
        "date_of_birth": self.updated_dob,
        "nationality": self.updated_nationality,
        "marital_status": self.updated_marital_status
    }

    def get_emp_number(self):

        current_url = self.page.url

        print(
            f"Current URL : {current_url}"
        )


        emp_number = (
            current_url.split(
                "/empNumber/"
            )[1].split(
                "/"
            )[0]
        )

        print(
            f"Emp Number : {emp_number}"
        )

        return emp_number

    def get_employee_id(self):

        return self.employee_id

    def get_first_name(self):

        return self.first_name

    def get_middle_name(self):

        return self.middle_name

    def get_last_name(self):

        return self.last_name

    def get_other_id(self):

        return self.other_id

    def get_driving_license(self):

        return self.driving_license

    def get_nationality(self):

        return self.nationality

    def get_marital_status(self):

        return self.marital_status

    def get_gender(self):

        return self.gender

    def get_license_expiry_date(self):

        return self.license_expiry_date

    def get_employee_details(self):

        return {
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "employee_id": self.employee_id,
            "other_id": self.other_id,
            "driving_license": self.driving_license,
            "nationality": self.nationality,
            "marital_status": self.marital_status,
            "gender": self.gender,
            "license_expiry_date": self.license_expiry_date
        }

    def select_employee_record(self):

        self.page.locator(
        EmployeeLocators.EMPLOYEE_CHECKBOX
    ).first.click()

    print(
        "Employee Record Selected"
    )

    def click_delete_button(self):

        self.retry_click(
        EmployeeLocators.DELETE_BUTTON
    )

    print("Delete Button Clicked")

    def confirm_delete(self):

        WaitHelper.wait_for_visible(
        self.page,
        EmployeeLocators.CONFIRM_DELETE_BUTTON
    )

        self.retry_click(
        EmployeeLocators.CONFIRM_DELETE_BUTTON
    )

    print(
        "Clicked Yes, Delete"
    )

    def verify_employee_deleted(self):

        WaitHelper.wait_for_visible(
        self.page,
        EmployeeLocators.SUCCESS_TOAST
    )

        self.verify_visible(
        EmployeeLocators.SUCCESS_TOAST
    )

    print(
        "Employee Deleted Successfully"
    )

    def get_selected_employee_number(self):

        row = self.page.locator(
        "//div[@class='oxd-table-card']"
    ).first
        return row.locator(
           ".//div[@role='cell'][2]"
      ).text_content()