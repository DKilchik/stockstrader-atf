Feature: Login

Scenario: User login the service
    Given user opens the login page
    When user enter valid username
    When user enter valid password
    When user click continue button
    Then home page should be opened