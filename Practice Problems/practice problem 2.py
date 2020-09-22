# DIVIDE THE APPLES
# TANISH SARMAH

def apple():

    "Returns whether the no. of apples are divisible by the no.s in range or not."
    n=int(input("Enter the no of apples:\n"))
    mn=int(input("Enter the starting of the range:"))
    mx=int(input("Enter the ending point of the range:"))
    if mn==mx:
        print("Not a valid range!")
        raise Exception("'mx' and 'mn' should not be equal!")
    elif mn>mx:
        raise Exception("'mn' should not be greater than 'mx'")
    else:
        divisors=[i for i in range(mn,mx+1)]
        for item in divisors:
            if n%item==0:
                print(f"{n} is divisible by : {item}")
            else:
                print(f"{n} is not divisibe : {item}")

if __name__ == "__main__":
    apple()
