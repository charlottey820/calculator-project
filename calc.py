initial = float(input("What is your initial investment?"))
rate = float(input("What is your interest rate?"))
time = float(input("How many years will you have this account?"))
def interest(money,rate,years):
    ans = money*((100+rate)/100)**years
    print(ans)
    print(round(ans,3))
    # if str(round(ans,0))[-1] != "0":
    #     return f"After {years} years, your account balance will be ${round(money*((100+rate)/100)**years, 2)}"
    if round(ans,0) == ans or str(round(ans,3))[-2] == "0": 
        return f"After {years} years, your account balance will be ${round(ans,2)}0" 
    else:
        return f"After {years} years, your account balance will be ${round(money*((100+rate)/100)**years, 2)}"
print(interest(initial,rate,time))