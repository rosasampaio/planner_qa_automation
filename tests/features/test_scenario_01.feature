Feature: Do the login traditional approach
    Tests related to Login 

    @login
    Scenario: Do the login as basic credentials
        Given access the general page in "https://authenticationtest.com/"
        And acess the login page
        And set the email to "simpleForm@authenticationtest.com"
        And set the password
        When do the login 
        Then the page should contains the msg "Login Success"
        And the page should contains the msg "You are now logged in!"
