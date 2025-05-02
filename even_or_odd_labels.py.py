# [문제 3] 리스트에서 5의 배수만 출력하세요.
numbers = [5, 11, 20, 9, 15, 3]
# 출력: 5, 20, 15

for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        print(numbers[i])
