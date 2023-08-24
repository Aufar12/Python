import xlwings as xw

newExcel = xw.Book('sample_file.xlsx')
sheet = newExcel.sheets['Sample 3']
sheet['E60'].value = 300

# set background color
# ws["B1"].value = "Field1"
# ws["B1"].color = (255,255,204)

# # set font to bold
# ws["B2"].value = "Field2"
# ws.range("B2").api.Font.Bold = True

# # set font color to green
# # color-index see here
# ws["B3"].value = "Field3"
# ws.range("B3").api.Font.ColorIndex = 4

newExcel.save()
app = xw.apps.active
app.kill()