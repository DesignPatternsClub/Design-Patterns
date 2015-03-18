import os
from openpyxl import Workbook
os.chdir(r"./mock_excel_files")

for i in xrange(1, 5):

    wb = Workbook()
    ws = wb.active

    msg = "I am mock html number " + str(i) + ", scrape me!"
    ws.cell(row=i, column=i).value = msg

    wb.save("test_mock_excel_" + str(i) + ".xlsx")
