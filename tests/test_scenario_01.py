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
from time import sleep
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.tag("scenario 01", "xpath")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Rosa Sampaio")
@allure.issue("AUTO-1234")
@allure.testcase("TCAUTO-4321")
def test_login():
    login = Login()
    login.do_login()


class Login:
    
    '''
    do login as basic credentials
    '''
    def do_login(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

        url = 'https://authenticationtest.com/'
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(2.25)

        # 01) Do the login

        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Simple Form Auth")]'))
        )
        txt_expected =  element.text

        element.click()

# driver.implicitly_wait(0.25)

# element.send_keys("")


# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "password-input"))
# )
# element.send_keys("")

# element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), " Sign in ")]'))
# )
# element.click()

# element.clear_field()

        assert txt_expected ==  "Simple Form Auth"
        sleep(30)
        driver.quit()
