

pos = -1

def BinarySearch(list1, n):

    l = 0
    u = len(list1)-1

    while l <= u:

        mid = (l+u)//2

        #Found Mid or Not
        if list1[mid] == n:
            globals()['pos'] = mid
            return True

        else:
            #change L and U until you find mid
            if list1[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False




list = [4,7,8,12,45,99]
n = 9

if BinarySearch(list, n):
    print('Found at:',pos)
else:
    print('Not Found')
