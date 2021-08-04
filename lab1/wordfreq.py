def tokenize(lines):
	words = []
	for line in lines:
		line = line.lower()
		start = 0
		end = 0
		while end < len(line):
			if(line[end].isspace()):
				if(start < end):
					words.append(line[start:end])
					start = end + 1
				else:
					start += 1
			elif(line[end].isalpha()):
				if(end > 0 and line[end - 1].isdigit()):
					words.append(line[start:end])
					start = end
			elif(line[end].isdigit()):
				if(end > 0 and line[end - 1].isalpha()):
					words.append(line[start:end])
					start = end
			else:
				if(end > 0 and (line[end - 1].isalpha() or line[end - 1].isdigit())):
					words.append(line[start:end])
				words.append(line[end])
				start = end + 1
			end += 1
			if(end == len(line) and start < end):
				words.append(line[start:end])
	return words

def countWords(words, stopWords):
	count = dict()
	for word in words:
		if word not in stopWords:
			if word in count:
				count[word] += 1
			else:
				count[word] = 1
	return count
	
def printTopMost(count, n):
	count = sorted(count.items(), key=lambda x: -x[1])
	i = 0
	while i < n and i < len(count):
		print(count[i][0].ljust(20) + str(count[i][1]).rjust(5))
		i += 1

