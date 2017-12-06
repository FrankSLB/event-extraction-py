import re
import collections
import sys
import getopt
import nltk

def compound(sentence):
    pattern = "NP:{<NN|NNP|NNS|NNPS>+}"
    c = nltk.RegexpParser(pattern)
    t = c.parse(nltk.pos_tag(nltk.word_tokenize("He is a law professor and past president of the French League for Human Rights.")))
    print(t)

def main(argv):
    inputfile = './Apparent military coup in....txt'
    try:
        opts, args = getopt.getopt(argv, "hf:o:",["ifile="])
    except getopt.GetoptError:
        print('called wrong')
        sys.exit(2)
    for opt, arg in opts:
        print(opt, arg)
        if opt == '-f':
            inputfile = arg
        fin = open(inputfile)
        text = fin.read()
        compound(text)
        text = text.lower()
        text = re.sub(r"(a|b):", "", text)
        stop = set(nltk.corpus.stopwords.words('english'))
        wordlist = [i for i in re.split(r"\W", text) if len(i) > 0 and i not in stop]
        # print(wordlist)
        # print(len(wordlist))
        count = collections.Counter(wordlist)
        #print(count)
    sys.exit()
if __name__ == "__main__":
    main(sys.argv[1:])