#!/usr/bin/env python3

def chatbot_response(user_input):
    if "merhaba" in user_input.lower():
        return "Merhaba! Sana nasıl yardımcı olabilirim?"
    elif "hava nasıl" in user_input.lower():
        return "Bugün hava güzel görünüyor!"
    elif "favori rengin ne" in user_input.lower():
        # Kullanıcıya favori rengini sormak
        print("Chatbot: Sen hangi rengi istersin? (Seçenekler: mavi, siyah, kırmızı, sarı, beyaz, turuncu, pembe)")
        user_color = input("Sen: ").lower()


        # Renkler listesi
        colors = ["mavi", "siyah", "kırmızı", "sarı", "beyaz", "turuncu", "pembe"]

        # Kullanıcının seçimi doğrulanır
        if user_color in colors:
            if user_color == "mavi":
                return "Tabii ki mavi! Gökyüzünün rengi :)"
            else:
                return f"Çok güzel bir renk, ben de {user_color} rengini seviyorum!"
        else:
            return "Üzgünüm, bu renk listede yok. Lütfen seçeneklerden birini seç."
    elif "kız arkadaş konusunda yardım et" in user_input.lower():
        return "Bu konuda yardımcı olamam kovboy. Kızlara özel davranman yeterli diye düşünüyorum"
    elif "teşekkürler" in user_input.lower():
        return "Rica ederim! Başka bir sorunuz var mı?"
    else:
        return "Üzgünüm, bu konuda pek bir bilgim yok."

def chatbot():
    print("Chatbot: Merhaba! Bana bir şeyler sorabilirsin. Çıkmak için 'çıkış' yaz.")
    while True:
        user_input = input("Sen: ")
        if user_input.lower() == "çıkış":
            print("Chatbot: Görüşmek üzere!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
