# summarize_scores.py
# 시험 점수 리스트를 받아 총합, 평균, 등급을 계산하는 함수

def summarize_scores(scores):
    total = sum(scores)
    avg = total / len(scores)

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    return f"총합: {total}\n평균: {avg}\n등급: {grade}"

# 실행 예시
print(summarize_scores([100, 85, 90, 100]))
