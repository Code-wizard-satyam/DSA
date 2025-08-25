def power2(n):
    if (n==1):
        return 2
    
    small_ans = power2(n-1)
    ans = 2 * small_ans
    # print(ans)
    return ans


print(power2(5))