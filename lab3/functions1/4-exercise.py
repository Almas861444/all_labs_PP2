def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers_str = input("enter list numbers: ")
numbers_list = list(map(int, numbers_str.split()))

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)