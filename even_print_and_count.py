# [문제 7] 리스트에서 짝수만 출력하고, 총 몇 개인지 개수도 출력하세요.
numbers = [3, 10, 7, 4, 6, 1]
# 출력: 10, 4, 6 / 짝수 개수: 3개

count = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])
        count += 1

print(f"짝수 개수: {count}개")
