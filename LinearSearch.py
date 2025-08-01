
pos = 0

def search(list1, n):

    for i in list1:

        if list1[pos] == n:
            return True

        globals()['pos'] += 1
    return False

list1 = [2,34,5,56,54,345,34,12,5,7,8,12,3]
n = 34

if search (list1, n):
    print('Found at: ', pos)
else:
    print('Not found')