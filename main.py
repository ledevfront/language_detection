from langdetect import detect
from langdetect import detect_langs
print(detect('salut comment allez vous'))
print((detect_langs("salut chien"))) # purcentage of language