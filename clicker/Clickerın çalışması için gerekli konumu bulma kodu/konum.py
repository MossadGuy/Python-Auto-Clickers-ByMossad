import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"Mouse'un mevcut konumu: ({x}, {y})")

#konumunu girmesi için mousun üzerisinde durması yeterlidir
#Not: OUTPUT üzerinde düzgün çalışmaz donmalar yaşanabilir bundan dolayı terminale python konum.py yazarak çalıştırılması daha stabil olur