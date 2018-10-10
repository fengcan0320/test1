import xlrd

def readExcel(sheet,row,col):
    a=xlrd.open_workbook("C:\dataCase.xlsx")
    b=a.sheet_by_name(sheet)
    c=b.cell_value(row,col)
    return c


