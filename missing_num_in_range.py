'''
a = [5,2,3,0,1]

def missing_num():
    n,s,k = len(a), 0,0

    for i in a:
        s = s + i
    for j in range(n+1):
        k = k + j


    print(k,s)
    return k - s

print(missing_num())

'''
'''
a = [5, 2, 3, 0, 1]

def missing_num():
    n = len(a)
    actual_sum = 0

    for i in a:
        actual_sum += i

    expected_sum = n * (n + 1) // 2

    return expected_sum - actual_sum

print(missing_num())
'''


a = [16, 17, 18, 20, 21]

def missing_num():
    first = 16
    last = 21

    total_numbers = last - first + 1

    expected_sum = (first + last) * total_numbers // 2

    actual_sum = 0

    for i in a:
        actual_sum += i

    return expected_sum - actual_sum


print(missing_num())