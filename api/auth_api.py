import requests


class AuthAPI:

    def verify_login_api(self):

        response = requests.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        return response