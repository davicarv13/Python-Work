from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import hunspell
import re
from unicodedata import normalize

def tokenize(sentence):
	#Retira acentos
	sentence = normalize('NFKD', sentence).encode('ASCII', 'ignore').decode('ASCII')

	tokens_regex = re.compile(r"([., :;\n()\"#!?1234567890/&%+])", flags=re.IGNORECASE)
	tokens = re.split(tokens_regex, sentence)
	postprocess = []
	postprocess_regex = re.compile(r"\b(\w+)-(me|te|se|nos|vos|o|os|a|as|lo|los|la|las|lhe|lhes|lha|lhas|lho|lhos|no|na|nas|mo|ma|mos|mas|to|ta|tos|tas)\b", flags=re.IGNORECASE)
	for token in tokens:
	    for token2 in re.split(postprocess_regex, token):
	        if token2.strip():
	            postprocess.append(token2)

	return postprocess

def lemmatizator(tokens):
	h = hunspell.HunSpell("/usr/share/hunspell/pt_BR.dic", "/usr/share/hunspell/pt_BR.aff")

	lemmas = [h.stem(word) for word in tokens]

	lista_lemmas = []

	for lemma in lemmas:
	    string = b''.join(lemma)
	    string = string.decode('utf-8')
	    lista_lemmas.append(string)

	return lista_lemmas

def text_cleaning(lemmatized_tokens):

	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in lemmatized_tokens]
	# Remove restante dos caracteres que não são alfa numéricos
	words = [word for word in stripped if word.isalpha()]

	#Retira stop words
	stop_words = set(stopwords.words('portuguese'))
	words = [w for w in words if not w in stop_words]

	#Realiza stemming

	porter = PorterStemmer()
	stemmed = [porter.stem(word) for word in words]

	return stemmed

text = "Crie planilhas com dados do usuário"

tokens = tokenize(text)

lemma = lemmatizator(tokens)

print(text_cleaning(lemma))


