def is_prime(n: int) -> bool:
    """Return True if n is a prime (n >= 2)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def print_primes_upto(limit: int) -> None:
    """Print all prime numbers <= limit, one per line."""
    if limit < 2:
        print("No primes")
        return
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    # Example usage: prints primes up to 50
    print_primes_upto(50)