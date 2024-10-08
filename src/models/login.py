from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        )
        element.send_keys("simpleForm@authenticationtest.com")

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        element.send_keys("pa$$w0rd")

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="Log In"]'))
        )
        element.click()

        assert txt_expected == "Simple Form Auth"
        
        page_after_redirect =  driver.page_source 
        assert 'Login Success' in page_after_redirect
        assert 'You are now logged in!' in page_after_redirect
        
        sleep(5)
        driver.quit()
