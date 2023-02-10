# Random Dengan Banyak Kata
import pyautogui, time, random
posisi = pyautogui.position()

for a in range(10):
	pilihan = ['Hai','Kamu','Saa','Kita','Bisa']
	x = random.choice(pilihan)
	print(x)
	pyautogui.click(posisi.x,posisi.y)
	pyautogui.typewrite(x)
	time.sleep(0.2)
	pyautogui.typewrite(["Enter"])
	


# # Random Dengan 1 Kata
# import pyautogui, time, random
# posisi = pyautogui.position()
# pesan = "Tes"

# for a in range(5):
# 	pyautogui.click(posisi.x,posisi.y)
# 	pyautogui.typewrite(x)
# 	print(pesan)
# 	time.sleep(0.2)
# 	pyautogui.typewrite(["Enter"])
	