class Motorsykkel:
    def __init__(self, merke, regnummer, kmavstand):
        self.merke = merke
        self.regnummer = regnummer
        self.kmavstand = kmavstand
    
    def kjor(self, km):
        self.kmavstand += km
    
    def hentKilometerstand(self):
        return self.kmavstand
    
    def skrivUt(self):
            print("Merke: ", self.merke)
            print("Regnummer: ", self.regnummer)
            print("Kilometerstand: ", self.kmavstand)
    

