# check_temperature.py
# 체온 리스트를 받아 평균을 계산하고 건강 판정을 내려주는 함수

def check_temperature(temps):
    avg = sum(temps) / len(temps)

    if avg >= 37.5:
        result = "주의 요망"
    else:
        result = "정상"

    return f"평균 체온: {avg}\n판정: {result}"

# 실행 예시
print(check_temperature([36.5, 37.8, 38.0]))
