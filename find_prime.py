def find_prime(X):
    factors = list()
    divisor = 2
    while (divisor <= X):
        if (X%divisor)==0:
                factors.append(divisor)
                X = X/divisor
        else:
            divisor += 1
    return factors
