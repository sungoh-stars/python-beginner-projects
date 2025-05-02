# [문제 1] 리스트에 있는 숫자 중 홀수만 출력하세요.
numbers = [4, 7, 1, 9, 6, 2]
# 출력: 7, 1, 9

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        print(numbers[i]