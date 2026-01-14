class India:
    def capital(self):
        print("India's capital is New Dehli")
    def language(self):
        print("India's widely spoken language is Hindi")
    def country(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("USA'S Capital is Washington D.C")
    def language(self):
        print("USA'S primary language is English")
    def country(self):
        print("USA is a developed country")
ind = India()
usa = USA()
for country in (ind, usa):
    country.capital()
    country.language()
    country.country()
