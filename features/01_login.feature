Feature: Login

  @smoke @login @smoke
  Scenario: Successful login with valid credentials
    Given User navigates to OrangeHRM login page
    When User logs in with valid credentials
    Then User should be redirected to the Dashboard
