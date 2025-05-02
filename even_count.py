# [문제 6] 리스트에서 짝수가 몇 개인지 세어 출력하세요.
numbers = [3, 8, 2, 5, 7, 6]
# 출력: 짝수 개수: 3개

count = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        count += 1

print(f"짝수 개수: {count}개")
