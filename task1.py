Document1= 'new home sales top forecasts.'
Document2= 'home sales rise in July'
Document3= 'increase in home sales in July.'
Document4= 'July new home sales rise'
text =[Document1,Document2,Document3,Document4]
distinct_items= set()
for doc in text:
    for item in doc.split():
        distinct_items.add(item)

inverted_index = {}
for i, doc in enumerate(text):
    for term in doc.split():
        if term in inverted_index:
            inverted_index[term].add(i)
        else: 
            inverted_index[term] = {i}
posting_list = inverted_index['home']
print(posting_list)



