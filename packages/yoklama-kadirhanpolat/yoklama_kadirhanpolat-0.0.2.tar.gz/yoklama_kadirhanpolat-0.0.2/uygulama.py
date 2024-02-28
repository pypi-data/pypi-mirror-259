from yoklama import *

# Sabitler
dersAdi = "Nümerik Analiz II"
dersKisaAdi = "Nüm. Ana. II"
kaynakDosyaYolu = f"Yoklama/Kaynaklar/{dersAdi}.xlsx"
hedefDosyaYolu = f"Yoklama/Ciktilar/{dersAdi} - Yoklama.xlsx"
universiteAdi = "Ağrı İbrahim Çeçen Üniversitesi"
birimAdi = "Fen Edebiyat Fakültesi"
bolumAdi = "Matematik"
donem = 2
yariyilBaslangicTarihi = "19/02/2024"
yariyilBitisTarihi = "31/05/2024"
dersinSorumlusu = "Kadirhan POLAT"
dersinKodu = "MATE404"
dersinHaftalikGunleri = ["Salı","Perşembe"]

yoklama = Yoklama(kaynakDosyaYolu,
                  hedefDosyaYolu,
                  universiteAdi,
                  birimAdi,
                  bolumAdi,
                  donem,
                  yariyilBaslangicTarihi,
                  yariyilBitisTarihi,
                  dersAdi,
                  dersKisaAdi,
                  dersinSorumlusu,
                  dersinKodu,
                  dersinHaftalikGunleri)

# print(yoklama.ders.ad)
# print(yoklama.ders.sorumlu)
# print(yoklama.ders.kod)
# print(yoklama.ders.kredi)
# print(yoklama.ders.haftalikGunler)
# print(yoklama.ders.haftalikGunSiralari)
# print(yoklama.yariyil.baslangicTarihi)
# print(yoklama.yariyil.bitisTarihi)
# print(yoklama.yariyil.toplamSaniye)
# print(yoklama.yariyil.toplamGun)
# print(yoklama.yariyil.toplamHafta)
# print(yoklama.toplamSutun)

yoklama.yoklamaDosyasiOlustur()



