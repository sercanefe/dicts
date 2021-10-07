#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 00:39:02 2021

@author: sercan
"""

"""
dictionary - sözlük

Sözlükler veya İngilizce ismiyle dictionaryler aynı gerçek hayattaki sözlükler gibi davranan bir veritipidir.
Bu veritipi, şimdiye kadar gördüğümüz tüm veritiplerinden yapısı gereği farklıdır.
Sözlüğün içindeki her bir eleman indeks ile değil, anahtar (key), değer (value) olarak tutulur. 
Bu anlamda gerçek hayattaki sözlüklere oldukça benzerler. 
Örneğin, elimize bir ingilizce-Türkçe sözlük alıp freedom kelimesini(key ya da anahtar) aradığımız zaman 
karşılık değer özgürlük (değer ya da value) olarak karşımıza çıkar. 
Sözlükleri de bu şekilde düşünebiliriz.

Şimdi isterseniz bir sözlük oluşturarak konumuza başlayalım.
"""

# Sözlük Oluşturmak
# Süslü Parantez ve iki nokta (:) ile anahtar değerlerimizi yerleştirelim.
sozluk1 = {"bir":1, "iki":2, "üç":3}
print(sozluk1)

# Boş bir sözlük
sözlük2 = {}

# Boş bir sözlük - dict() ile 
sözlük2 = dict()

print(sozluk2)

"""
Sözlük Değerlerine Erişmek ve Sözlüğe Değer Eklemek
Sözlük veritipinin gerçek hayattaki sözlüklere çok benzediğini söylemiştik.
Öyleyse, bir değeri (value) elde etmek için, indeksleri değil anahtarları (key) kullanacağız.
"""

# "bir" anahtarına karşılık gelen değeri buluyoruz.
sözlük1["bir"]

# "iki" anahtarına karşılık gelen değeri buluyoruz.
sözlük1["iki"]

"""
Olmayan bir anahtar
sözlük1["beş"]
"""

a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}

# "iki" anahtarının değeri
a["iki"]

# İç içe listeleri biliyoruz.
a["iki"][1][1]

a["üç"]

a["üç"] += 5
print(a["üç"])

print(a)

# Bir sözlüğe dinamik olarak da eleman ekleyebiliriz.
# Sözlük oluşturalım.
a = {"bir":1,"iki":2,"üç":3}

a["dört"] = 4 
print(a)

"""
Dikkat ederseniz yeni eklediğimiz anahtar ve değer sözlüğün sonuna eklenmedi.
Burada sözlüklerin bir özelliğini daha görüyoruz.
Sözlükler diğer veri tiplerinden farklı olarak sıralı olmayan bir veri tipidir.
"""

"""
İç içe Sözlükler

Tıpkı listeler gibi, iç içe sözlükler de oluşturulabilir.
"""

b = {"numbers" : {"one":1, "two":2, "three":3},"meyveler" : {"kiraz":"yaz",  "portakal","kış", "erik":"yaz"}}

print(b["numbers"]["one"])

print(b["meyveler"]["kiraz"])

"""
Temel Sözlük Metodları
"""

yeni_sozluk = {"bir":1,"iki":2,"üç":3}

# values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
print(yeni_sozluk.values())

# keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
print(yeni_sozluk.keys())

# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
print(yeni_sozluk.items())


for x,y in sozluk1.items():
    print(x,y)