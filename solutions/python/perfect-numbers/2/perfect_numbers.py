def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisor_sum = 0

    for i in range(1,int(number ** 0.5) + 1):
        if number % i == 0:
            other = number // i
            if i != number:
                divisor_sum += i
            if other != i and other != number:
                divisor_sum += other

    if divisor_sum > number:
        return "abundant"
    elif divisor_sum < number:
        return "deficient"
    else:
        return "perfect"
