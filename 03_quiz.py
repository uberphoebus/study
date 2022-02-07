# 사회적 거리두기 영화관 좌석 예매 시스템

# 각 열은 1 ~ 20번까지 총 20개의 좌석으로 구성
# 이 때 A열에 대해서 홀수로 끝나는 좌석에 대해서만 출력(각 좌석은 ' '로 구분)

for i in range(1, 21):
    if i % 2 == 1:
        print(f'A{i}', end=' ')

print()

for i in range(1, 21, 2):
    print(f'B{i}', end=' ')