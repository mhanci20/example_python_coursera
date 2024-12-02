#!/usr/bin/env python3

import tkinter as tk

def quiz():
    pencere = tk.Tk()
    pencere.title("Quiz Uygulaması")
    pencere.geometry("600x300")

    sorular = [
        "7.806.787 ve 7.849.137 arasında hangisi büyüktür?",
        "1,2,3,4,5,6,7,8 ve 9 rakamları birer defa kullanılarak 9 basamaklı 500.000.000'dan küçük en büyük doğal sayıyı bulunuz?",
        "1.004.502 sayısının milyonlar bölüğü 1'dir. İfadesi doğru mu yanlış mı? Cevabını yazınız.",
        "2,8,0,5,7,1,3 rakamları kullanılarak yazılabilecek en büyük doğal sayı hangisidir?",
        "42.287.175 sayısında 287 hangi bölüktedir?",
        "Bir bisikletli sabit hızla yarım saatte 30.000 m yol almaktadır. Aynı hızla devam ederse 1 saatte kaç km yol alır?"
    ]

    cevaplar = ["7.849.137", "498.765.321", "doğru", "8753210", "binler", "60"]

    index = 0

    def sonraki_soru():
        nonlocal index
        if index < len(sorular):
            soru_etiket.config(text=sorular[index])
            cevap_girisi.delete(0, tk.END)  # Cevap giriş alanını temizle
        else:
            pencere.destroy()
            print("Quiz tamamlandı!")

    # Soru etiketini oluştur ve yerleştir
    soru_etiket = tk.Label(pencere, text=sorular[index], font=("Helvetica", 20), wraplength=500)
    soru_etiket.grid(row=0, column=0, columnspan=2, pady=30)

    # Cevap girişi alanı
    cevap_girisi = tk.Entry(pencere, font=("Helvetica", 16))
    cevap_girisi.grid(row=1, column=0, columnspan=2, pady=10)

    # Cevap kontrolü fonksiyonu
    def cevap_kontrol(cevap):
        nonlocal index
        if index < len(cevaplar):
            dogru_cevap = cevaplar[index].strip().lower()  # Doğru cevabı alıp küçük harfe çevir
            girilen_cevap = cevap.strip().lower()  # Kullanıcının cevabını küçük harfe çevir

            if girilen_cevap == dogru_cevap:
                print("Doğru cevap!")
            else:
                print(f"Yanlış cevap! Doğru cevap: {cevaplar[index]}")

            index += 1  # Cevap kontrolünden sonra index'i artır
            sonraki_soru()  # Sonraki soruyu göster

    # Cevapla düğmesi
    cevapla_dugmesi = tk.Button(pencere, text="Cevapla", command=lambda: cevap_kontrol(cevap_girisi.get()))
    cevapla_dugmesi.grid(row=2, column=1)

    pencere.mainloop()

quiz()
