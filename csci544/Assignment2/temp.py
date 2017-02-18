import json
import string
import re

wordCount = {}
#extraWords= ["a","an", "and","are","as","at","be","by","for","from","has","he","in","is","it","its","of","on","that","the","to","was","were","will","with","am",
#"pm","whose","why","will","with","would","what","when","where","whether","which","while","who","we","i","I","not","had","have","how","stay","breakfast"]

extraWords = ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']
def getWords(text):
    return re.compile('\w+').findall(text)

with open("sample-train-labels.txt","r") as f:
    content_labels = f.readlines()
    content_labels = [x.strip() for x in content_labels]
    #print(content)


my_dict_labels = {}
for lists in content_labels:
    words = list(lists.split())
    my_dict_labels[words[0]] = words[1:]

print(my_dict_labels)
print("REVIEW")


with open("sample-train-text.txt") as f:
    content_reviews = f.readlines()
    content_reviews = [x.strip() for x in content_reviews]
    #print(content)

label_count = {
    'deceptive' : 0,
    'positive' : 0,
    'negative' : 0,
    'truthful' : 0
}
def get_words_from_sentence(sentence):
    words = []
    global wordCount, label_count
    words_list = sentence.split(' ')
    if words_list[0] in my_dict_labels:
        labels = my_dict_labels[words_list[0]]
    else:
        print ("Error !!!!!!!!!!!!!!!")

    for word in words_list[1:]:
        word = word.strip(string.punctuation).lower()
        if (word in extraWords) or (not word):
            continue
        if word not in wordCount:
            wordCount[word] = {}
            for x in label_count:
                wordCount[word][x] = 0
        for label in labels:
            wordCount[word][label] = wordCount[word][label] + 1
            label_count[label] = label_count[label] + 1 

my_dict_reviews = {}
for lists in content_reviews:
    #words = list(lists.split())
    #print(words)
    words = get_words_from_sentence(lists)

probability = {}
V = len(wordCount)
for wordc in wordCount:
    if (wordc not in probability):
        probability[wordc] = {}
    for lc in label_count:
        probability[wordc][lc] = float(wordCount[wordc][lc] + 1) / float(label_count[lc] + V)
prior = {}
prior['positive'] = label_count['positive'] / (label_count['positive'] + label_count['negative'])
prior['negative'] = label_count['negative'] / (label_count['positive'] + label_count['negative'])
prior['truthful'] = label_count['truthful'] / (label_count['truthful'] + label_count['deceptive'])
prior['deceptive'] = label_count['deceptive'] / (label_count['truthful'] + label_count['deceptive'])

# print (wordCount)
# print (label_count)
# print (prior)

print (probability)
p = {}
p['prior_pro'] = prior
merge = probability.copy()
merge.update(p)

fp = open("nbmodel.txt", 'w')
json.dump(merge,fp)
