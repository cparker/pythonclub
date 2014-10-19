#asks questions
phoneNum = input('what are the first three digits of your phone number?')
phoneNum2 = input('what are the last three digits of your phone number?')
houseNum = input('what is your house number? (last three digits)')
age = input('how old are you? 0(s) in front')
zipCode = input('what are the first three digits of your zipcode')
info = [phoneNum, phoneNum2, houseNum, age, zipCode, 'pressing enter']
obvNums = ['123', '321', '456', '654', '789', '987', '111', '222', '333', '444', '555', '666', '777', '888', '999',
           '101', '678', 'pressing enter']
print('turn the lock to what I say and type \'y\' if the lock works or press enter if it does\'nt')
works = 'n'
currentNum = 999
while works != 'y':
    #   tries the numbers in personal info
    for numbers in info:
        print('try ' + numbers)
        works = input('does it work?')
        if numbers == 'pressing enter':
            break
        #   tries obvious, easy to remember combinations
    for numbers2 in obvNums:
        print('try ' + numbers2)
        works = input('does it work?')
        if numbers2 == 'pressing enter':
            break


        #   starts from 999 and counts down, skipping already guessed #'s
    while works != 'y':
        #      makes sure number hasnt already been tried
        if currentNum in obvNums or info:
            currentNum = currentNum - 1
        else:
            print("try " + str(currentNum) + 'if two digits, put 0 in front')
        works = input('does it work?')
        if str(currentNum) == '-1':
            break
    print('either we missed something or you CHEATED')
    break
