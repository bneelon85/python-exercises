day = int(input('Day (0-6)? '))

if day ==0 or day ==6:
    print("Sleep In")
elif day >0 and day <6: 
    print("Go to work")
else: print("Number too big")
