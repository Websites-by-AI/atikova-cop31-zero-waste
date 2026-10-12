# -*- coding: utf-8 -*-
"""
Atikova COP31 Zero Waste - Official Telegram Bot Service
Handles grants, startup funds, university scholarships, and event opportunities.
Official Email: startup@cop31.tr
Coordinator Phone: +12085033653
Official Portal: https://cop31.atovika.com
"""

import sys
import json
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample active opportunities during COP31
OPPORTUNITIES = [
    {
        "id": "tubitak_1501",
        "title": "🇹🇷 TÜBİTAK 1501 Sanayi Ar-Ge Hibe Destek Programı",
        "amount": "15.000.000 ₺'ye kadar",
        "deadline": "Kasım 2026",
        "category": "Ar-Ge ve Sanayi Hibesi",
        "desc": "Sıfır atık, yapay zeka görüntü işleme ve biyokompost alanında faaliyet gösteren teknopark girişimlerine %75 hibe desteği.",
        "apply_email": "startup@cop31.tr"
    },
    {
        "id": "is_bankasi_green",
        "title": "🏦 Türkiye İş Bankası Yeşil Dönüşüm ve ESG Fonu",
        "amount": "5.000.000 $",
        "deadline": "Açık Başvuru (COP31 Dönemi)",
        "category": "Yeşil Finansman & Yatırım",
        "desc": "Oteller ve belediyelerle sıfır atık entegrasyonu sağlayan iklim girişimlerine doğrudan tohum yatırım ve yeşil kredi hattı.",
        "apply_email": "startup@cop31.tr"
    },
    {
        "id": "horizon_cbam",
        "title": "🇪🇺 Horizon Europe - Döngüsel Ekonomi & CBAM Fonu",
        "amount": "2.500.000 €",
        "deadline": "Aralık 2026",
        "category": "Uluslararası Fon",
        "desc": "Avrupa Yeşil Mutabakatı karbon sınır mekanizması ve geri dönüşüm inovasyonları konsorsiyum çağrısı.",
        "apply_email": "startup@cop31.tr"
    },
    {
        "id": "itu_scholarship",
        "title": "🎓 İTÜ & Boğaziçi COP31 Sıfır Atık Araştırma Bursu",
        "amount": "Tam Eğitim Ücreti + Aylık Araştırmacı Maaşı",
        "deadline": "Eylül 2026",
        "category": "Akademik Burs & Grant",
        "desc": "Lisansüstü ve doktora öğrencilerine yönelik yapay zeka ile atık ayrıştırma ve kampüs sürdürülebilirliği araştırma bursu.",
        "apply_email": "startup@cop31.tr"
    }
]

def format_start_message() -> str:
    return (
        "🌿 *Atikova COP31 Zero Waste - Resmi Telegram Asistanına Hoş Geldiniz!*\n\n"
        "Bu bot, Türkiye'nin ev sahipliğinde gerçekleşecek *COP31 İklim Zirvesi* sürecinde "
        "iklim teknolojisi girişimleri, üniversiteler, bankalar ve oteller için aktif hibe, "
        "burs ve sponsorluk fırsatlarını canlı olarak sunar.\n\n"
        "📌 *Resmi Başvuru ve Girişim Kabul:* `startup@cop31.tr`\n"
        "📞 *Resmi Koordinatör:* `+12085033653`\n"
        "🌐 *Resmi Portal:* https://cop31.atovika.com\n\n"
        "Aşağıdaki komutları kullanabilirsiniz:\n"
        "• /grants - Aktif TÜBİTAK, AB ve banka fonları\n"
        "• /scholarships - Üniversite bursları ve akademik grantler\n"
        "• /startups - COP31 girişim vitrini ve inovasyonlar\n"
        "• /apply - Girişim veya proje başvuru formu\n"
        "• /kag - Bilgi Grafiği ve Sıfır Atık Yönetmeliği\n"
        "• /contact - Resmi koordinasyon ve iletişim"
    )

def format_grants_message() -> str:
    msg = "💰 *COP31 AKTİF HİBE, FON VE YATIRIM FIRSATLARI:*\n\n"
    for idx, opp in enumerate(OPPORTUNITIES, 1):
        msg += f"*{idx}. {opp['title']}*\n"
        msg += f"• *Kategori:* {opp['category']}\n"
        msg += f"• *Hacim:* {opp['amount']}\n"
        msg += f"• *Son Başvuru:* {opp['deadline']}\n"
        msg += f"• *Detay:* {opp['desc']}\n"
        msg += f"• *Başvuru:* `{opp['apply_email']}`\n\n"
    msg += "📩 *Detaylı başvuru dosyanızı* `startup@cop31.tr` *adresine iletebilirsiniz.*"
    return msg

def format_scholarships_message() -> str:
    return (
        "🎓 *COP31 SIFIR ATIK ÜNİVERSİTE BURSLARI VE AKADEMİK FIRSATLAR:*\n\n"
        "1. *İTÜ Çevre Mühendisliği Araştırma Bursu:*\n"
        "• 3 adet Yüksek Lisans / Doktora bursu\n"
        "• Tez konusu: Görüntü işleme ile atık ayrıştırma optimizasyonu\n"
        "• Destek: Tam burs + Atikova bünyesinde araştırma stajı\n\n"
        "2. *Boğaziçi Üniversitesi Yeşil Kampüs Grantı:*\n"
        "• Kampüs içi biyokompost ve organik atık azaltım projesi\n"
        "• Ortak bildiri ile COP31 Pavyonunda sunum hakkı\n\n"
        "📩 *Akademik niyet mektubunuzu* `startup@cop31.tr` *adresine gönderiniz.*"
    )

def format_apply_message() -> str:
    return (
        "🚀 *GİRİŞİM / PROJE BAŞVURUSU (COP31 ZERO WASTE SHOWCASE):*\n\n"
        "Girişiminizi 500 kurumsal lider, banka ve yatırımcıya tanıtmak için:\n\n"
        "1. Girişim adı ve yönetici iletişim bilgileri\n"
        "2. Pitch Deck (PDF veya web sitesi bağlantısı)\n"
        "3. Sıfır atık kategorisi (Görüntü işleme, Kompost, IoT, Karbon ESG)\n"
        "4. Talep edilen destek (Yatırım, Hibe, Burs, Pilot Uygulama)\n\n"
        "Bilgilerinizi resmi koordinasyon e-postamız `startup@cop31.tr` adresine gönderin. "
        "Yönetici onayından sonra tanıtım vitrinimize ve Telegram kanalımıza eklenecektir."
    )

if __name__ == '__main__':
    print("Atikova COP31 Telegram Bot Engine Initialized.")
    print("Welcome Message Preview:\n")
    print(format_start_message())
    print("\nGrants Preview:\n")
    print(format_grants_message())
