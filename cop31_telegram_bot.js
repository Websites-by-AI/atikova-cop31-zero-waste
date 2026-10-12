/**
 * Atikova COP31 Zero Waste - Official Telegram Bot (Node.js / Cloudflare Worker)
 * Official Email: startup@cop31.tr
 * Coordinator Phone: +12085033653
 * Portal: https://cop31.atovika.com
 */

const OPPORTUNITIES = [
  {
    id: 'tubitak_1501',
    title: '🇹🇷 TÜBİTAK 1501 Sanayi Ar-Ge Hibe Destek Programı',
    amount: "15.000.000 ₺'ye kadar",
    deadline: 'Kasım 2026',
    category: 'Ar-Ge ve Sanayi Hibesi',
    desc: 'Sıfır atık, yapay zeka görüntü işleme ve biyokompost alanında teknopark girişimlerine %75 hibe desteği.',
    email: 'startup@cop31.tr'
  },
  {
    id: 'is_bankasi_green',
    title: '🏦 Türkiye İş Bankası Yeşil Dönüşüm ve ESG Fonu',
    amount: '5.000.000 $',
    deadline: 'Açık Başvuru (COP31 Dönemi)',
    category: 'Yeşil Finansman & Yatırım',
    desc: 'Oteller ve belediyelerle sıfır atık entegrasyonu sağlayan iklim girişimlerine doğrudan tohum yatırım.',
    email: 'startup@cop31.tr'
  },
  {
    id: 'horizon_cbam',
    title: '🇪🇺 Horizon Europe - Döngüsel Ekonomi & CBAM Fonu',
    amount: '2.500.000 €',
    deadline: 'Aralık 2026',
    category: 'Uluslararası Fon',
    desc: 'Avrupa Yeşil Mutabakatı karbon sınır mekanizması ve geri dönüşüm inovasyonları.',
    email: 'startup@cop31.tr'
  },
  {
    id: 'itu_scholarship',
    title: '🎓 İTÜ & Boğaziçi COP31 Sıfır Atık Araştırma Bursu',
    amount: 'Tam Eğitim Ücreti + Aylık Maaş',
    deadline: 'Eylül 2026',
    category: 'Akademik Burs & Grant',
    desc: 'Lisansüstü ve doktora öğrencilerine yönelik yapay zeka ile atık ayrıştırma araştırma bursu.',
    email: 'startup@cop31.tr'
  }
];

function handleTelegramCommand(command) {
  switch (command.toLowerCase()) {
    case '/start':
      return {
        text: `🌿 <b>Atikova COP31 Zero Waste - Resmi Telegram Asistanına Hoş Geldiniz!</b>\n\nCOP31 İklim Zirvesi hibe, burs ve fon fırsatları canlı olarak sunulmaktadır.\n\n📌 <b>Resmi Başvuru:</b> <code>startup@cop31.tr</code>\n📞 <b>Koordinatör:</b> <code>+12085033653</code>\n🌐 <b>Portal:</b> https://cop31.atovika.com`,
        keyboard: [
          [{ text: '💰 Aktif Hibe ve Fonlar', callback_data: '/grants' }, { text: '🎓 Üniversite Bursları', callback_data: '/scholarships' }],
          [{ text: '🚀 Girişim Başvurusu', callback_data: '/apply' }, { text: '📧 İletişim', callback_data: '/contact' }]
        ]
      };
    case '/grants':
      return {
        text: `💰 <b>COP31 AKTİF HİBE VE FONLAR:</b>\n\n` + OPPORTUNITIES.map(o => `<b>${o.title}</b>\n• Hacim: ${o.amount}\n• Son Başvuru: ${o.deadline}\n• E-posta: <code>${o.email}</code>\n`).join('\n')
      };
    case '/scholarships':
      return {
        text: `🎓 <b>COP31 SIFIR ATIK ÜNİVERSİTE BURSLARI:</b>\n\n• İTÜ Çevre Mühendisliği: 3 Adet Yüksek Lisans / Doktora bursu\n• Boğaziçi Yeşil Kampüs Projesi: Tam burs + staj\n\nBaşvuru: <code>startup@cop31.tr</code>`
      };
    case '/apply':
      return {
        text: `🚀 <b>Girişim Başvurusu:</b>\n\nProje özetinizi veya Pitch Deck dosyanızı <code>startup@cop31.tr</code> adresine gönderiniz.`
      };
    case '/contact':
      return {
        text: `📞 <b>Resmi İletişim Koordinasyonu:</b>\n\n• E-posta: <code>startup@cop31.tr</code>\n• Telefon / WhatsApp: <code>+12085033653</code>\n• Web: https://cop31.atovika.com`
      };
    default:
      return { text: 'Komut anlaşılamadı. Lütfen /start yazınız.' };
  }
}

if (require.main === module) {
  console.log("Telegram bot node handler test:");
  console.log(handleTelegramCommand('/start'));
  console.log(handleTelegramCommand('/grants'));
}

module.exports = { OPPORTUNITIES, handleTelegramCommand };
