
a = 5
b = 0



try:
    print("open file")
    print(a/b)
    # print("Closing file")
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print("Division by zero" , e)
    #print("Closing file")

except ValueError as e:
    print("ValueError", e)

except Exception as e:
    print("Exception", e)

finally:
    print("Closing file")

