---
title: Atikova COP31 Zero Waste Engine
emoji: 🌿
colorFrom: emerald
colorTo: teal
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# Atikova COP31 Zero Waste Engine & Lead Operations

سامانه پیشرفته مدیریت لیدهای سازمانی، ماشین وضعیت (State Machine)، ره‌گیری حسگرهای IoT، و گرنت‌های تکنوپارک ترکیه (قانون ۴۶۹۱ و TÜBİTAK) برای اجلاس آب‌وهوایی COP31.

## 🚀 ویژگی‌های کلیدی
- **پایپ‌لاین ۶ مرحله‌ای ایجنت (Agent State Machine):** کشف لیدها ➔ ممیزی سانترال و موبایل ➔ ارزیابی پسماند صفر ➔ رتبه‌بندی قطعی P1/P2/P3 ➔ پرونده تکنوپارک و توبیتاک ➔ ارسال کنترل‌شده انسانی.
- **ویجت استعلام سریع (TrackWidget):** ره‌گیری بلادرنگ نرخ تفکیک زباله و سنسورهای IoT هوشمند با وارد کردن شناسه پرونده یا نام هتل/سازمان.
- **لیدهای پین‌شده طلایی (Pinned VIP Leads):** دسترسی سریع به هتل‌های کلیدی اجلاس COP31 در آنتالیا و استانبول (Rixos, Titanic, Maxx Royal, Swissôtel) و دانشگاه‌های مادر تکنوپارک (İTÜ, ODTÜ).
- **گارد هوشمند واتساپ (Smart PBX Guard):** تفکیک خودکار شماره‌های موبایل (05xx) از خطوط تلفن ثابت شهری و سانترال (02xx).
- **ارتباط یکپارچه چندکاناله:** واتساپ مستقیم، تلگرام، ایمیل سازمانی با درج شماره فرستنده اختصاصی `+12085033653`.
- **معماری استقرار دوگانه:** قابل استقرار بر روی Hugging Face Spaces (داکر پورت 7860) و Cloudflare Pages.

## 💻 اجرا به صورت محلی یا در داکر
```bash
python3 server.py
# یا با داکر:
docker build -t atikova-cop31 .
docker run -p 7860:7860 atikova-cop31
```
