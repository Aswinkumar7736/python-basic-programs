n=int(input("ENTER THE NUMBER:"))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of n:", factorial(n))