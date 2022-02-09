from openpyxl import load_workbook

wb = load_workbook('sample2.xlsx')
ws = wb.active

ws.delete_rows(8, 3)
ws.delete_cols(2, 2)

wb.save('sample_del.xlsx')