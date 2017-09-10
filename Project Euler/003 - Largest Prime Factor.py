# Author tbejos

num = 600851475143

def isPrime(n):
        if n == 1 or (n != 2 and n % 2 == 0):
                return False
        for i in range(3, int(n**0.5), 2):
            if n % i == 0:
                    return False
        return True

def main():
    largest = 0
    for i in range(1, int(num**0.5)):
        if num % i == 0 and isPrime(i):
            largest = i
    print(largest)

main()
