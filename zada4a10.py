number_is_not_prime = False
n = int(input())
for i in range(2, n):
    if n % i == 0:
        number_is_not_prime = True
if number_is_not_prime:
    print(f"{n}is not prime")
else:
    print(f"{n}is prime")
