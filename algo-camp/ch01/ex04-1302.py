d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

print(d)

# from collections import Counter

# N = int(input())
# books = [input() for _ in range(N)]
# c = Counter(books)
# # print(sorted(c, key=lambda x: (x, c[x]))[0])
# # print(c)
# # books = []
# # for _ in range(int(input())):
# #     books.append(input())

# # books = ['icecream', 'icecream', 'chocolate', 'chocolate']

# c = Counter(books)
# print(c.most_common())
# print(sorted(c.most_common(), key=lambda x: (x[1], x[0])))