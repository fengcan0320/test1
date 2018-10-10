from login_testCase import login
from leads_element import l_leadsAdd,l_leadsClick,l_leadsConName,l_submit,l_leadsNameClick
from public import readExcel,windowsClick
from leads_judge import leadsRight,leadsNull,leadsWindowsText

class leads(login):
    @classmethod
    def setUpClass(self):
        login.setUp()
        login.case001()

    def setUp(self):
        try:
            l_leadsClick(self)
        except:
            windowsClick(self)
            l_leadsClick(self)

    def test001(self):
        l_leadsAdd(self)
        l_leadsConName(self,readExcel("leads",1,2))
        l_submit(self)
        assert leadsRight(self)
    def test002(self):
        l_leadsAdd(self)
        l_leadsConName(self,readExcel("leads",2,2))
        l_submit(self)
        l_submit(self)
        assert leadsWindowsText(self)
        windowsClick(self)
        l_leadsNameClick(self)
        assert leadsNull(self)

