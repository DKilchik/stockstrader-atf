Feature: Login

@positive
Scenario: User can login the service
    Given user opens the login page
    When user enter valid username
    When user enter valid password
    When user click continue button
    Then home page should be opened

@negative
Scenario Outline: User pass wrong username and password into login form
    Given user opens the login page
    When user enter '<username>' username
    When user enter '<password>' password
    When user click continue button
    Then invalid credentials label should be present

  Examples:
        | username            | password  |
        | wrongUser@fake.mail | wrongPass |