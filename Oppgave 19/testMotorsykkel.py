from motorsykkel import Motorsykkel

def hovedprogram():
    motorsykkel1 = Motorsykkel("Yamaha", "BR 45652", 10000)
    motorsykkel2 = Motorsykkel("Honda", "BR 12345", 20000)
    motorsykkel3 = Motorsykkel("Suzuki", "BR 67890", 30000)

    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()

    motorsykkel3.kjor(10)
    motorsykkel3.skrivUt()

hovedprogram()
