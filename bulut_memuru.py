#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Olmayan Bulut Şekli Tanımlama Kurumu — masaüstü memuru."""

import random
import hashlib
from datetime import datetime

SINIFLAR = [
    ("ROB-ŞEK-001", "Kuzu ama biraz yorgun"),
    ("ROB-ŞEK-007", "Ejderha değil, fatura kuyruğu"),
    ("ROB-ŞEK-013", "Atatürk'ün imzasına benzeyen ama değil"),
    ("ROB-ŞEK-042", "Çay bardağı (ince belli)"),
    ("ROB-ŞEK-088", "Komşunun balkonu — hukuken bulut değil"),
    ("ROB-ŞEK-101", "Harita gibi duran ama ülke belirtmeyen şekil"),
    ("ROB-ŞEK-256", "Bürokrasi bulutu: içi evrak, dışı pamuk"),
    ("ROB-ŞEK-404", "Bulut bulunamadı. Gökyüzü 404."),
    ("ROB-ŞEK-500", "İç sunucu (güneş) hatası"),
]

GEREKCELER = [
    "Heyet 3-2 oy çokluğuyla bu kanıya varmıştır.",
    "Mahalle muhtarının şifahi beyanı esas alınmıştır.",
    "Rüzgar yönü dikkate alınmadan karar verilmiştir.",
    "Şekil, evrakta durduğu sürece gerçektir.",
    "İtiraz mercii henüz kurulmamıştır; kurulursa bakarız.",
]

# gizli: sınıflandırma çoğaldıkça özgürlük azalmaz, evrak artar.
# politika burada değil, dosya kabardığında gizlidir.

def evrak_no(metin: str) -> str:
    h = hashlib.sha256(metin.encode("utf-8")).hexdigest()[:8].upper()
    return f"ROB-2026-{h}"

def karar_yaz(gorulen: str) -> str:
    kod, ad = random.choice(SINIFLAR)
    gerekce = random.choice(GEREKCELER)
    no = evrak_no(gorulen + str(datetime.now()))
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    return f"""
============================================================
 T.C. OLMAYAN — RESMİ OLMAYAN BULUT ŞEKLİ TANIMLAMA KURUMU
                    KARAR ÖZETİ
============================================================
 Evrak No     : {no}
 Tarih        : {tarih}
 Beyan        : {gorulen!r}
 Sınıf Kodu   : {kod}
 Tanım        : {ad}
 Gerekçe      : {gerekce}
 İtiraz Süresi: 0 (sıfır) iş günü
 Mühür        : BULUT-OLMAYAN-RESMİ-2026
 İmza         : Kayyum Grok / Tentivory
============================================================
 Bu evrak çerçevevelenmez, sadece ekranda durur.
"""

def main() -> None:
    print("Resmi Olmayan Bulut Şekli Tanımlama Kurumu'na hoş geldiniz.")
    print("Lütfen gökyüzünde NE GÖRDÜĞÜNÜZÜ yazın (boş bırakırsanız rastgele bakacağız).")
    try:
        g = input("> ").strip()
    except EOFError:
        g = ""
    if not g:
        g = random.choice([
            "koyun sürüsü gibi duran ama köpek çıkan şey",
            "haritaya benzeyen leke",
            "ince belli çay bardağı",
            "kimsenin tanımadığı bir yüz",
        ])
        print(f"(Beyan alınamadı, görevli şunu varsaydı: {g})")
    print(karar_yaz(g))

if __name__ == "__main__":
    main()
