import math
from operator import itemgetter, attrgetter
import re
from timeit import Timer
import random
# chia het cho 7 nhung k chia het cho 5, 2000<=x<=3000

# lst = []
# x = 2002
# i = 1
# while x<=2072:
#     if i==5:
#         i = 1
#         x = x+7
#     else:
#         lst.append(x)
#         x = x + 7
#         i = i + 1
#
# print(lst)

# tinh giai thua

# def giaiThua(n):
#     if n==1:
#         return 1
#     else:
#         return n*giaiThua(n-1)
#
#
# print("Nhap vao so can tinh: ")
# n = int(input())
# print(giaiThua(n))


# def giaiThua(n):
#     """ Tra ve giai thua cua mot so
#     """
#     if n==1:
#         return 1
#     else:
#         return n*giaiThua(n-1)
#
#
# class Test:
#     def __init__(self):
#         self.string = ""
#
#     def getString(self):
#         self.string = input("Nhap chuoi: ")
#
#     def printString(self):
#         print(self.string.upper())
#
#
# print(giaiThua.__doc__)

# khai bao bien static trong class

# class Person:
#     # name la bien static
#     name = "Personloz"
#
#     # Code by Quantrimang.com
#     def __init__(self, name=None):
#         # self.name là biến instance
#         self.name = name

# class VietNam:
#     @staticmethod
#     def printNationality():
#         print("This is Viet Nam")
#
#     surface = "300 km2"
#     length = "1600 km"
#
#     def __init__(self):
#         self.speciality = ["thuoc lao", "xoc dia"]
#
# class HaNoi(VietNam):
#     @staticmethod
#     def printName():
#         print("Day la Ha Noi")
#
#     surface = "16 km2"
#     length = "50 km"
#
#     def __init__(self):
#         self.name = "Ha Noi"
#         self.isCapital = True
#         self.speciality = ["ca phe sua", "tra da", "bun cha"]
#
#
# vn = VietNam()
# hn = HaNoi()
# print(vn.speciality)
# print(hn.speciality)
# print(VietNam.surface)
# print(HaNoi.surface)


lst = [1,2,3,4,5]
for i in lst:
    print(i)