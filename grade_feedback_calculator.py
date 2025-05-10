
---

## 🧠 완성된 코드 (`grade_feedback_calculator.py`)

```python
def get_score_input() -> str:
    """input에 점수를 입력 받습니다"""
    return input("점수를 입력하세요: ")

def convert_average(scors_str: str) -> list[int]:
    """문자열 스코어 리스트를 정수 리스트로 바꿉니다"""
    return list(map(int, scors_str.split(",")))

def calculate_average(scors_list: list[int]) -> float:
    """리스트 정수를 소수로 바꾸어 평균을 계산합니다"""
    return sum(scors_list) / len(scors_list)

def get_grade(avg: float) -> str:
    """평균을 바탕으로 등급을 출력합니다"""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"

def get_feedback(grade: str) -> str:
    """문자열 등급을 받아 피드백을 문자열로 출력합니다"""
    if grade == "A":
        return "완벽합니다"
    elif grade == "B":
        return "니이스!"
    elif grade == "C":
        return "음... 하..."
    else:
        return "넌 진짜 뭐냐?"

def main() -> str:
    scores = get_score_input()
    scors_list = convert_average(scores)
    avg = calculate_average(scors_list)
    reg = get_grade(avg)
    feedback = get_feedback(reg)
    return f"""당신의 평균은: {avg}
당신의 등급은: {reg}
피드백: {feedback}"""

print(main())
