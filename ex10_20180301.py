answer = 'yes'
count = 0
while answer == 'yes':
    print('You have',count,'coins.')
    answer = input("Would you like another coin? ")
    count += 1
    if answer.lower() != 'yes':
        break
print("bye")