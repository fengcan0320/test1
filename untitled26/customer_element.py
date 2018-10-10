#coding=utf-8

def c_custmoerClick(self):
    self.a.find_element_by_link_text("客户").click()
def c_customerAdd(self):
    self.a.find_element_by_css_selector('a[href="/wk/index.php?m=customer&a=add"]').click() #新建客户
def c_customerName(self,customerName):
    self.a.find_element_by_id("name").send_keys(customerName)#客户名
def c_submit(self):
    self.a.find_element_by_name("submit").click()#保存
def c_customerRightText(self):
    b=self.a.find_element_by_xpath("/html/body/div[5]/div[2]").text
    return b
def c_ownershipClick(self):
    self.a.find_element_by_id("ownership").click()
def c_custmoerErrorText(self):
    b=self.a.find_element_by_id("nameTip").text
    return b