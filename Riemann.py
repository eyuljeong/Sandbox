# 소수 리스트의 마지막 소수에 2 더하고(5부터 시작하니까) 리스트의 소수들로 나누어서
# 나누어지면 다시 2 더하고, 안 나누어지면 리스트에 추가, 반복

decimal = [2, 3]
divnum = 5
flag = 0
i = 5
while i <= 1000000:
    for num in decimal:
        if divnum % num == 0:
            flag = 1
            break
    
    if flag == 0:
        decimal.append(divnum)
    
    divnum += 2
    flag = 0
    i += 2

print(decimal)