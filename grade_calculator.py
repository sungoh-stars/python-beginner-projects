def get_two_integers():
    while True:
        try:
            user_input = input("숫자 2개를 입력하세요 (예: 70,80): ")
            parts = user_input.strip().split(",")

            if len(parts) != 2:
                print("숫자 두 개를 입력하시오")
                continue

            scores = [int(x.strip()) for x in parts]
            return scores

        except ValueError:
            print("잘못된 형식 입력했습니다")

def print_larger(nums: list[int]) -> int:
    return max(nums)

def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def get_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def main():
    numbers = get_two_integers()
    largest = print_larger(numbers)
    avg = calculate_average(numbers)
    grade = get_grade(avg)
    print(f"당신이 입력한 숫자는: {numbers}")
    print(f"최고 점수는: {largest}입니다")
    print(f"평균은: {avg}")
    print(f"등급: {grade}")

main()
