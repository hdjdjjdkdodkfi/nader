#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import json
from datetime import datetime, date

# --- تعريف الألوان ---
RED = "\033[1;31m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def print_banner():
    print(fr'''
{PURPLE}<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>
{GREEN} _ {RED}  _  {GREEN} _   {RED}_  {GREEN} _
{GREEN}/ \ {RED}/ \ {GREEN}/ \ {RED}/ \ {GREEN}/ \  
 {GREEN}N | A | D | E | R 
{RED}\_/ {GREEN}\_/{RED} \_/ {GREEN}\_/ {RED}\_/
{PURPLE}<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>
{WHITE}𝐅𝐈𝐑𝐄   :{GREEN}  [ النسخة الشاملة - أدق التفاصيل المستخرجة ]
{WHITE}𝐕𝐞𝐫𝐬𝐢𝐨𝐧  : {GREEN}4.7.0 (Ultra Detail)
{WHITE}Telegram : {GREEN} @N_0_N_7
{PURPLE}<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>
''')

# --- الإعدادات ---
BASE_URL_WFP = "https://pal.beneficiaryregistration.cbt.wfp.org/api/v2/submission/retrieve/"
HEADERS_ZEZ = {
    'User-Agent': "Dalvik/2.1.0",
    'Authorization': "Basic WmV6c29mdFVzZXJAMjAyNTpaZXpzb2Z0JFBhc3MjMjAyNQ=="
}

# =========================
# أدوات التنسيق المطورة
# =========================
def clean_val(v):
    if v is None or str(v).lower() in ("none", "null", ""): return "غير متوفر"
    if v is True or str(v).lower() == "true": return "نعم"
    if v is False or str(v).lower() == "false": return "لا"
    return str(v)

def draw_box(title, content_list):
    width = 55 
    lines = []
    lines.append(f"{CYAN}╔{'═' * width}╗{RESET}")
    title_str = f" {title} "
    lines.append(f"{CYAN}║{WHITE}{title_str.center(width)}{CYAN}║{RESET}")
    lines.append(f"{CYAN}╠{'═' * width}╣{RESET}")
    for label, val in content_list:
        v = clean_val(val)
        lbl = str(label)
        # حساب المسافة لضمان استقامة العمود ║
        content_len = len(lbl) + len(v) + 4
        padding = " " * max(0, width - content_len)
        lines.append(f"{CYAN}║ {RED}{lbl}: {GREEN}{v}{padding} {CYAN}║{RESET}")
    lines.append(f"{CYAN}╚{'═' * width}╝{RESET}")
    return "\n".join(lines)

# =========================
# معالجة البحث الشامل (WFP)
# =========================
def handle_wfp_search(nid):
    try:
        print(f"\n{YELLOW}🔄 جاري استخراج أدق التفاصيل من قاعدة البيانات...{RESET}\n")
        r = requests.get(BASE_URL_WFP + nid, timeout=30)
        if r.status_code != 200:
            print(f"{RED}❌ لم يتم العثور على سجلات لهذه الهوية.{RESET}")
            return
        
        d = r.json()
        
        # 1. معلومات السكن واللجوء (تفصيلي)
        shelter_info = [
            ("حالة السكن", d.get('shelterType')),
            ("تاريخ النزوح", str(d.get('dateofDisplacement', ''))[:10]),
            ("عدد مرات النزوح", d.get('hhdisplacement')),
            ("حالة اللجوء", d.get('refugeeStatus')),
            ("كود المنطقة (Admin4)", d.get('admin4')),
            ("نوع الإقامة", d.get('adminAccomodation')),
            ("تاريخ تقديم الطلب", str(d.get('created_date', ''))[:10])
        ]
        print(draw_box("🏠 تفاصيل السكن والنزوح المتقدمة", shelter_info))

        # 2. بيانات رب الأسرة (تفصيلي)
        hoh_info = [
            ("الاسم الأول", d.get('hohfirstName')),
            ("اسم الأب", d.get('hohfathersName')),
            ("اسم الجد", d.get('hohgrandfathersName')),
            ("اسم العائلة", d.get('hohlastName')),
            ("رقم الهوية", d.get('documentNumber')),
            ("الجنس", "ذكر" if d.get('hohgender') == "M" else "أنثى"),
            ("تاريخ الميلاد", str(d.get('hohdob', ''))[:10]),
            ("العمر الدقيق", f"{d.get('hohage')} سنة"),
            ("الحالة الاجتماعية", d.get('hohmaritalStatus')),
            ("هل يعاني من إعاقة؟", d.get('hhpwd'))
        ]
        print(draw_box("👤 بيانات ربّ الأسرة التفصيلية", hoh_info))

        # 3. وسائل الاتصال
        contacts = [
            ("رقم الجوال الأساسي", d.get('primaryPhoneNumber')),
            ("رقم الجوال الثانوي", d.get('secondaryPhoneNumber'))
        ]
        print(draw_box("📞 معلومات التواصل", contacts))

        # 4. أفراد العائلة (كل عضو بتفاصيله)
        members = d.get("family_members_information", [])
        for idx, m in enumerate(members, 1):
            if m.get("deleted"):
                status = "🗑️ (عضو محذوف من الملف)"
            else:
                status = f"👪 عضو رقم ({idx})"

            m_details = [
                ("الاسم بالكامل", f"{m.get('hhmemberfirstName')} {m.get('hhmemberlastName')}"),
                ("اسم الأب", m.get('hhmemberfathersName')),
                ("الصلة برب الأسرة", m.get('hhmemberrelation')),
                ("رقم الهوية", m.get('hhmemberdocumentNumber')),
                ("تاريخ الميلاد", str(m.get('hhmemberdob', ''))[:10]),
                ("العمر", f"{m.get('hhmemberage')} سنة"),
                ("الجنس", "ذكر" if m.get('hhmembergender') == "M" else "أنثى"),
                ("يعاني من إعاقة؟", m.get('hhmemberpwd')),
                ("حالة الحمل", m.get('hhmemberpregnant')),
                ("حالة الرضاعة", m.get('hhmemberlactating'))
            ]
            print(draw_box(status, m_details))

    except Exception as e:
        print(f"{RED}❌ فشل الاستخراج: {e}{RESET}")

