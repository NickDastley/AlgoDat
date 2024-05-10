def fizz_buzz(n):
    number = 1
    for _ in range(n):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
        number += 1
    return


fizz_buzz(100)