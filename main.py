def check(str1):
    if len(str1) > 3:
        if str1[-3:] != "ing":
            str1 += "ing"
        else:
            str1 += "ly"
        return str1
    else:
        return str1


# List trong Python
def listTest():
    n = int(input())
    lst = []  # khoi tao list
    for i in range(n):
        lst.append(int(input()))  # them phan tu vao list
    min_value = lst[0]
    for i in lst:  # duyet list
        if i < min_value:
            min_value = i
    print(min_value)


def tri_recursion(k):
    if k == 1:
        return 1
    else:
        return k * tri_recursion(k - 1)


class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age

    def printName(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.graduationYear = year
        print("Hello, " + str(self.firstname) + " is being initialized")

    def printName(self):
        print("I'm a student. I will graduate in " + str(self.graduationYear))


def insertionSort(lst):
    for i in range(1,len(lst)):
        k = i
        while k > 0 and lst[k] < lst[k-1]:
            lst[k], lst[k-1] = lst[k-1], lst[k]
            k -= 1

def bubbleSort(lst):
    for i in range(len(lst),0,-1):
        for j in range(0,i-1):
            if lst[j]>lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def selectionSort(lst):
    for i in range(0,len(lst)):
        for j in range(i,len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]

def quickSort(a, low, high):
    if low < high:
        last = low + 1
        for i in range(last, high + 1):
            if a[i] < a[low]:
                a[i], a[last] = a[last], a[i]
                last += 1
        last -= 1
        a[low], a[last] = a[last], a[low]
        last -= 1
        quickSort(a, low, last)
        last += 2
        quickSort(a, last, high)


def merge(a,low,mid,high):
    lst = []
    index1 = low
    index2 = mid+1
    while index1 <= mid and index2 <= high:
        if a[index1] <= a[index2]:
            lst.append(a[index1])
            index1 += 1
        else:
            lst.append(a[index2])
            index2 += 1
    if index1 > mid:
        for i in range(index2,high+1):
            lst.append(a[i])
    elif index2 > high:
        for i in range(index1, mid+1):
            lst.append(a[i])
    k = 0
    for i in range(low,high+1):
        a[i] = lst[k]
        k += 1


def mergeSort(a, low, high):
    if low<high:
        mid = (low+high)//2
        mergeSort(a,low,mid)
        mergeSort(a,mid+1,high)
        merge(a, low, mid, high)

def maxHeapify(a,i,n):
    max = i
    if left[i] <= n and a[left[i]] > a[max]:
        max = left[i]
    if right[i] <= n and a[right[i]] > a[max]:
        max = right[i]
    if max != i:
        a[max], a[i] = a[i], a[max]
        maxHeapify(a,max,n)


def buildMaxHeap(a):
    for i in range(len(a)//2,-1,-1):
        maxHeapify(a,i,len(a)-1)


def heapSort(a):
    n = len(a)-1
    buildMaxHeap(a)
    a[0],a[n] = a[n], a[0]
    n -= 1
    while n>=1:
        maxHeapify(a,0,n)
        a[0], a[n] = a[n], a[0]
        n -= 1


lst = [3,4,5,6,9,8,1,7,2]
parent = []
left = []
right = []
for i in range(0,len(lst)):
    if i==0:
        parent.append(0)
    elif i != 0:
        parent.append(i//2) if i%2 == 1 else parent.append(i//2 - 1)
    left.append(2*i+1)
    right.append(2*i+2)

heapSort(lst)
print(lst)


