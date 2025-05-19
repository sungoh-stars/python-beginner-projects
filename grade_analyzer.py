def get_scores() -> list[int]:
    """
    사용자에게 쉼표로 구분된 점수를 입력받아 정수 리스트로 반환합니다.
    Gets a list of scores from user input and returns it as a list of integers.
    """
    while True:
        try:
            user_input = input("점수들을 쉼표로 입력하세요 (예: 70,80,90): ")
            scores = [int(x.strip()) for x in user_input.split(",")]
            return scores
        except ValueError:
            print("잘못된 형식을 입력하였습니다. 숫자만 쉼표로 구분해서 입력해주세요.")

def calculate_average(scores: list[int]) -> float:
    """
    점수 리스트의 평균을 계산해 반환합니다.
    Calculates and returns the average of the score list.
    """
    return sum(scores) / len(scores)

def get_max_min(scores: list[int]) -> tuple[int, int]:
    """
    최고 점수와 최저 점수를 튜플로 반환합니다.
    Returns the highest and lowest scores as a tuple.
    """
    return max(scores), min(scores)

def get_grade(average: float) -> str:
    """
    평균 점수를 바탕으로 등급(A~F)을 반환합니다.
    Returns a grade letter (A~F) based on the average score.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def display_result(scores: list[int], average: float, max_score: int, min_score: int, grade: str) -> None:
    """
    입력 점수, 평균, 최고점, 최저점, 등급을 화면에 출력합니다.
    Displays the score list, average, highest and lowest score, and final grade.
    """
    print("\n--- 결과 요약 ---")
    print(f"입력한 점수: {', '.join(str(s) for s in scores)}")
    print(f"평균 점수: {average:.2f}")
    print(f"최고 점수: {max_score}")
    print(f"최저 점수: {min_score}")
    print(f"등급: {grade}")

def main() -> None:
    """
    프로그램의 메인 흐름을 실행합니다.
    Runs the main logic of the grade analyzer.
    """
    scores = get_scores()
    average = calculate_average(scores)
    max_score, min_score = get_max_min(scores)
    grade = get_grade(average)
    display_result(scores, average, max_score, min_score, grade)

if __name__ == "__main__":
    main()
