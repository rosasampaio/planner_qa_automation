from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login:
    '''
     do login as basic credentials
    '''
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    txt_expected = ''
    TEXT_BTN_LOGIN = "Simple Form Auth"
    
    def go_to_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2.25)
    
    
    def access_login_page(self):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Simple Form Auth")]'))
        )
        
        self.txt_expected =  element.text
        assert self.txt_expected == self.TEXT_BTN_LOGIN
        
        element.click()
        
    
    def set_email(self, email: str):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'email'))
        )
        element.send_keys(email)
        
    def set_password(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        element.send_keys("pa$$w0rd")
    
    def do_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="Log In"]'))
        )
        element.click()

    
    def verify_redirect_login_succefully(self, msg):
        page_after_redirect =  self.driver.page_source 
        assert msg in page_after_redirect, f'expected: {msg}'
        sleep(2)
        
    def __del__(self):
        self.driver.quit()
