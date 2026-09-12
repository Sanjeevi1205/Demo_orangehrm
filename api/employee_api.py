import requests


class EmployeeAPI:

    BASE_URL = (
        "https://opensource-demo.orangehrmlive.com"
    )

    def get_employee_by_number(
            self,
            emp_number,
            cookie_value
    ):

        session = requests.Session()

        session.cookies.set(
            "orangehrm",
            cookie_value
        )

        response = session.get(
            f"{self.BASE_URL}/web/index.php/api/v2/pim/employees/{emp_number}"
        )

        return response