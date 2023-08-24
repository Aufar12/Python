import xlwings as xw
from xlwings import constants

# Refresh Pivot : https://stackoverflow.com/questions/48173137/update-2-pivot-tables-on-single-worksheet
# Membuat Pivot : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html

wbook = xw.Book('excel-pivot-tables-example-file.xlsx')
wbook.sheets['Sheet2'].select()
wbook.api.ActiveSheet.PivotTables('AZZ').RefreshTable()
# wbook.api.ActiveSheet.PivotTables('AZZ').ChangePivotCache()
# wbook.api.ActiveSheet.PivotTables('AZZ').PivotCache.refresh


# bsheet1 = wbook.sheets['Sheet2']
# PT = bsheet1.api.PivotTables("AZZ")
# PT.SourceData = 'Data!$B3:$H469'
