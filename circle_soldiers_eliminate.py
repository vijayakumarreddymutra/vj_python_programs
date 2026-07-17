
def soldiers_survival(n):
    power = 1

    while 2 * power <=n :
        power *= 2

    return 2*(n-power) + 1

val = int(input("Enter any value: "))

print(soldiers_survival(val))