# =========================
# معالجة البحث في الأرشيف (Archive)
# =========================
def handle_archive_search(url, payload):
    try:
        print(f"\n{YELLOW}🔎 جاري سحب بيانات الأرشيف التفصيلية...{RESET}\n")
        res = requests.post(url, headers=HEADERS_ZEZ, data=payload)
        js = res.json()
        if 'psarchive' in js and js['psarchive']:
            for p in js['psarchive']:
                p_info = [
                    ("الاسم الكامل", f"{p.get('name','')} {p.get('father','')} {p.get('gfather','')} {p.get('family','')}".strip()),
                    ("رقم الهوية", p.get('id')),
                    ("تاريخ الميلاد", p.get('birth')),
                    ("العمر", f"{p.get('numage')} سنة"),
                    ("الجنس", p.get('sex')),
                    ("الحالة الاجتماعية", p.get('status')),
                    ("المحافظة", p.get('mohafzacode')),
                    ("المنطقة/الحي", p.get('areacode')),
                    ("الناحية", p.get('nahea')),
                    ("الحي السكني", p.get('hae')),
                    ("ملاحظات الأرشيف", p.get('notes'))
                ]
                print(draw_box("📄 بيانات الأرشيف المستخرجة", p_info))
        else:
            print(f"{RED}❌ لا توجد بيانات مطابقة في الأرشيف.{RESET}")
    except Exception as e:
        print(f"{RED}⚠️ خطأ: {e}{RESET}")

# =========================
# القائمة الرئيسية
# =========================
def main():
    while True:
        print_banner()
        print(f"{WHITE} اختر نوع البحث لاستخراج البيانات:{RESET}")
        print(f"{CYAN}1. {GREEN}استخراج شامل (WFP) - أدق تفاصيل الملف العائلي")
        print(f"{CYAN}2. {GREEN}استخراج أرشيف (بالاسم الثلاثي والعائلة)")
        print(f"{CYAN}3. {GREEN}استخراج أرشيف (برقم الهوية)")
        print(f"{CYAN}4. {RED}خروج{RESET}")
        
        choice = input(f"\n{YELLOW}🎯 رقم العملية: {RESET}").strip()

        if choice == '1':
            nid = input(f"{WHITE}أدخل رقم الهوية (WFP): {RESET}").strip()
            if nid: handle_wfp_search(nid)
        elif choice == '2':
            n = input("الاسم الأول: "); f = input("اسم الأب: "); l = input("اسم العائلة: ")
            handle_archive_search("https://zezsoft.eu/PSApp/PsArchive/getPFF.php", {"name": n, "father": f, "family": l})
        elif choice == '3':
            nid = input("رقم الهوية (Archive): ")
            handle_archive_search("https://zezsoft.eu/PSApp/PsArchive/getIDP.php", {"id": nid, "type": "1"})
        elif choice == '4':
            break
        
        input(f"\n{CYAN}--- اضغط Enter للعودة للرئيسية ---{RESET}")

if __name__ == "__main__":
    main()
