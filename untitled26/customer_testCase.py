#coding=utf-8
from public import readExcel,windowsClick,windowsText
from customer_element import c_custmoerClick,c_customerAdd,c_customerName,c_submit,c_ownershipClick
from customer_judge import customerRight,customerRename,customerNull,customerWindowsText
from login_testCase import  login

class customer(login):
    @classmethod #setUpClass必须配合@classmethod 一起使用
    def setUpClass(self): #setUpClass此方法只运行一次，并且是优先执行的
        login.setUp()
        login.case001()

    def setUp(self): #setUp此方法在setUpClass这个方法执行后，每次都先运行
        try:
            c_custmoerClick(self)
        except:
            windowsClick(self)
            c_custmoerClick(self)

    def test001(self): #setUp之后运行
        c_customerAdd(self)
        c_customerName(self,readExcel("customer",1,2))
        c_submit(self)
        assert customerRight(self)

    def test002(self):
        c_customerAdd(self)
        customer=readExcel("customer",2,2)
        c_customerName(self,customer)
        c_submit(self)
        assert customerWindowsText(self,customer)
        windowsClick(self)
        c_ownershipClick(self)
        assert customerRename(self)

    def test003(self):
        c_customerAdd(self)
        customer=readExcel("customer",3,2)
        c_customerName(self,customer)
        c_submit(self)
        assert customerWindowsText(self,customer)
        windowsClick(self)
        windowsClick(self)
        assert customerNull(self)


