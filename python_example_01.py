#!/usr/bin/env python3

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
   fh = float(sh)
   fr = float(sr)

except:
      print("Error, please enter numberic input")
      quit() #16'th December added quit() function.

print(fh, fr)
if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    # print('Regular')
    xp = fh * fr
    print('Pay:', xp)
