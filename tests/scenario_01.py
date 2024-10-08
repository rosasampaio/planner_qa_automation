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
from src.models.login import Login
import allure

@allure.tag("scenario 01", "xpath")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Rosa Sampaio")
@allure.issue("AUTO-1234")
@allure.testcase("TCAUTO-4321")
def test_login():
    login = Login()
    login.do_login()

