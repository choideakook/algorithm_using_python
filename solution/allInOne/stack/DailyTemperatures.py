# temperatures = 날짜별 온도 int[] ( 1 ~ 10^5 )

def solution(temps):
    answer = [0] * len(temps)
    stack = []

    for today, temp in enumerate(temps):
        while stack and stack[-1][1] < temp:
            past_date, _ = stack.pop()
            answer[past_date] = past_date - today

        stack.append((today, temp))
    return answer

print(solution(temps=[73,74,75,71,69,72,76,73]))
print(solution(temps=[3,2,5]))
print(solution(temps=[1,2,3]))
print(solution(temps=[3,2,1]))