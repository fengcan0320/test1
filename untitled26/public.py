#coding=utf-8
import xlrd#引用外部excle数据

def readExcel(sheet,row,col):
    x=xlrd.open_workbook("C:\dataExcel.xlsx")#读取C盘路径里面的dataExcel.xlsx
    s=x.sheet_by_name(sheet)#读哪个SHEET
    v=s.cell_value(row,col) #读第几行，第几列
    return v   #返回读取到的数据给方法

def windowsClick(self):
    self.a.switch_to_alert().accept()

def windowsText(self):
    b=self.a.switch_to_alert().text
    return b