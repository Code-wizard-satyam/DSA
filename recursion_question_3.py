def count_digit(n):
  if (n//10) == 0:
    return 1
  
  small_ans = count_digit(n//10)
  ans = small_ans +1
  return ans


print(count_digit(1234))