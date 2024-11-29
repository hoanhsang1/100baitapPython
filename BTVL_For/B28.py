# Nhập vào n
# Tính S = 1 + 2 + 3 + 4 + … + n

n = int(input('nhập n: '))
sum = 0
for i in range(n+1):
    sum+=i
print(sum)