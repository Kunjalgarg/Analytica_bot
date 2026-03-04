import nltk 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk import word_tokenize
from nltk import ne_chunk
from re import split
# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('maxent_ne_chunker_tab')
# nltk.download('words')
import re


text = "Hello! I am Kunjal.A paragraph is a self-contained unit of writing, a collection of sentences grouped around a single main idea or topic, used to organize text, break up long passages, and guide readers through an author's points. Key components include a topic sentence (expressing the main idea), supporting sentences (providing details, examples, or explanations), and often a concluding sentence. Paragraphs structure discourse, making longer texts more digestible and showing logical divisions in thought.Hello my Number is 123456789 and my friend's number is 987654321"
# word= word_tokenize(text)

# print(sent_tokenize(text))

# print (FreqDist(word))

# porter= PorterStemmer()
# print(porter.stem("play"))
# print(porter.stem("playing"))
# print(porter.stem("played"))
# print(porter.stem("plays"))
# print(porter.stem("communication"))
# print(porter.stem("supercalifragilisticexpialidocious"))

# lem=WordNetLemmatizer()
# print(lem.lemmatize("communication"))

# tokenized_text = word_tokenize(text)
# tags = tokens_tag = pos_tag(tokenized_text)
# print(tags)

# tokens = word_tokenize(text)
# tags = pos_tag(tokens)

# entities = ne_chunk(tags)
# print(entities)

# match=re.search(r'Kunjal',text)
# print('start', match.start())
# print('end',match.end())

regex='\d+'
match=(re.findall(regex, text))
print(match)

# p=re.compile('\w')
# print(p.findall(text))
# p=re.compile('\w+')
# print(p.findall(text))
# p=re.compile('\W')
# print(p.findall(text))

# p = re.compile('ab*')
# print(p.findall("ababbaabbb"))

# print(split('\W+', 'Words, words , Words'))
# print(split('\W+', "Word's words Words"))
# print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
# print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))

# print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))
# print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))
# print(re.split('[a-f]+','Aey, Boy oh boy, come here'))

# print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
# print(re.sub('ub', '~*', 'Subject has Uber booked already'))
# print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
# print(re.sub(r'\sAND\s', ' & ', 'Bread AND Butter', flags=re.IGNORECASE))

s = "Welcome to GeeksForGeeks"
res = re.search(r"\bG", s)
print(res.re)
print(res.string)












