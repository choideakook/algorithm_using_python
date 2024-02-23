# nums = ( 0 ~ 10^5 )
# nums[i] = ( -10^9 ~ 10^9 )

def solution(nums):
    answer = 0
    num_set = set(nums)

    for num in nums:
        count = 1
        if num - 1 not in num_set:
            next = num + 1
            while next in num_set:
                count += 1
                next += 1

        answer = max(answer, count)
    return answer

print(solution(nums=[]))
print(solution(nums=[3,4,1,2]))
print(solution(nums=[100,4,200,1,3,2]))
print(solution(nums=[0,3,7,2,5,8,4,6,0,1]))