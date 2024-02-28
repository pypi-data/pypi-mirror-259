from datetime import datetime, timedelta

class Yariyil:
    def __init__(self, donem, baslangicTarihiMetni, bitisTarihiMetni):
        
        self.__donem = donem

        self.__baslangicTarihi = datetime.strptime(
            baslangicTarihiMetni,"%d/%m/%Y")
        
        self.__bitisTarihi = datetime.strptime(
            bitisTarihiMetni,"%d/%m/%Y")
        
        self.__toplamSaniye = int((self.bitisTarihi - self.baslangicTarihi + timedelta(days=3)).total_seconds())

        self.__toplamGun = self.__toplamSaniye // (60 * 60 * 24)

        self.__toplamHafta = self.__toplamGun // 7
    
    @property
    def donem(self) -> int:
        return self.__donem

    @property
    def baslangicTarihi(self) -> datetime:
        return self.__baslangicTarihi
    
    @property
    def bitisTarihi(self) -> datetime:
        return self.__bitisTarihi

    @property
    def toplamSaniye(self) -> int:
        return self.__toplamSaniye

    @property
    def toplamGun(self) -> int:
        return self.__toplamGun

    @property
    def toplamHafta(self) -> int:
        return self.__toplamHafta