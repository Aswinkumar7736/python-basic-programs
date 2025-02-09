P=int(input("enter principal amount :"))
R=int(input("enter rate :"))
T=int(input("enter the time period :"))
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Simple Interest (P, R, T ):", simple_interest(P, R, T))