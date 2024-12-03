#!/usr/bin/env python3

from datetime import datetime

def countdown_calculator():
    print("Lütfen tarihleri 'YYYY-MM-DD HH:MM:SS' formatında giriniz")
    start_date_input = input("Başlangıç tarihi: ")
    end_date_input = input("Bitiş tarihi: ")

    try:
       # Tarihleri datetime nesnelerine çevirme
       start_date = datetime.strptime(start_date_input, "%Y-%m-%d %H:%M:%S")
       end_date = datetime.strptime(end_date_input, "%Y-%m-%d %H:%M:%S")

       # Tarihleri arasındaki farkı hesaplama
       difference = end_date - start_date

       if difference.total_seconds() < 0:
           print("\nBitiş tarihi başlangıç tarihinden önce olamaz.")
       else:
           days = difference.days
           seconds_remaining = difference.seconds
           hours = seconds_remaining // 3600
           minutes = (seconds_remaining % 3600) // 60
           seconds = seconds_remaining % 60

           print(f"\nTarih farkı: {days} gün, {hours} saat, {minutes} dakika, {seconds} saniye.")
    except ValueError:
        print("\nHatalı tarih formatı. Lütfen tekrar deneyin.")

# Fonksiyonu çalıştır
if __name__ == "__main__":
    countdown_calculator()
