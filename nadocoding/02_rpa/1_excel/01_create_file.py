from openpyxl import Workbook

wb = Workbook() # 새 워크북 생성
ws = wb.active # 활성화된 sheet 가져옴
ws.title = 'NadoSheet' # sheet명 변경
wb.save('sample.xlsx')
wb.close()