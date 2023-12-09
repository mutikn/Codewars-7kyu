def divisors(integer):
    divisor = 2
    list_of_divisors = []
    for i in range(2, integer):
        if integer % divisor == 0:
            list_of_divisors.append(divisor)
        divisor += 1
    return list_of_divisors if len(list_of_divisors) > 0 else f'{integer} is prime'

