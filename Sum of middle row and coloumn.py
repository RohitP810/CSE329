arr = [[1,2,3],[4,5,6],[7,8,9]]
sumr = 0
sumc = 0
for i in range(0,3):
    for j in range(0,3):
        if i==1 and j==1:
            sumc += arr[i][j]
            sumr += arr[i][j]
        elif j == 1:
            sumc += arr[i][j]
        elif i == 1:
            sumr += arr[i][j]
print("Sum of Rows = " + str(sumr))
print("Sum of Columns = " + str(sumc))
