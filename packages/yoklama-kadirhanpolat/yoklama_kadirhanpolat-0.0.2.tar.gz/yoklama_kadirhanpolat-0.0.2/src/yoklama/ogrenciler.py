import pandas as pd

class Ogrenciler:
    def __init__(self, dersAdi):
        self.__ogrenciler = self.__ogrencileriOku(dersAdi)
    
    def __ogrencileriOku(self,dersAdi) -> pd.DataFrame:
        dosyaYolu = f"Yoklama/Kaynaklar/{dersAdi}.xlsx"
        ogrenciler = pd.read_excel(dosyaYolu)
        ogrenciler.columns = ["Öğrenci No", "Ad", "Soyad", "Sınıf", "Alış Tipi", "Not", "Fakülte", "Program"]
        return ogrenciler
    
    def __getitem__(self, key):
        row, column = key
        return self.__ogrenciler[row, column]
    
    def __iter__(self):
        yield from self.__ogrenciler

