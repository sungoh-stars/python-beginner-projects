# [문제 2] 리스트에서 10보다 큰 숫자만 출력하세요.
numbers = [3, 12, 5, 18, 7, 2]
# 출력: 12, 18

for i in range(len(numbers)):
    if numbers[i] > 10:
        print(numbers[i]