def std_weight(h, g):
    if g == '남자':
        return h * h * 22
    else:
        return h * h * 21

h = 175
g = '남성'

w = std_weight(h / 100, g)
w = round(w, 2)

print(w)