nums = [17,13,18,23,23]

#check if number is divisible by 5 (if true print number and exit)
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found")

