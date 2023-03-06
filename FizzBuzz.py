def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
       return "Buzz"
    return input
print (input("Biror sonni kiriting:"))
print (fizz_buzz(30))