n = int(input())
pascal_matrix = [[1]]

for i in range(1, n + 1):
    binomial_koeff = []
    for j in range(0, i + 1):
        if j == 0:
            binomial_koeff.append(pascal_matrix[i - 1][0])
        elif j == i:
            binomial_koeff.append(pascal_matrix[i - 1][j - 1])
        else:
            binomial_koeff.append(pascal_matrix[i - 1][j] + pascal_matrix[i - 1][j - 1])
    pascal_matrix.append(binomial_koeff)

for i in range(0, len(pascal_matrix[n])):
    print(pascal_matrix[n][i], end=' ')
