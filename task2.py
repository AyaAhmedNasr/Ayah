from nltk.tokenize import word_tokenize,sent_tokenize
text=input("inter your text")
print("1: tokenize words 2: tokenize sentence 3: original text")
choice=input("choose your number")
if choice=="1":
    print(word_tokenize(text))
elif choice == "2":
    print(sent_tokenize(text))
elif choice =="3":
    print(text)
else:
    print("wrong choice ")



#“ NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.”


