from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import os
import pyperclip


class LoginByIMG:
    '''
     do login as basic credentials
    '''
    project_dir = os.getcwd()
    img_dir_home = 'src/pageObjects/home/img'
    img_dir_login = 'src/pageObjects/login/img'

     
    def do_login_by_img(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

        url = 'https://authenticationtest.com/'
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(2.25)
        sleep(2) # waiting for the page load
      
        # 01 -> Do the login
        img = 'image_01.png'
        self.click_by_img(self.img_dir_home, img)    
        sleep(2)
        page_after_redirect =  driver.page_source 
        assert 'How to log in:' in page_after_redirect

        img = 'image_02.png'
        self.click_by_img(self.img_dir_login, img)   
        pyperclip.copy('simpleForm@authenticationtest.com')
        pyautogui.hotkey('ctrl', 'v')

       
        img = 'image_03.png'
        self.click_by_img(self.img_dir_login, img) 
        pyautogui.typewrite("pa$$w0rd")
      
        img = 'image_04.png'
        self.click_by_img(self.img_dir_login, img) 

        page_after_redirect =  driver.page_source 
        assert 'Login Success' in page_after_redirect
        assert 'You are now logged in!' in page_after_redirect
        
        sleep(3)
        driver.quit()
    
    
    def click_by_img(self,img_dir, img):
        file = os.path.join(self.project_dir, img_dir, img)
        location_of_el = pyautogui.locateOnScreen(file, confidence=0.8)      
        button = pyautogui.center(location_of_el)
        button7x, button7y = button
        pyautogui.click(button7x, button7y)
        
