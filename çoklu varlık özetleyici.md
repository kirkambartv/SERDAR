from transformers import pipeline

# Özetleme motoru
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Varlıklar ve içerikleri
data = {
    "CAT": """
    2025 yılında Caterpillar için analistlerin beklentisi altyapı yatırımlarının artmasıyla büyüme yönünde.
    Truist Securities analisti Jamie Cook, hedef fiyatı 582$ olarak belirledi.
    Citigroup analisti Kyle Menges ise 540$ hedefiyle güçlü al önerisi verdi.
    Ancak bazı analistler, döngüsel endüstri yapısı nedeniyle kısa vadeli dalgalanmalara dikkat çekiyor.
    """,
    "WULF": """
    TeraWulf, AI ve HPC altyapısına geçişle birlikte analistlerin ilgisini çekiyor.
    Clear Street ve Roth Capital, fiyat hedeflerini yükseltti.
    Brüt kâr marjı %43.8 olsa da borç oranı yüksek.
    """,
    "CSCO": """
    Cisco Systems, AI ve bulut yatırımlarıyla büyüme hedefliyor.
    25 analistin ortalama hedefi $74.89; en yüksek tahmin $87.
    Döngüsel teknoloji harcamaları fiyatı etkileyebilir.
    """,
    "NVDA": """
    NVIDIA, AI devriminin merkezinde yer alıyor.
    2025’te %36 yükseliş yaşadı.
    Goldman Sachs 2026 için $4,900 hedefi verdi.
    """,
    "GOLD": """
    Altın fiyatları 2025’te %51 yükseldi.
    Ed Yardeni 2026’da $5,000, 2028’de $10,000 hedefliyor.
    Fed faiz indirimleri ve merkez bankası alımları fiyatı destekliyor.
    """,
    "SILVER": """
    Gümüş 2025’te %30’dan fazla yükseldi.
    Citigroup 2026 için $43 tahmini yaptı.
    Solar enerji ve elektronik talebi fiyatı yukarı çekiyor.
    """
}

# Özetleme ve çıktı
for name, text in data.items():
    summary = summarizer(text, max_length=100, min_length=40, do_sample=False)
    print(f"\n📌 {name} Özet:\n{summary[0]['summary_text']}")
