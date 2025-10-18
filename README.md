# Faruk-OSINT

**Faruk-OSINT** — temel, etik ve açık kaynak bir OSINT araç seti.  
Amaç: telefon numarası doğrulama, IP konumlandırma ve açık Instagram profil meta verilerini sorgulamak.

> ⚠️ Bu araç **etik ve yasal** kullanım için tasarlanmıştır.  
> Başkalarının kişisel verilerini izinsiz toplamak, başkalarını taciz etmek veya sitelerin kullanım şartlarını ihlal etmek yasaktır.

---

## 🚀 Hızlı kullanım
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Telefon
python osint.py phone +905XXXXXXXXX

# IP
python osint.py ip 8.8.8.8

# Instagram (kullanıcı adı)
python osint.py insta instagram_username
\`\`\`

---

## ⚙️ Konfigürasyon
\`src/config_example.yaml\` dosyasını \`src/config.yaml\` olarak kopyalayın  
ve varsa API anahtarlarınızı ekleyin.

---

## 🧾 Lisans
MIT License
