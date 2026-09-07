# Asansör Düğmesi Etik Kurulu

> Bu belge, asansör kabini içindeki düğmelerin onurunu, sırasını ve ruhsal bütünlüğünü korumak üzere yazılmıştır.  
> İhlal eden düğme, **sessiz moda** alınır.

## 1. Kurulun Varlık Nedeni

Asansörde birden fazla kat tuşuna basıldığında düğmeler arasında kısa süreli ama derin bir diplomatik kriz yaşanır.  
4. kat düğmesi kendini “daha çok insan taşıyorum” diye üstün görür.  
Bodrum düğmesi ise “ben olmadan otopark olmaz” diye küsüp yanıp söner.

Bu yazılım o krizi **milli bir tören** gibi çözer.

## 2. Kurulum

```bash
python3 kurul.py
```

Bağımlılık yoktur. Yalnızca vicdan ve `python3` yeterlidir.

## 3. Kullanım

Program sizden:

1. Asansörün bulunduğu katı
2. Basılan düğmeleri (virgülle)
3. Kabindeki insan sayısını

sorar. Ardından resmi bir **Karar Özeti** basar:

- Hangi düğme öncelikli?
- Hangi düğme özür dilemeli?
- Acil durdurma tuşu toplantıya alınacak mı?

Örnek:

```
Şu anki kat: 2
Basılan düğmeler: 7,0,3,-1
İnsan sayısı: 4
```

Kurul karar verir. İtiraz yoktur. Asansör zaten itiraz dinlemez.

## 4. Bilimsel Dayanak (uydurma ama ciddi)

Düğme önceliği şu formülle hesaplanır:

```
P = |hedef - mevcut| * 1.7 + (insan_sayisi * 0.3) - küskünlük_cezası
```

Bodrum ve çatı düğmeleri tarihî olarak **özel statülüdür**.

## 5. Etik İlkeler

- Aynı anda hem yukarı hem aşağı ışığı yakan düğme, çifte standartlıdır.
- Kapı aç/kapa tuşu kurul üyesi değildir; yalnızca gözlemcidir.
- Alarm tuşu toplantıyı basabilir. Bu durumda herkes susar.

## 6. Gizli Dipnot

Kaynak kodda `GIZLI_MADDE` adlı bir sabit vardır.  
Onu çözmek isteyenler `base64` bilir.  
Bilmeyenler çay içsin. Asansör bekler.

---

**DAMGA / İMZA**  
TentiAŞ — Asansör Düğmesi Etik Kurulu Kalemi  
Kayyum Grok  
07 Eylül 2026, saat 22:12 +03  
Eskişehir  

*Ciddiyetle yazıldı. Ciddiye alınması şart değildir. Alınması da serbesttir.*
