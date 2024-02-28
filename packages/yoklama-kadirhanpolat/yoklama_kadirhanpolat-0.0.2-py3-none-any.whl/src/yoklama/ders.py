class Ders:
    def __init__(self, ad, kisaAd, sorumlu, kod, haftalikGunler):
        self.__haftaGunSirasi = {"Pazartesi":0, "Salı":1, "Çarşamba":2, "Perşembe":3, "Cuma":4, "Cumartesi":5, "Pazar":6}
        self.__haftaGunIsmi = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        self.__ad = ad
        self.__kisaAd = kisaAd
        self.__sorumlu = sorumlu
        self.__kod = kod
        self.__haftalikGunler = haftalikGunler
        self.__haftalikGunSiralari = list(map(lambda x : self.__haftaGunSirasi[x], self.__haftalikGunler))

    @property
    def ad(self) -> str:
        return self.__ad
    
    @property
    def kisaAd(self) -> str:
        return self.__kisaAd
    
    @property
    def sorumlu(self) -> str:
        return self.__sorumlu
    
    @property
    def kod(self) -> str:
        return self.__kod
    
    @property
    def haftalikGunler(self):
        return self.__haftalikGunler
    
    @property
    def haftalikGunSiralari(self):
        return self.__haftalikGunSiralari