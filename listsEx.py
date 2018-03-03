# Ex 1
numbers = [10,20,30, 9,-12]
print("The sum of 'numbers' is:",sum(numbers))

# Ex 2
print("The largest of 'numbers' is:",max(numbers))
# Ex 3
print("The smallest of 'numbers' is:",min(numbers))
# Ex 4
for i in numbers:
    if (i % 2 == 0):
        print(i,"is even.")
# Ex 5
for i in numbers:
    if (i > 0):
        print(i,"is positive.")
# Ex 6        
posNums = []       
for i in numbers:
    if (i > 0):
        posNums.append(i)
        
print(posNums)
# Ex 7
times5 = []
for x in numbers:
    times5.append(x*5)

print(times5)
# Ex 8
a=[1,3,6]
b=[2,4,6]
ab = []
for i in range(0, len(a)):
     ab.append(a[i]*b[i])

print(ab)

# Ex 9 and 10
m=[[1,2],[7,8],[3,4]]
n=[[3,4],[5,6],[3,4]]
m_n = []
for h in range(len(m)):
    row = []
    for j in range(len(m[h])):
        row.append(m[h][j] + n[h][j])
    m_n.append(row)

print(m_n)

# Ex 11
dupList = ["x","y","z","y",23,0.5,23]
noDup = []
for z in dupList:
    if(z not in noDup):
        noDup.append(z)
        
print(noDup)