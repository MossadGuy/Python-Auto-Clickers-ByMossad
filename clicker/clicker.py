import pyautogui
import time

tiklanacaklar_listesi = [
    (2619, 250),
    (2971, 203),
    (2995, 278),
]

tiklama_araligi_saniye = 1

print("Program başlamadan önce 3 saniye süreniz var.")
time.sleep(3)

tekrar_sayisi = 6276

for _ in range(tekrar_sayisi):
    for konum in tiklanacaklar_listesi:
        x, y = konum
        pyautogui.click(x, y)
        time.sleep(tiklama_araligi_saniye)

print("Tıklamalar tamamlandı.")
