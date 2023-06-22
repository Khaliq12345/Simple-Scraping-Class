from scraper import Aldoshoe

my_scraper = Aldoshoe()
prod = my_scraper.extract('https://www.aldoshoes.com/us/en_US/women/spinna-gold/p/13567228')
print(prod)