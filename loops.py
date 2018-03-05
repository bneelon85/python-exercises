#ex 1
for i in range(1,11):
    print(i)

#ex 2
n = int(input("At what number would you like to begin?"))
m = int(input("At what number would you like to end?"))

for i in range(n,m+1):
    print(i)

#ex 3
for i in range(1,11,2):
    print(i)

#ex 4
for i in range(1,6):
    print("*****")

#ex 5
howBig = int(input("How big is the square? "))
char = "*"

for i in range(1,howBig+1):
    print(howBig*char)
    
#ex 6
width = int(input("How wide? "))
height = int(input("How tall? "))
star = "*"
space = " "

for i in range(1,height+1):
    if i==1 or i==height:
        print(width*star)
    else:
        print(star,space*(width-2),star,sep="")

#ex 7
for i in range(1,8,2):
    print(space*int(((7-i)/2)),star*i,space*int(((7-i)/2)))

#ex 8
triHeight = int(input("Height? "))
tH2 = (2*triHeight-1)
for i in range(1,triHeight*2,2):
    print(space*int(((tH2-i)/2)),star*i,space*int(((tH2-i)/2)))

#ex 9
for j in range(1,11):
    for i in range(1,11):
        print(j,"X", i,"=",i*j)

#Bonus 1
text = input("What do you want a banner around? ")

print("*"*(len(text)+4))
print("* ",text," *",sep="")
print("*"*(len(text)+4))

#Bonus 2