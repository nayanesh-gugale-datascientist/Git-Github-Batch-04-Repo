# Program to check whether a number is Perfect or not

num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")

else:
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        print(num, "is a Perfect Number.")
    else:
        print(num, "is not a Perfect Number.")