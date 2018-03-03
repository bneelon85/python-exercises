billTotal = float(input("How much was your bill? "))
level = input("How would you rate your service?(Good, Fair, Bad): ")
splitWays = int(input("Split the bill how many ways? "))

if level == "Good":
    print("Tip Amount: $",.2*billTotal)
    print("Total Amount: $", .2*billTotal+billTotal)
    print("Amount per person: $", (.2*billTotal+billTotal)/splitWays)
elif level == "Fair":
    print("Tip Amount: $",.15*billTotal)
    print("Total Amount: $", .15*billTotal+billTotal)
    print("Amount per person: $", (.15*billTotal+billTotal)/splitWays)
elif level == "Bad":
    print("Tip Amount: $",.1*billTotal)
    print("Total Amount: $", .1*billTotal+billTotal)
    print("Amount per person: $", (.1*billTotal+billTotal)/splitWays)
else: print("Try Again")