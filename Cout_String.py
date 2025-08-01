

arr = []
Number_Of_Inputs = 10
count = 0

for i in range(Number_Of_Inputs):
    User_input = input('Enter 10 String to be inserted')
    arr.append(User_input)

    if len(arr[i]) > 5:
        count += 1


# Print full array
print("\nAll strings entered:")
print(arr)


# Print count of long strings
print(f"\nTotal strings with more than 5 characters: {count}")

for string in arr:
    if len(string) > 5:
        print(string)