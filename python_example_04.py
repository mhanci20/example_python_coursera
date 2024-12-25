#!/usr/bin/env python3

# def stuff():
#    print('Hello')
#    return
#    print('World')

# stuff()

def computepay(h, r):
    if h <= 40:
      pay = h * r
    else:
        pay = (40 * r) + ((h - 40) * r * 1.5)
    return pay

# Kullanıcıdan giriş almak
hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate per Hour: "))

# Ödemeyi hesaplama
p = computepay(hrs, rate)
print("Pay", p)
