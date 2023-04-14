import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
pstem=PorterStemmer()
sball=SnowballStemmer(language='english')
text=input("put the text")
print("1: tokenize words 2: tokenize sentence 3: original text 4: stemming 4.1: Snowball 4.2: Porter")
choice=input("select number")
if choice=="1":
    print(word_tokenize(text))
elif choice == "2":
    print(sent_tokenize(text))
elif choice =="3":
    print(text)
elif choice =="4.1":
    print(pstem.stem(text))
elif choice =="4.2":
    print(sball.stem(text))
else:
    print("wrong choice ")
