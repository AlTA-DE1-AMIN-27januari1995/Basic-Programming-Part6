def compare(a, b):
    m = len(a)
    n = len(b)
    result = 0
    end = 0
    length = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (i == 0 or j == 0):
                length[i][j] = 0
            elif (a[i - 1] == b[j - 1]):
                length[i][j] = length[i - 1][j - 1] + 1
                if length[i][j] > result:
                    result = length[i][j]
                    end = i - 1
            else:
                length[i][j] = 0
    return a[end - result + 1 : end + 1]

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA