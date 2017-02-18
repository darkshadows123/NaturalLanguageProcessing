import re
import sys
import string
import json
import math

testing = False
map_reviews = {}
nbProbabilites = {}
map_labels = {}
nbclass_count = {
	'deceptive':0,
	'truthful':0,
	'positive':0,
	'negative':0
}
prior = {
	'deceptive':0,
	'truthful':0,
	'positive':0,
	'negative':0
}
stopWords = ['i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']

pos_t_p = 0
pos_f_p = 0
pos_f_n = 0
pos_recall = 0
pos_precision = 0
pos_f1 = 0

tru_t_p = 0
tru_f_p = 0
tru_f_n = 0
tru_recall = 0
tru_precision = 0
tru_f1 = 0
correct_predictions = 0
predicted_labels = []

def readTestFile():
	with open(sys.argv[1], 'r') as f:
	    reviews = f.readlines()
	for review in reviews:
		r_split = review.split(' ',1)
		map_reviews[r_split[0]] = ' '.join(r_split[1:]).strip()

def readLabelFile():
	with open('test-labels.txt', 'r') as f:
	    labels = f.readlines()
	for label in labels:
		l_split = label.split(' ')
		# print (l_split[0])
		map_labels[l_split[0]] = ' '.join(l_split[1:]).strip()  
	# print (map_labels)
	
def readModelFile():
	with open("nbmodel.txt", 'r') as fp:
		global nbProbabilites, prior
		nbProbabilites = json.load(fp)
	prior = nbProbabilites['prior_probability']
	print (prior)
	del (nbProbabilites['prior_probability'])

def getWords(review_sentence):
	review_words = []
	for word in review_sentence.split():
		word = word.strip(string.punctuation).lower()
		if not word:
			continue
		if word in stopWords:
			# print ("word = ", word)
			continue
		review_words.append(word)
	return review_words

def calculatePrior():
	prior['deceptive'] = nbclass_count['deceptive'] / (nbclass_count['deceptive'] + nbclass_count['truthful'])
	prior['truthful'] = nbclass_count['truthful'] / (nbclass_count['deceptive'] + nbclass_count['truthful'])
	prior['positive'] = nbclass_count['positive'] / (nbclass_count['positive'] + nbclass_count['negative'])	
	prior['negative'] = nbclass_count['negative'] / (nbclass_count['positive'] + nbclass_count['negative'])

def calculatePosterior(words, nbClass):
	# print (prior[nbClass])
	score = math.log(prior[nbClass])
	for word in words:
		if not word:
			continue
		if word in nbProbabilites.keys():
			score = score + math.log(nbProbabilites[word][nbClass])
	return score

def getLabels(key, words):
	label2 = 'positive'
	label1 = 'truthful'
	global pos_t_p,pos_f_p,pos_f_n,tru_t_p,tru_f_p,tru_f_n
	if (calculatePosterior(words, 'positive') > calculatePosterior(words, 'negative')):
		label2 = 'positive'
		if (testing):
			if key in map_labels:
				if map_labels[key].split(' ')[1] == 'positive':
					pos_t_p = pos_t_p + 1
				else:
					pos_f_p = pos_f_p + 1
			else:
				print ("Error!!!!!!!!!!!!!!!!!")
	else:
		label2 = 'negative'
		if (testing):
			if key in map_labels:
				if map_labels[key].split(' ')[1] == 'positive':
					pos_f_n = pos_f_n + 1

	if (calculatePosterior(words, 'truthful') > calculatePosterior(words, 'deceptive')):
		label1 = 'truthful'
		if (testing):
			if key in map_labels:
				if map_labels[key].split(' ')[0] == 'truthful':
					tru_t_p = tru_t_p + 1
				else:
					tru_f_p = tru_f_p + 1
			else:
				print ("Error!!!!!!!!!!!!!!!!!")
	else:
		label1 = 'deceptive'
		if (testing):
			if key in map_labels:
				if map_labels[key].split(' ')[0] == 'truthful':
					tru_f_n = tru_f_n + 1
	return label1,label2

def classify():
	global correct_predictions
	for key in map_reviews:
		words = getWords(map_reviews[key])
		label1,label2 = getLabels(key,words)
		if (testing):
			if ((label1 == map_labels[key].split(' ')[0]) and (label2 == map_labels[key].split(' ')[1])):
				correct_predictions = correct_predictions + 1
		predicted_labels.append(key + ' ' + label1 + ' ' + label2 + '\n')

def calculateF1():
	global pos_f1,tru_f1
	try:
		pos_precision = float(pos_t_p) / (float(pos_t_p) + float(pos_f_p)) 
		pos_recall = float(pos_t_p) / (float(pos_t_p) + float(pos_f_n))
		pos_f1 = (2 * pos_precision * pos_recall) / (pos_precision + pos_recall)
	except:
		pos_f1 = 0.0
	try:
		tru_precision = float(tru_t_p) / (float(tru_t_p) + float(tru_f_p)) 
		tru_recall = float(tru_t_p) / (float(tru_t_p) + float(tru_f_n))
		tru_f1 = (2 * tru_precision * tru_recall) / (tru_precision + tru_recall)
	except:
		tru_f1 = 0.0
	# print (pos_t_p,pos_t_p,pos_f_p)
	# print (pos_f1)
	# print (tru_f1)

readModelFile()
readTestFile()
if (testing):
	readLabelFile()
# calculatePrior()
classify()
calculateF1()

# print (prior)
print ("pos_f1 = ", pos_f1)
print ("tru_f1 = ", tru_f1)
print ("average = ", (tru_f1 + pos_f1) / 2)
print (correct_predictions)
# print (nbProbabilites)
# print (nbclass_count)
predicted_labels.sort()
# print (type(nbProbabilites['absence']['negative']))
with open("nboutput.txt","w") as f:
	for predicted_label in predicted_labels:
		# print (predicted_label)
		f.write(predicted_label)
