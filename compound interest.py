P=int(input("enter principal amount :"))
R=int(input("enter rate :"))
T=int(input("enter the time period :"))
def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

print("Compound Interest (P, R, T years):", compound_interest(P,R,T))