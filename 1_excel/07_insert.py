from openpyxl import load_workbook

wb = load_workbook('sample2.xlsx')
ws = wb.active

ws.insert_rows(8, 5) # 8번째 줄에 5줄 추가 
ws.insert_cols(2, 3)

wb.save('sample_insert.xlsx')