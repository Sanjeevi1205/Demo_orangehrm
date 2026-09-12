Feature: Employee Management

  @employee @create @smoke
  Scenario: Create employee successfully

    Given User is on the dashboard page
    When User navigates to the PIM module
    And User clicks the Add Employee button
    And User enters employee details
    And User clicks the Save button
    Then Employee should be created successfully
    When User updates personal details
    Then Personal details should be saved successfully
    And Employee details should be verified through API


  @employee @update @smoke
  Scenario Outline: Update employee successfully

    Given User is on the dashboard page
    When User navigates to the PIM module
    And User searches the employee "<EmployeeName>"
    And User updates employee details
    And User clicks the Save button
    Then Employee details should be updated successfully
    And Updated employee details should be verified through API

    Examples:
      | EmployeeName |
      | Jobin MathewSam |


  @employee @delete @smoke
  Scenario Outline: Delete employee successfully

    Given User is on the dashboard page
    When User navigates to the PIM module
    And User searches the employee "<EmployeeName>"
    And User selects the employee record
    And User clicks the Delete button
    And User confirms the employee deletion
    Then Employee should be deleted successfully

    Examples:
      | EmployeeName |
      | charles     |