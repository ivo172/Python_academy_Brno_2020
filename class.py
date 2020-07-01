
#class Zdravic:
#    """ Třída reprezentuje zdravič, který slouží ke zdravení uživatelů
#    """
#    def __init__(self):
#        self.text = None
#
#    def pozdrav(self, jmeno):
#        """
#        Vrátí pozdrav uživatele s nastaveným textem a jeho jménem.
#        """
#        return '{0} {1}!'.format(self.text, jmeno)
#
#zdravic = Zdravic()
#zdravic.text = 'Ahoj uzivateli'
#print(zdravic.pozdrav('Karel'))
#print(zdravic.pozdrav('Petr'))
#zdravic.text = 'Vitej programatore'
#print(zdravic.pozdrav('Ivo'))
#input()


class Clovek:
    def __init__(self, jmeno: str, rok_narozeni: int, pohlavi = 'Muz', narodnost = 'Cech' ):
        self.__jmeno = jmeno
        self.__rok_narozeni = rok_narozeni
        self.__pohlavi = pohlavi
        self.__narodnost = narodnost

    def vrat_datum_narozeni(self):
        return self.__rok_narozeni

    def vrat_pohlavi(self):
        return self.__pohlavi

aneta = Clovek('Aneta', 1991, pohlavi='Zena')
ivo = Clovek('Ivo', 1965)
hana = Clovek('Hana', 1965, pohlavi='Zena')

print(aneta.vrat_datum_narozeni())
print(Clovek.vrat_datum_narozeni(aneta))
print(ivo.vrat_datum_narozeni())
print(hana.vrat_pohlavi(), hana.vrat_datum_narozeni())



