# grade_checker.py

score = int(input("당신의 점수를 입력하세요 (0~100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"당신의 등급은: {grade}")
else:
    print("잘못된 점수입니다. (0~100 사이의 값을 입력하세요)")
