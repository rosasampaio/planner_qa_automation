'''
 1. GO TO  the web system: https://authenticationtest.com/
 2.  with the right button on any place from the webpage
 3. select inspect
 4. select console
 5. click in the first button in the console header & click on the element in th page:
 6. so, the element will be highlight  on console:
    # click above with right button;
    # choose Copy;
    # choose XPath
'''
import pytest  
from functools import partial
from pytest_bdd import scenarios, scenario, given, when, parsers, step
import allure
from src.models.login import Login

scenarios("../features/test_scenario_01.feature")  

login = Login()
  
EXTRA_TYPES = {
    'Number': int,
    "String": str
}

parser_new_types = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

@pytest.fixture 
def users():
    return {"email": "simpleForm@authenticationtest.com",
            "password": "pa$$w0rd"
            } 
  
@allure.tag("scenario 01", "xpath")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Rosa Sampaio")
@allure.issue("AUTO-1234")
@allure.testcase("TCAUTO-4321")
@given(parser_new_types('access the general page in "{url:String}"'))
def general_page(url):
    login.go_to_url(url=url)


@given("acess the login page")
def login_page():
    login.access_login_page()


@given(parser_new_types('set the email to "{email:String}"'))
def set_email(email):
    login.set_email(email)
 
    
@given('set the password')
def set_password():
    login.set_password()


@when('do the login')
def do_login():
    login.do_login()

@step(parser_new_types('the page should contains the msg "{msg:String}"'))
def verify_redirect_login_successfully(msg):
    login.verify_redirect_login_succefully(msg)
    