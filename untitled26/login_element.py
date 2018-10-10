#coding=utf-8
from selenium import webdriver

def l_browser(self):
    self.a=webdriver.Chrome()
def l_inputUrl(self):
    self.a.get("http://192.168.1.208/wk/")
def l_inputUserName(self,userName):
    self.a.find_element_by_name("name").send_keys(userName)
def l_inputPasswd(self,passWord):
    self.a.find_element_by_name("password").send_keys(passWord)
def l_submit(self):
    self.a.find_element_by_name("submit").click()
def l_loginRightText(self):
    b=self.a.find_element_by_xpath("/html/body/div[5]/div[2]").text
    return b
def l_loginErrorText(self):
    c=self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset/div").text
    return c
