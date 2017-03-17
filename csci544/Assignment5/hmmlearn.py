import os
import sys
import json
path = sys.argv[1]

words = {}
tags = {}
start_state_count = {}
start_probability = {}
tag_count = {}
formatted_input = []
total_lines = 0

def readInput():
	print(path)
	global total_lines
	fp = open(path,'r')
	for line in fp.readlines():
		if not line.strip():
			continue
		else:
			total_lines = total_lines + 1
			tagged_words = line.strip().split(' ')
			i = 0
			formatted_sentence = []
			for tagged_word in tagged_words:
				split_text = tagged_word.rsplit('/', 1)
				word = split_text[0]
				tag =  split_text[1]
				formatted_word = {
					'word' : word,
					'tag' : tag
				}
				if tag in tag_count:
					tag_count[tag] = tag_count[tag] + 1
				else:
					tag_count[tag] = 1
				# print(tag)
				if i == 0:
					if tag in start_state_count:
						start_state_count[tag] = start_state_count[tag] + 1
					else:
						start_state_count[tag] = 1
				i = i + 1
				formatted_sentence.append(formatted_word)
		formatted_input.append(formatted_sentence)

def calculateStartProbability():
	for tag,count in start_state_count.items():
		start_probability[tag] = float(count) / float(total_lines)
def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError
def calculateTransitionProbability():
		prev_tag = 'q0'
		transition_count = {}
		emission_count = {}
		for line in formatted_input:
			for word_tag in line:
				if (prev_tag in transition_count):
					if (word_tag['tag'] in transition_count[prev_tag]):
						transition_count[prev_tag][word_tag['tag']] = transition_count[prev_tag][word_tag['tag']] + 1
					else:
						transition_count[prev_tag][word_tag['tag']] = 1
				else:
					transition_count[prev_tag] = {}
					transition_count[prev_tag][word_tag['tag']] = 1
				prev_tag = word_tag['tag']
				if word_tag['tag'] in emission_count:
					if word_tag['word'] in emission_count[word_tag['tag']]:
						emission_count[word_tag['tag']][word_tag['word']] += 1
					else:
						emission_count[word_tag['tag']][word_tag['word']] = 1
				else:
					emission_count[word_tag['tag']] = {}
					emission_count[word_tag['tag']][word_tag['word']] = 1
		print (transition_count)
		transition_prob = {}
		for cur_tag in transition_count:
			next_tag_prob = []
			for next_tag in tag_count:
				if next_tag in transition_count[cur_tag]:
					num = (transition_count[cur_tag][next_tag] + 1)
				else:
					num = 1
				if cur_tag == 'q0':
					den = total_lines + len(tag_count)
				else:
					den = tag_count[cur_tag] + len(tag_count)
				prob = num / den

				tag_prob = {
					'next_tag' : next_tag,
					'prob' : prob
				}
				next_tag_prob.append(tag_prob)
			transition_prob[cur_tag] = next_tag_prob
		# print (transition_prob)

		emission_prob = {}
		for tag in emission_count:
			emission_prob[tag] = {}
			for word in emission_count[tag]:
				emission_prob[tag][word] = emission_count[tag][word] / tag_count[tag]
		m_prob = {} 
		m_prob['transition_prob'] = transition_prob
		m_prob['emission_prob'] = emission_prob
		with open('hmmmodel.txt', 'w') as wfile:
			json.dump(m_prob, wfile, default=decimal_default)
readInput()
# print (start_state_count)
# print (formatted_input)
calculateStartProbability()
calculateTransitionProbability()
