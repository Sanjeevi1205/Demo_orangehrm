class EmployeeLocators:

    # PIM Menu

    PIM_MENU = (
        "//span[text()='PIM']"
    )

    # Add Employee

    ADD_EMPLOYEE_BUTTON = (
        "//a[text()='Add Employee']"
    )

    # Employee Details

    FIRST_NAME = (
        "input[name='firstName']"
    )

    MIDDLE_NAME = (
        "input[name='middleName']"
    )

    LAST_NAME = (
        "input[name='lastName']"
    )

    EMPLOYEE_ID = (
        "(//input[contains(@class,'oxd-input')])[5]"
    )

    # Common Save Button

    SAVE_BUTTON = (
        "//button[@type='submit']"
    )

    # Personal Details Header

    PERSONAL_DETAILS_HEADER = (
        "//h6[text()='Personal Details']"
    )

    # Labels

    EMPLOYEE_ID_LABEL = (
        "//label[text()='Employee Id']"
    )

    OTHER_ID_LABEL = (
        "//label[text()='Other Id']"
    )

    DRIVING_LICENSE_LABEL = (
        "//label[contains(text(),\"Driver's License Number\")]"
    )

    LICENSE_EXPIRY_LABEL = (
        "//label[contains(text(),'License Expiry Date')]"
    )

    NATIONALITY_LABEL = (
        "//label[contains(text(),'Nationality')]"
    )

    MARITAL_STATUS_LABEL = (
        "//label[contains(text(),'Marital Status')]"
    )

    DATE_OF_BIRTH_LABEL = (
        "//label[contains(text(),'Date of Birth')]"
    )

    GENDER_LABEL = (
        "//label[contains(text(),'Gender')]"
    )

    # Personal Details Inputs

    OTHER_ID_INPUT = (
        "//label[text()='Other Id']/../following-sibling::div//input"
    )

    DRIVING_LICENSE_INPUT = (
        "//label[contains(text(),\"Driver's License Number\")]/../following-sibling::div//input"
    )

    LICENSE_EXPIRY_DATE = (
        "(//input[@placeholder='yyyy-dd-mm'])[1]"
    )

    DATE_OF_BIRTH_INPUT = (
        "(//input[@placeholder='yyyy-dd-mm'])[2]"
    )

    # Nationality

    NATIONALITY_DROPDOWN = (
        "(//div[contains(@class,'oxd-select-text')])[1]"
    )

    INDIAN_OPTION = (
        "//div[@role='option'][.//span[normalize-space()='Indian']]"
    )

    SELECTED_NATIONALITY = (
        "//label[text()='Nationality']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text-input')]"
    )

    # Marital Status

    MARITAL_STATUS_DROPDOWN = (
        "(//div[contains(@class,'oxd-select-text')])[2]"
    )

    SINGLE_OPTION = (
        "//div[@role='option'][.//span[normalize-space()='Single']]"
    )

    SELECTED_MARITAL_STATUS = (
        "//label[text()='Marital Status']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text-input')]"
    )

    # Gender

    GENDER_MALE = (
        "//label[normalize-space()='Male']"
    )

    GENDER_FEMALE = (
        "//label[normalize-space()='Female']"
    )

    GENDER_MALE_RADIO = (
        "//label[normalize-space()='Male']/preceding-sibling::input"
    )

    GENDER_FEMALE_RADIO = (
        "//label[normalize-space()='Female']/preceding-sibling::input"
    )

    # Personal Details Save

    PERSONAL_DETAILS_SAVE = (
        "(//button[@type='submit'])[1]"
    )

    # Success Message

    SUCCESS_TOAST = (
        "//div[contains(@class,'oxd-toast-content')]"
    )

    # ------------------------------------------------
    # UPDATE EMPLOYEE LOCATORS
    # ------------------------------------------------

    EMPLOYEE_NAME_SEARCH = (
        "//input[@placeholder='Type for hints...']"
    )

    SEARCH_BUTTON = (
        "//button[@type='submit']"
    )

    EDIT_BUTTON = (
        "//button[@type='button']"
    )

    DATE_OF_BIRTH_CALENDAR = (
        "//label[text()='Date of Birth']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    SAVE_BUTTON = "(//button[@type='submit'])[2]"


# Delete Employee

    EMPLOYEE_CHECKBOX = (
    "//div[@class='oxd-table-card']//span[contains(@class,'oxd-checkbox-input')]"
      )

    DELETE_BUTTON = (
        "//button[contains(@class,'oxd-button--label-danger')]"
     )

    CONFIRM_DELETE_BUTTON = (
    "//button[normalize-space()='Yes, Delete']"
     )