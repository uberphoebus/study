absent = [2, 5]
no_book = [7]
for stu in range(1, 11):
    if stu in absent:
        continue
    elif stu in no_book:
        print(f'end {stu} come')
        break
    print(f'{stu} read')