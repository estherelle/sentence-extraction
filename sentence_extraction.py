import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict

def get_sentences(url):
	# url = "http://www.elevate-hr.com/about-us/"

	# perform GET request to target url
	r = requests.get(url)
	s = BeautifulSoup(r.text, "lxml")


	# substitute extra whitespace with single newline
	bod_sub = re.sub(r'(\t|\n|\s)*\n(\t|\n|\s)*', '\n\n',s.getText(separator=u' '))
	# strip trailing whitespace
	bod_sub = bod_sub.strip()


	# replace newlines
	# bod_stripped = bod_sub.replace('(.|!|?)\n', '. ')
	bod_stripped = bod_sub.replace('.\n', '. ')
	bod_stripped = bod_stripped.replace('!\n', '. ')
	bod_stripped = bod_stripped.replace('Inc.', 'Incorporated')
	bod_stripped = bod_stripped.replace('?\n', '. ')


	# takes care of sentences that dont' end with periods- extra newline blocks were
	# replaced by a single newline in line 15
	bod_s = re.sub(r'(([a-z])|([A-Z]))+\n(([a-z])|([A-Z]))+', ' ',bod_stripped)
	stripped_newlines = bod_s.replace('\n\n', '. ')
	stripped_newlines = bod_s.replace('\n', ' ')

	# strip any remaining trailing whitespace (probably unnecessary)
	stripped_newlines = stripped_newlines.strip()

	# split by sentences and add back period at the end of each sentence
	stripped = stripped_newlines.split('.')
	stripped = [(strip + '.') for strip in stripped]

	cleaned = []

	stopwords = ["function", "{", "}", "https", "http", "href", ");", "javascript", "return", "async", "]", "crossorigin", "error", "js", "()", "var ", "*", "invoked", "\"/\""]
	for strip in stripped:
		separated = strip.split(' ')
		if len(separated) > 3:
			stopped = False
			for stopword in stopwords:
				if stopword in strip:
					stopped = True
					break
			if not stopped:
				cleaned.append(strip)

	return " ".join(cleaned), cleaned

# url = "http://www.elevate-hr.com/about-us/"
# text, arr = get_sentences(url)
# print(text)