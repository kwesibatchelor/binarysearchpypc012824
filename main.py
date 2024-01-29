pos = -1

def search (list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid+1
    return False 

list = [3, 6, 8, 13, 44, 98, 101, 700, 10986, 45555]

n = 8

if search (list, n):
    print("Found at", pos+1)
else:
    print("Not Found")