number = input("점수를 입력하세요")
numbers = number.split(",")
total = list(map(int, numbers))
pusl = sum(total)

reg = pusl / len(total)

if reg >= 90:
    scores = "A"
elif reg >= 80:
    scores = "B"
elif reg >= 70:
    scores = "C"
elif reg >= 60:
    scores = "D"
else:
    scores = "F"

print(f"총합: {pusl} \n평균: {reg} \n등급: {scores} 학점입니다.")
