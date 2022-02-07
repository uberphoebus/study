# https://youtu.be/487mr-e_Z74

# 리스트에서 랜덤으로 1개 단어 선택
# 단어의 길이에 맞게 밑줄 출력
lst = ['apple', 'banana', 'orange']

# 사용자로부터 한글자씩 입력을 받되, 단어에 입력값이 포함되면
# Correct 출력, 아니면 Wrong 출력

# 입력 받을 때 마다 현재까지 맞힌 글자들 표시
# 맞히지 못한 글자는 밑줄 출력

# 정답을 맞히면 Success 출력 후 프로그램 종료(횟수 제한 없음)

import random

word = [alp for alp in lst[random.randint(0, 2)]]
word = lst[random.randint(0, 2)]
ans = [a for a in word]
blank = ['_' for i in range(len(word))]
running = True

while running:
    print(' '.join(blank))
    a = input('Input letter > ')
    
    if a in word:
        print('Correct')
        print(' ')
        
        idx = []
        for i, j in enumerate(ans):
            if j == a:
                idx.append(i)
        
        for i in idx:
            blank[i] = a
    
    else:
        print('Wrong')
        print(' ')
    
    if ''.join(blank) == word:
        print('Succeed')
        running = False