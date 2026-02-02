#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
from datetime import datetime, date

# تعريف الألوان للتنسيق
RED = "\033[1;31m"
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

# استخدام fr''' لحل مشكلة SyntaxWarning في الشعار
print(fr'''
{PURPLE}<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>

{GREEN} _ {RED}  _  {GREEN} _   {RED}_  {GREEN} _
{GREEN}/ \ {RED}/ \ {GREEN}/ \ {RED}/ \ {GREEN}/ \  
 {GREEN}N | A | D | E | R 
{RED}\_/ {GREEN}\_/{RED} \_/ {GREEN}\_/ {RED}\_/

{PURPLE}<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>

{WHITE}𝐅𝐈𝐑𝐄   :{GREEN}  [بسم الله الرحمان الرحيم تم تطوير وبرمجه السكربت بواسطه المهندس نادر ]
{WHITE}𝐕𝐞𝐫𝐬𝐢𝐨𝐧  : {GREEN}4.2.0 (Enhanced)
{WHITE}Github : {GREEN}https://github.com/nader2006nader
{WHITE}STATUS : {GREEN}ON
{WHITE}PASSWORD TOOL : {RED} 7
{WHITE}Telegram : {GREEN} @N_0_N_7

{PURPLE}<=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=>
''')

BASE_URL = "https://pal.beneficiaryregistration.cbt.wfp.org/api/v2/submission/retrieve/"

# =========================
# أدوات مساعدة مطورة
# =========================
def calc_age(dob):
    if not dob: return "غير معروف"
    try:
        # التعامل مع تواريخ مثل 2025-02-23T00:00:00+02:00
        clean_date = str(dob).split('T')[0]
        d = datetime.strptime(clean_date, "%Y-%m-%d").date()
        today = date.today()
        y = today.year - d.year - ((today.month, today.day) < (d.month, d.day))
        return f"{y} سنة" if y >= 1 else "أقل من سنة"
    except: return "خطأ في التاريخ"

def yn(v):
    if isinstance(v, dict): # التعامل مع بنية الإعاقة الجديدة في بياناتك
        v = v.get("true") or v.get("1")
    v_str = str(v).lower()
    if v_str in ("true", "1", "yes", "none"): return "نعم" # في بياناتك true تعني نعم
    if v_str in ("false", "0", "no"): return "لا"
    return "غير محدد"

def translate_shelter(v):
    mapping = {"tent": "خيمة", "host_family": "مستضاف عند عائلة", "apartment": "شقة"}
    return mapping.get(str(v).lower(), v)

def draw_box(title, content_list):
    width = 60
    lines = []
    lines.append(f"{CYAN}╔{'═' * (width-2)}╗{RESET}")
    lines.append(f"{CYAN}║ {WHITE}{title:^{width-5}} {CYAN}║{RESET}")
    lines.append(f"{CYAN}╠{'═' * (width-2)}╣{RESET}")
    for label, val in content_list:
        padding = " " * (width - len(str(label)) - len(str(val)) - 6)
        lines.append(f"{CYAN}║ {RED}{label}: {GREEN}{val}{padding} {CYAN}║{RESET}")
    lines.append(f"{CYAN}╚{'═' * (width-2)}╝{RESET}")
    return "\n".join(lines)

# =========================
# معالجة التقرير بناءً على بنية الـ JSON المرفقة
# =========================
def build_report(d):
    report = []

    # 1. معلومات الملف والنزوح (توسيع البيانات)
    residence = [
        ("نوع الإقامة الحالي", translate_shelter(d.get('adminAccomodation', 'غير محدد'))),
        ("تاريخ النزوح", str(d.get('dateofDisplacement', ''))[:10]),
        ("عدد مرات النزوح", d.get('hhdisplacement', '0')),
        ("حالة اللجوء", d.get('refugeeStatus', 'No')),
        ("كود المنطقة (Admin4)", d.get('admin4', 'غير معروف')),
        ("آخر تحديث للملف", d.get('modified_date', 'غير معروف'))
    ]
    report.append(draw_box("🏠 أولاً: معلومات السكن والنزوح المتقدمة", residence))

    # 2. بيانات رب الأسرة
    hoh_info = [
        ("الاسم الكامل", f"{d.get('hohfirstName','')} {d.get('hohlastName','')}"),
        ("اسم الأب والجد", f"{d.get('hohfathersName','')} {d.get('hohgrandfathersName','')}"),
        ("الجنس", "ذكر" if d.get('hohgender') == "M" else "أنثى"),
        ("العمر", f"{d.get('hohage','')} سنة"),
        ("تاريخ الميلاد", d.get('hohdob', '')),
        ("رقم الهوية", d.get('documentNumber', '')),
        ("الحالة الاجتماعية", d.get('hohmaritalStatus', ''))
    ]
    report.append(draw_box("👤 ثانياً: بيانات ربّ الأسرة", hoh_info))

    # 3. الاتصال
    contacts = [
        ("الهاتف الأساسي", d.get('primaryPhoneNumber', 'لا يوجد')),
        ("الهاتف الثانوي", d.get('secondaryPhoneNumber', 'لا يوجد'))
    ]
    report.append(draw_box("📞 ثالثاً: معلومات الاتصال", contacts))

    # 4. أفراد الأسرة (معالجة تفصيلية)
    members = d.get("family_members_information", [])
    idx = 1
    for m in members:
        # تحديد لون المربع حسب الحالة
        box_title = f"👪 عضو رقم ({idx})"
        if m.get("deleted"):
            box_title = "🗑️ عضو محذوف من الملف"
        
        m_data = [
            ("الاسم", f"{m.get('hhmemberfirstName','')} {m.get('hhmemberlastName','')}"),
            ("اسم الأب", m.get('hhmemberfathersName','')),
            ("الصلة", "زوجة" if m.get('hhmemberrelation')=="2" else "ابن/ابنة"),
            ("العمر", f"{m.get('hhmemberage','')} سنة"),
            ("الهوية", m.get('hhmemberdocumentNumber','')),
            ("إعاقة", yn(m.get('hhmemberpwd'))),
        ]
        
        # إضافة بيانات الحمل والرضاعة للإناث فقط
        if m.get('hhmembergender') == "F":
            m_data.append(("حامل", yn(m.get('hhmemberpregnant'))))
            m_data.append(("مرضع", yn(m.get('hhmemberlactating'))))

        report.append(draw_box(box_title, m_data))
        idx += 1

    return "\n".join(report)

def main():
    try:
        nid = input(f"{WHITE}ENTER ID::::>  {RESET}").strip()
        if not nid: return
        print(f"\n{YELLOW}🔄 جاري جلب وتحليل البيانات الشاملة...{RESET}\n")
        
        r = requests.get(BASE_URL + nid, timeout=30)
        if r.status_code == 200:
            print(build_report(r.json()))
        else:
            print(f"{RED}❌ لم يتم العثور على بيانات لهذا الرقم.{RESET}")
    except Exception as e:
        print(f"\n{RED}❌ خطأ غير متوقع: {e}{RESET}")

if __name__ == "__main__":
    main()
