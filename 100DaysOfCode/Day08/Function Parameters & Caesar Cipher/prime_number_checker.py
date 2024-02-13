
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % 2 == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

n= int (input("Type a number: ")) # check this number
prime_checker(number=n)