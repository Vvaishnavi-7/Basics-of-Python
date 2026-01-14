#Generators: Implement a generator function that yields prime numbers indefinitely.

def prime():
    n=2
    while True:
        is_prime=True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                is_prime=False
                break
        if is_prime:
            yield n
        n += 1

gen=prime()
for i in range(20):
    print(next(gen))
