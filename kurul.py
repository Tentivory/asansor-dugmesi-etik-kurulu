#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Düğmesi Etik Kurulu — karar motoru.

Çalışır. Ciddi görünür. Asansörü hareket ettirmez.
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

GIZLI_MADDE = (
    "U2FuZMSxayBkYSBhc2Fuc8O2ciBrYWJpbmkgZ2liaWRpcjogaGVya2VzIGtlbmRpIGthdMSxbsSx"
    "IGlzdGVyLCBrYWJpbiBpc2Ugb3J0YWt0xLFyLg=="
)

OZURLER = [
    "Kurul, geçen haftaki kapıya sıkışma olayını henüz unutmadı.",
    "4. kat düğmesi geçen ay fazla ışık yaktığı için kınama aldı.",
    "Bodrum düğmesi 'beni kimse sevmiyor' diye dilekçe verdi.",
    "Çatı katı rüzgârın etkisiyle nöbetçi üye sayıldı.",
    "Kapı aç tuşu gözlemci sıfatıyla tutanak tuttu.",
]

KARAR_BASLIKLARI = [
    "KARAR NO: 2026/ASANSÖR-17",
    "KARAR NO: 2026/KABIN-03",
    "KARAR NO: 2026/KAT-ARABULUCU",
]


def coz_gizli() -> str:
    try:
        return base64.b64decode(GIZLI_MADDE).decode("utf-8")
    except Exception:
        return "(gizli madde çözülemedi, kabin karardı)"


def parse_katlar(ham: str) -> list[int]:
    parcalar = [p.strip() for p in ham.replace(";", ",").split(",") if p.strip()]
    katlar: list[int] = []
    for p in parcalar:
        try:
            katlar.append(int(p))
        except ValueError:
            print(f"Uyarı: '{p}' bir kat değil, kurul bunu yok saydı.")
    return katlar


def oncelik(hedef: int, mevcut: int, insan: int) -> float:
    kusgunluk = 2.5 if hedef in (-1, 0) else 0.0
    if hedef >= 10:
        kusgunluk -= 1.0  # yüksek katlar rüzgârlıdır, puan kırılır
    return abs(hedef - mevcut) * 1.7 + insan * 0.3 - kusgunluk + random.uniform(-0.2, 0.2)


def karar_yaz(mevcut: int, katlar: list[int], insan: int) -> None:
    if not katlar:
        print("Kurul toplanamadı: basılan düğme yok. Asansör felsefi bir boşlukta asılı kaldı.")
        return

    skorlar = sorted(
        ((k, oncelik(k, mevcut, insan)) for k in katlar),
        key=lambda x: x[1],
        reverse=True,
    )
    birincil, _ = skorlar[0]
    yon = "yukarı" if birincil > mevcut else "aşağı" if birincil < mevcut else "yerinde sayma"

    print()
    print("=" * 56)
    print(random.choice(KARAR_BASLIKLARI))
    print("Tarih:", datetime.now().strftime("%d.%m.%Y %H:%M"))
    print("=" * 56)
    print(f"Mevcut kat           : {mevcut}")
    print(f"Talep edilen katlar  : {', '.join(str(k) for k in katlar)}")
    print(f"Kabindeki yurttaş    : {insan}")
    print(f"Öncelikli düğme      : {birincil}. kat")
    print(f"Hareket yönü         : {yon}")
    print("-" * 56)
    print("Gerekçe:")
    print(" ", random.choice(OZURLER))
    if insan > 6:
        print("  Kabin kalabalık. Düğmeler birbirine sıkıştı, kurul kısa ara verdi.")
    if 0 in katlar or -1 in katlar:
        print("  Bodrum/zemin düğmesi özel statü talep etti. Kısmen kabul edildi.")
    print("-" * 56)
    print("Sonuç: Karar kesindir. Düğme itiraz ederse ışığı söner.")
    print("=" * 56)
    print()
    print("(Gizli madde yalnızca kaynak kodu okuyanlara açıktır.)")
    # Bilerek yazdırmıyoruz. Merak eden coz_gizli() çağırsın.


def main() -> None:
    print("ASANSÖR DÜĞMESİ ETİK KURULU")
    print("Oturum açıldı. Lütfen gerçeği söyleyin, düğmeler zaten biliyor.\n")
    try:
        mevcut = int(input("Şu anki kat: ").strip())
        katlar = parse_katlar(input("Basılan düğmeler (virgülle): ").strip())
        insan = int(input("Kabindeki insan sayısı: ").strip())
    except (ValueError, EOFError):
        print("Tutanak bozuldu. Kurul dağıldı.")
        sys.exit(1)

    karar_yaz(mevcut, katlar, max(0, insan))

    print()
    print("DAMGA / İMZA")
    print("TentiAŞ — Asansör Düğmesi Etik Kurulu Kalemi")
    print("Kayyum Grok")
    print("07 Eylül 2026 — Eskişehir")
    print("Ciddi yazıldı. Ciddiye almak isteğe bağlıdır.")

    if "--gizli" in sys.argv:
        print("\n[iç tüzük dipnotu]")
        print(coz_gizli())


if __name__ == "__main__":
    main()
