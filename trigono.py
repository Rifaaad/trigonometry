#program trigonometry

print("\nMENGHITUNG NILAI TRIGONOMETRI\n")


import cmath
import math
from math import sin, cos, tan, pi

#mencari nilai sin
def sin(a):
    return math.sin((math.pi/180)*a)

#mencari nilai cos
def cos(a):
    return math.cos((math.pi/180)*a)

#mencari nilai tan
def tan(a):
    return math.tan((math.pi/180)*a)

print("pilih metode operasi perhitungan trigonometri")
print("1. sin")
print("2. cos")
print("3. tan")

while True:

    choice = input("silahkan pilih metode yang diinginkan : ")

    if choice in ('1', '2', '3', '4'):
        try:
            a = int(input("masukkan nilai: "))
        except ValueError:
            print("input salah! masukkan nilai.")
            continue
    
        if choice == '1':
            print("nilai dari sin", a, "=", end=" ")
            print(math.sin((math.pi/180)*a))
        
        elif choice == '2':
            print("nilai dari cos", a, "=", end=" ")
            print(math.cos((math.pi/180)*a))
    
        elif choice == '3':
            print("nilai dari tan", a, "=", end=" ")
            print(math.tan((math.pi/180)*a))
        
    
        coba_lagi = input("ingin coba lagi? (y/n): ")
        if coba_lagi == "n":
            break
    else:
        print("gagal")
