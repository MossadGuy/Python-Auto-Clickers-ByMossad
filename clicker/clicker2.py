import pyautogui
import time

tekrar_sayisi = int(input("Kaç kez tıklamak istediğinizi girin: ")) # 3 farklı yere tıklanacağında dolayı tek bir yere kaç kere tıklanacağı nı soruyor yani 12 kez tıkla yazarsak 12*3=36 olur bunun üzerinden hesap yapılmalı
tiklama_araligi_saniye = float(input("Tıklama aralığını saniye cinsinden girin: "))
tiklanacaklar_listesi = [(100, 100), (200, 200), (300, 300)]  # İstediğiniz koordinatları buraya giricen

tiklama_sayisi = 0

for _ in range(tekrar_sayisi):
    for konum in tiklanacaklar_listesi:
        x, y = konum
        pyautogui.click(x, y)
        tiklama_sayisi += 1
        print(f"{tiklama_sayisi} kez tıklandı.")
        time.sleep(tiklama_araligi_saniye)
