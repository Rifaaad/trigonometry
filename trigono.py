#program trigonometry

print("\nMENGHITUNG NILAI TRIGONOMETRI\n")


import cmath
# import math
from math import sin, cos, tan, pi

#mencari nilai sin
def sinD(a):
    return round(sin((pi/180)*a),2)

#mencari nilai cos
def cosD(a):
    return round(cos((pi/180)*a),2)

#mencari nilai tan
def tanD(a):
    if a == 90 or a == 270:
        return "inf"
    return round(tan((pi/180)*a),2)

# ada 3 menu:
# 1. pembelajaran
#  ____________|
# |____________|
# |____________|
# |_____________|
# 2. Kalkulator
# 3. Game

def pembelajaran():
    print(f"""
     __________________________________________________________________________________________________________________________________ 
    |     | 0   | 30   | 45   | 60    | 90  | 120  | 135   | 150   | 180  | 210   | 225   | 240   | 270  | 300   | 315  | 330   | 360  |
    | Sin | {sinD(0)} | {sinD(30)}  | {sinD(45)} | {sinD(60)}  | {sinD(90)} | {sinD(120)} | {sinD(135)}  | {sinD(150)}   | {sinD(180)}  | {sinD(210)}  | {sinD(225)} | {sinD(240)} | {sinD(270)} | {sinD(300)} | {sinD(315)}| {sinD(330)}  | {sinD(360)} |
    | cos | {cosD(0)} | {cosD(30)} | {cosD(45)} | {cosD(60)}   | {cosD(90)} | {cosD(120)} | {cosD(135)} | {cosD(150)} | {cosD(180)} | {cosD(210)} | {cosD(225)} | {cosD(240)}  | {cosD(270)} | {cosD(300)}   | {cosD(315)} | {cosD(330)}  | {cosD(360)}  |
    | tan | {tanD(0)} | {tanD(30)} | {tanD(45)}  | {tanD(60)}  | {tanD(90)} | {tanD(120)}| {tanD(135)}  | {tanD(150)} | {tanD(180)} | {tanD(210)}  | {tanD(225)}   | {tanD(240)}  | {tanD(270)}  | {tanD(300)} | {tanD(315)} | {tanD(330)} | {tanD(360)} |
    """) 

def kalkulator():
    print("Pilih metode operasi perhitungan trigonometri:")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    choice = input("silahkan pilih metode yang diinginkan : ")

    if choice in ('1', '2', '3', '4'):
        try:
            a = float(input("masukkan nilai: "))
        except ValueError:
            print("input salah! masukkan nilai.")
    
        if choice == '1':
            print("nilai dari sin", a, "=", end=" ")
            print(sinD((pi/180)*a))
        
        elif choice == '2':
            print("nilai dari cos", a, "=", end=" ")
            print(cosD((pi/180)*a))
    
        elif choice == '3':
            print("nilai dari tan", a, "=", end=" ")
            print(tanD((pi/180)*a))

def game():
    pass

def main():
    print("Selamat datang di dunia matematika")
    print("Silakan pilih menu:")
    print("1. Pembelajaran")
    print("2. Kalkulator")
    print("3. Game")
    choice = int(input("silahkan pilih metode yang diinginkan : "))
    if 0 < choice <= 3:
        if choice == 1:
            pembelajaran()
        elif choice == 2:
            kalkulator()
        else:
            game()
    else:
        print("Gak ada woy")

if __name__ == "__main__":
    while True:
        main()

        


# while True:


        
    
#         coba_lagi = input("ingin coba lagi? (y/n): ")
#         if coba_lagi == "n":
#             break
#     else:
#         print("gagal")
