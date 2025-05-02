# [문제 5] 리스트에서 5 이상이면서 10 이하인 숫자만 출력하세요.
numbers = [3, 5, 7, 10, 11, 2]
# 출력: 5, 7, 10

for i in range(len(numbers)):
    if 5 <= numbers[i] <= 10:
        print(numbers[i])
