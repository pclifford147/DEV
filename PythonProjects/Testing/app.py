def checkio(number: int) -> str:
    # Your code here
    # It's main function. Don't remove this function
    # It's using for auto-testing and must return a result for check.

    result = ""
    if 0 < number and number <= 1000:
        if number % 3 == 0 and number % 5 == 0:
            result = "Fizz Buzz"
        elif number % 5 == 0:
            result = "Buzz"
        elif number % 3 == 0:
            result = "Fizz"
        else:
            result = str(number)
    
    return result

print(checkio(7))

print("end")