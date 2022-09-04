from openpyxl import load_workbook

# 수식이 아닌 실제 데이터(계산되지 않은 상태면 파일을 열고 저장)
wb = load_workbook('sample_formula.xlsx', data_only=True)
ws = wb.active

for row in ws.values:
    for cell in row:
        print(cell)

# wb.save('sample_formula.xlsx')