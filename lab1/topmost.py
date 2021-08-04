import wordfreq
import sys
import urllib.request

def main():
	if(len(sys.argv) < 3):
		print("Too few arguments!")
		return

	file = False	
	if "http://" in sys.argv[2] or "https://" in sys.argv[2]:
		response = urllib.request.urlopen(sys.argv[2])
		inp_file = response.read().decode("utf-8").splitlines()
	else:
		file = True
		inp_file = open(sys.argv[2], "r")
	stopwords_file = open(sys.argv[1], "r")
	n = int(sys.argv[3])

	stopwords = []
	for line in stopwords_file:
		stopwords.append(str(line).strip('\n'))

	words = wordfreq.tokenize(inp_file)
	count = wordfreq.countWords(words, stopwords)
	wordfreq.printTopMost(count, n)
	if(file):
		inp_file.close()
	stopwords_file.close()

main()