# GO TO  the web system: https://authenticationtest.com/
# testing by image

from src.models.loginByImg import LoginByIMG
import allure

@allure.tag("scenario 01", "xpath")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Rosa Sampaio")
@allure.issue("AUTO-1233")
@allure.testcase("TCAUTO-4322")
def test_login():
    login = LoginByIMG()
    login.do_login_by_img()
    
    
if __name__ == '__main__':
    test_login()