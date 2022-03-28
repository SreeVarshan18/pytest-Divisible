def divisible_5(x):
    if x % 5 == 0:
        return True
    else:
        return False

def divisible_7(x):
    if x % 7 == 0:
        return True
    else:
        return False

def divisible_9(x):
    if x % 9 == 0:
        return True
    else:
        return False

def divisible_10(x):
    if x % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    a = int(input("Enter a Number: "))
    res = divisible_5(a)
    if res == True:
        print(a, " is Divisible by 5")
    else:
        print(a, " is NOT Divisible by 5")

    res2 = divisible_7(a)
    if res2 == True:
        print(a, " is Divisible by 7")
    else:
        print(a, " is NOT Divisible by 7")
    res3 = divisible_9(a)
    if res3 == True:
        print(a, " is Divisible by 9")
    else:
        print(a, " is NOT Divisible by 9")
    res4 = divisible_10(a)
    if res4 == True:
        print(a, " is Divisible by 10")
    else:
        print(a, " is NOT Divisible by 10")

