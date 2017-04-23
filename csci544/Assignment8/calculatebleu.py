import os
import sys
import math
from collections import Counter
candidates = []
references = []

def readCandidateFile():
	candidateFileName = sys.argv[1]
	file = open(candidateFileName, "r", encoding = "utf-8")
	for line in file.readlines():
		candidates.append(line.strip())

def readReferenceFile():
	referencePath = sys.argv[2]
	global references
	if os.path.isdir(referencePath):
		for root,dirs,files in os.walk(referencePath):
			for referenceFileName in files:
				file = open(os.path.join(root,referenceFileName), "r", encoding = "utf-8")
				line_number = 0
				temp = []
				for line in file.readlines():
					temp.append(line.strip())
					line_number += 1
				references.append(temp)

	else:
		file = open(referencePath, "r", encoding = "utf-8")
		references.append([])
		for line in file.readlines():
			references[0].append(line.strip())

def getNGrams(input, n):
  input = input.split(' ')
  output = []
  if (len(input) < n):
  	return Counter(output)
  for i in range(len(input)-(n-1)):
  	output.append(' '.join(input[i:i+n])) 
  return Counter(output)

def countNGrams(candidate, n, line_number):
	# print (candidate)
	candidateNGrams = getNGrams(candidate, n)
	# print (candidateNGrams)
	max_ngram_count = {}
	for reference in references:
		referenceNGrams = getNGrams(reference[line_number], n)
		for c_ngram in candidateNGrams:
			max_ngram_count[c_ngram] = max(max_ngram_count.get(c_ngram, 0) , referenceNGrams[c_ngram])
	clip_count = 0
	ngram_count = 0
	for c_ngram in candidateNGrams:
		clip_count = clip_count + min(candidateNGrams[c_ngram], max_ngram_count[c_ngram])
		ngram_count = ngram_count + candidateNGrams[c_ngram] 
	return clip_count, ngram_count

def brevity_penalty():
	total_candidate_count = 0 
	total_reference_count = 0
	line_number = 0
	for c in candidates:
		candidate_len = len(c.split(' '))
		ans = len(references[0][line_number].split(' '))
		total_candidate_count += candidate_len
		diff = abs(len(references[0][line_number].split(' ')) - candidate_len)
		for reference in references:
			reference_len = len(reference[line_number].split(' '))
			if abs(candidate_len - reference_len) < diff:
				diff = abs(candidate_len - reference_len)
				ans = reference_len
		total_reference_count += ans
		line_number = line_number + 1
	# print (total_candidate_count)
	# print (total_reference_count)
	if (total_candidate_count > total_reference_count):
		return float(1)
	else:
		return math.exp(1 - float(total_reference_count / total_candidate_count))

def calculateBLEU():
	bleu_score = 0.0
	for i in range(1,5):
		# print (i)
		total_clip_count = 0
		total_ngram_count = 0
		line_number = 0
		# print (len(candidates))
		for c in candidates:
			clip_count,ngram_count = countNGrams(c, i, line_number)
			total_clip_count += clip_count
			total_ngram_count += ngram_count
			line_number = line_number + 1
		
		# print (total_clip_count, " ", total_ngram_count)
		p_n = float(float(total_clip_count) / float(total_ngram_count))
		w_n = 0.25
		bleu_score = bleu_score + (math.log(p_n) * 0.25)
	# print (bleu_score)
	bleu_score = math.exp(bleu_score)
	bp = brevity_penalty()
	# print (bp)
	bleu_score = bp * bleu_score
	with open('bleu_out.txt','w',encoding='utf-8') as f:
		f.write(str(bleu_score))
	# print (bleu_score)


readCandidateFile()
readReferenceFile()
# print (references)
calculateBLEU()











