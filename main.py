def alo_talabalar(baholar):
    alo_talabalar = {talaba: baholar[talaba] for talaba, baholar in baholar.items() if baholar >= 90}
    return alo_talabalar

baholar = {
    "Ali": 85,
    "Vali": 92,
    "Hasan": 78,
    "Husan": 95,
    "Rustam": 88,
    "Abdulloh": 91,
    "Said": 76,
    "Tohir": 98,
    "Nuriddin": 82,
    "Abdulaziz": 94
}

alo_talabalar = alo_talabalar(baholar)
print(alo_talabalar)
```

Kodni ishlatish uchun quyidagilar kerak:

1. Baholangan talabalar lug'atini yaratish.
2. `alo_talabalar` funksiyasiga baholangan talabalar lug'atini berish.
3. Funksiya ichida lug'atdan "a'lo" talabalarni (baholari 90 dan yuqori bo'lganlar) ajratib olish uchun dictionary comprehension qo'llanish.
4. Natijani `alo_talabalar` deygarasida saqlab qo'yish.
5. Natijani konsolga chiqarish.
