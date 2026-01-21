#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
from datetime import datetime, date

BASE_URL = "https://pal.beneficiaryregistration.cbt.wfp.org/api/v2/submission/retrieve/"

# =========================
# أدوات مساعدة
# =========================
def validate_id(text):
    text = (text or "").strip()
    if not re.fullmatch(r"\d{6,12}", text):
        raise ValueError("رقم الهوية غير صحيح (6–12 رقم)")
    return text

def calc_age(dob):
    if not dob:
        return ""
    try:
        d = datetime.strptime(str(dob)[:10], "%Y-%m-%d").date()
        today = date.today()
        y = today.year - d.year - ((today.month, today.day) < (d.month, d.day))
        return f"{y} سنة" if y >= 1 else "أقل من سنة"
    except:
        return ""

def yn(v):
    if str(v).lower() in ("true", "1", "yes"):
        return "نعم"
    if str(v).lower() in ("false", "0", "no"):
        return "لا"
    return "غير منطبق"

def gender(v):
    return {
        "M": "ذكر",
        "F": "أنثى",
        "MALE": "ذكر",
        "FEMALE": "أنثى"
    }.get(str(v).upper(), v or "")

def relation(v):
    return {
        "2": "زوجة",
        "3": "ابن",
        "4": "ابنة"
    }.get(str(v), v or "")

def safe(d, k, default=""):
    if isinstance(d, dict):
        return d.get(k, default)
    return default

# =========================
def fetch_data(nid):
    r = requests.get(
        BASE_URL + nid,
        headers={"Accept": "application/json"},
        timeout=30
    )
    r.raise_for_status()
    return r.json()

# =========================
def build_report(d):
    out = []

    out.append("🏠 أولاً: معلومات السكن والنزوح")
    if safe(d, "shelterType"):
        out.append(f"نوع السكن: {safe(d,'shelterType')}")
    if safe(d, "displacementDate"):
        out.append(f"تاريخ النزوح: {str(safe(d,'displacementDate'))[:10]}")
    if safe(d, "numberOfDisplacements"):
        out.append(f"عدد مرات النزوح للأسرة: {safe(d,'numberOfDisplacements')}")
    out.append("")

    out.append("👤 ثانياً: بيانات ربّ الأسرة")
    full = f"{safe(d,'hohfirstName')} {safe(d,'hohlastName')}".strip()
    out.append(f"الاسم الكامل: {full}")
    out.append(f"الجنس: {gender(safe(d,'hohgender'))}")
    out.append(f"تاريخ الميلاد: {str(safe(d,'hohdob'))[:10]}")
    out.append(f"العمر: {calc_age(safe(d,'hohdob'))}")
    out.append(f"اسم الأب: {safe(d,'hohfathersName')}")
    out.append(f"اسم الجد: {safe(d,'hohgrandfathersName')}")
    out.append(f"الحالة الاجتماعية: {safe(d,'hohmaritalStatus')}")
    out.append(f"الحالة السكنية: {yn(safe(d,'hohresidentialStatus'))}")
    out.append(f"حالة الإعاقة (PWD): {yn(safe(d,'hhpwd'))}")
    out.append(f"رقم الهوية: {safe(d,'documentNumber')}")
    out.append("نوع الوثيقة: هوية وطنية (NID)")
    out.append("")

    out.append("📞 ثالثاً: معلومات الاتصال")
    if safe(d, "primaryPhoneNumber"):
        out.append(f"رقم الهاتف الأساسي: {safe(d,'primaryPhoneNumber')}")
    if safe(d, "secondaryPhoneNumber"):
        out.append(f"رقم الهاتف الثانوي: {safe(d,'secondaryPhoneNumber')}")
    out.append("")

    out.append("👪 رابعاً: معلومات أفراد الأسرة")
    members = safe(d, "family_members_information", [])
    idx = 1

    for m in members:
        if m.get("deleted") is True:
            out.append("🗑️ عضو محذوف (غير محتسب ضمن الأسرة)")
            out.append(f"الاسم: {m.get('hhmemberfirstName','')} {m.get('hhmemberlastName','')}")
            out.append(f"تاريخ الميلاد: {str(m.get('hhmemberdob'))[:10]}")
            out.append(f"العمر: {calc_age(m.get('hhmemberdob'))}")
            out.append(f"رقم الهوية: {m.get('hhmemberdocumentNumber')}")
            out.append("")
            continue

        out.append(f"{idx}️⃣ {m.get('hhmemberfirstName','')} {m.get('hhmemberlastName','')}")
        out.append(f"صلة القرابة: {relation(m.get('hhmemberrelation'))}")
        out.append(f"الجنس: {gender(m.get('hhmembergender'))}")
        out.append(f"تاريخ الميلاد: {str(m.get('hhmemberdob'))[:10]}")
        out.append(f"العمر: {calc_age(m.get('hhmemberdob'))}")
        out.append(f"رقم الهوية: {m.get('hhmemberdocumentNumber')}")
        out.append(f"حالة الحمل: {yn(m.get('hhmemberpregnant'))}")
        out.append(f"حالة الرضاعة: {yn(m.get('hhmemberlactating'))}")
        out.append(f"حالة الإعاقة: {yn(m.get('hhmemberpwd'))}")
        out.append("")
        idx += 1

    return "\n".join(out)

# =========================
def main():
    try:
        nid = validate_id(input("أدخل رقم الهوية: "))
        print("\nجاري جلب البيانات...\n")
        data = fetch_data(nid)
        print(build_report(data))
    except Exception as e:
        print(f"\nخطأ: {e}")

if __name__ == "__main__":
    main()