#coding=utf-8
from login_element import l_browser,l_inputUserName,l_inputUrl,l_submit,l_inputPasswd
from login_judge import loginError,loginNull,loginRiht,loginOften
from public import readExcel
from unittest import TestCase#导入unittest框架的TestCase类

class login(TestCase):#继承unittest框架的TestCase类
    @classmethod
    def setUp(self):  #setUp是TestCase类中定义的，如果遇到叫setUp名字的方法，每次都会先执行
        l_browser(self)
        l_inputUrl(self)

    @classmethod
    def case001(self):#TestCase类定义了，如果遇到叫test开头的方法就会在setUp方法只会依次按顺序运行
        l_inputUserName(self,readExcel("login",1,2))
        l_inputPasswd(self,int(readExcel("login",1,3)))
        l_submit(self)
        assert loginRiht(self)

    def case002(self):
        l_inputUserName(self,readExcel("login",2,2))
        l_inputPasswd(self,int(readExcel("login",2,3)))
        l_submit(self)
        assert loginRiht(self)

    def case003(self):
        l_inputUserName(self,readExcel("login",3,2))
        l_inputPasswd(self,int(readExcel("login",3,3)))
        l_submit(self)
        assert loginError(self)

    def case004(self):
        l_inputUserName(self,readExcel("login",4,2))
        l_inputPasswd(self,readExcel("login",4,3))
        l_submit(self)
        assert loginNull(self)
    '''
    def case005(self):
        l_inputUserName(self,readExcel("login",5,2))
        l_inputPasswd(self,int(readExcel("login",5,3)))
        l_submit(self)
        assert loginOften(self)

    def tearDown(self):#tearDown每次运行完用例方法之后，执行
        self.a.quit()
    '''

