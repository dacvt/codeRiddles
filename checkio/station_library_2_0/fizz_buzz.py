def checkio(number):
    if number%3==0:
        if number%5==0:
            return "Fizz Buzz"
        return "Fizz"
    elif number%5==0:
        return "Buzz"
    else:
        return str(number)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    try:
        assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
        assert checkio(6) == "Fizz", "6 is divisible by 3"
        assert checkio(5) == "Buzz", "7 is divisible by 5"
        assert checkio(7) == "7", "15 is not divisible by 3 or 5"
    except:
        print "Correct your function"
