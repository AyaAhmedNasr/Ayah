def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    operations = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            operations.append(('No operation', str2[j-1]))
            i -= 1
            j -= 1
        elif dp[i][j] == 1 + dp[i-1][j]:
            operations.append(('Delete', str1[i-1]))
            i -= 1
        elif dp[i][j] == 1 + dp[i][j-1]:
            operations.append(('Insert', str2[j-1]))
            j -= 1
        else:
            operations.append(('Substitute', (str2[j-1], str1[i-1])))
            i -= 1
            j -= 1
    
    while i > 0:
        operations.append(('Delete', str1[i-1]))
        i -= 1
    
    while j > 0:
        operations.append(('Insert', str2[j-1]))
        j -= 1
    
    operations.reverse()
    
    return dp[m][n], operations

# Example usage
str1 = 'abcdef'
str2 = 'azced'
min_ops, ops_list = edit_distance(str1, str2)
print(f'Minimum number of operations: {min_ops}')
for op in ops_list:
    print(op[0], op[1])


Output:


Minimum number of operations: 3
No operation a
Substitute b z
Substitute f d