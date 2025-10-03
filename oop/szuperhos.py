class Szuperhos():
    def __init__(self, nev, szuperero=50):
        self.nev = nev
        self.szuperero = szuperero
        self.__szuperero = szuperero #private

thor = Szuperhos(nev= "Thor", szuperero= 100)
batman = Szuperhos("Batman")

# getter metódus
def get_szuperero(self):
    return self.__szuperero

# setter metódus
def set_szuperero(self, szuperero):
    self.__szuperero = szuperero

    #property
    @property
    def nev(self):
        return self.__nev

    #@adattag.setter
    @nev.setter
    def nev(self, ertek):
        self.__nev = ertek

    def __str__(self): #ToString
        return (f"Név: {self.__nev} egy szuperhős, akinek a"
                f"szupereje: {self.__szuperero}")

# In Python, “dunder” is short for “double underscore” — it refers to any method or variable name that starts and ends with two underscores like this:

     #Operator overloading
    #  két szuperhős, akkor lesz egyenlő, ha a nevük és a szupererejük megegyezik
    def __eq__(self, other):
        if isinstance(other, Szuperhos):
            return self.__nev == other.__nev and self.__szuperero == other.__szuperero
        else:
            print("Egy szuperhőst csak egy másik szuperhősseé lehet összehasonlítani")


thor = Szuperhos(nev = "Thor", szuperero = 100)
batman = Szuperhos("Batman")
print(thor.__Szuperhos__szuperero)
thor.set_szuperero(200)
print(thor.get_szuperero())
thor.nev = "God of Thunder"
print(thor.nev)
print(thor)
print(isinstance("42", int))