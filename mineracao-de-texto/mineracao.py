import re
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

text = 'Deverão ser criadas planilhas com dados dos usuários'

tokens = word_tokenize(text)
# Transforma para lower case
tokens = [w.lower() for w in tokens]
# Remove pontuações

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# Remove restante dos caracteres que não são alfa numéricos
words = [word for word in stripped if word.isalpha()]

#Retira stop words
stop_words = set(stopwords.words('portuguese'))
words = [w for w in words if not w in stop_words]

#Realiza stemming

porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]

print(stemmed)