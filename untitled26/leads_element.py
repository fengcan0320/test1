
def l_leadsClick(self):
    self.a.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a").click()
def l_leadsAdd(self):
    self.a.find_element_by_css_selector('a[href="/wk/index.php?m=leads&a=add"]').click()
def l_leadsConName(self,conName):
    self.a.find_element_by_id("contacts_name").send_keys(conName)
def l_submit(self):
    self.a.find_element_by_name("submit").click()
def l_leadsRightText(self):
    b=self.a.find_element_by_xpath("/html/body/div[5]/div[2]").text
    return b
def l_leadsNameClick(self):
    self.a.find_element_by_id("name").click()
def l_leadsNullText(self):
    b=self.a.find_element_by_id("contacts_nameTip").text
    return b