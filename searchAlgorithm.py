def binarySearch(a, low, high, x):
    if low<=high:
        mid = (low + high) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return binarySearch(a, low, mid - 1,x)
        else:
            return binarySearch(a, mid + 1, high,x)
    else:
        return -1


lst = [1,2,3,4,6,7,8,9]
print(binarySearch(lst,0,7,9))
